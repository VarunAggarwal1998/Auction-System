from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.core.mail import send_mail
from django.conf import settings
from django.conf import settings
from django.db import models
from datetime import timedelta
from django.utils import timezone

class User(AbstractUser):
    pass

    def __str__(self):
        return f"User id: {self.id} | Username: {self.username}"

    def get_username(self):
        return self.username


# define the models of category
class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"


# define the model of a auction list
class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    starting_bid = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    current_bid = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="auction_category", blank=True, null=True) # related_name search all the auctions with a given category
    imageURL = models.URLField(blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auction_seller")
    closed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
    # lastBid = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True) 
    end_time = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"Auction id: {self.id} | Title: {self.title} | Seller: {self.seller} | Closed: {self.closed}"
    
    def get_fields(self):
        return [(field.name, getattr(self, field.name)) for field in Auction._meta.fields]

    def is_active(self):
        return timezone.now() < self.end_time if self.end_time else False

# define the model of a bid
class Bid(models.Model):
    bider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid_date = models.DateTimeField(auto_now_add=True)
    bid_price = models.DecimalField(max_digits=9, decimal_places=2)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction_bids")

    def __str__(self):
        return f"{self.bider} bid ${self.bid_price} on {self.auction}"


# define the model of a comment
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    headline = models.CharField(max_length=64)
    message = models.TextField(blank=False)
    cm_date = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction_comments")

    def __str__(self):
        return f"{self.user} comments on {self.auction}"


# define the model of a watchlist
class Watchlist(models.Model):
    auctions = models.ManyToManyField(Auction, related_name="auctions_in_watchlist", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="watchlist")

    def __str__(self):
        return f"{self.user}'s watchlist"

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bid
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

@receiver(post_save, sender=Bid)
def bid_post_save(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'auction_{instance.auction.id}',
            {
                'type': 'auction_message',
                'message': json.dumps({
                    'bid': str(instance.bid_price),  # Convert Decimal to string
                    'user': instance.bider.username
                })
            }
        )


