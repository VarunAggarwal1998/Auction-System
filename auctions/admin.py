from django.contrib import admin

from auctions.models import Auction, Bid, Comment, Watchlist, Category, User

# Register your models here.
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlist)
admin.site.register(Category)
admin.site.register(User)