from django.core.management.base import BaseCommand
from django.utils import timezone
from auctions.models import Auction

class Command(BaseCommand):
    help = 'Close auctions that have passed their end time'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_auctions = Auction.objects.filter(end_time__lte=now, closed=False)
        for auction in expired_auctions:
            auction.closed = True
            auction.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully closed auction: {auction.title}'))
