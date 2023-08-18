from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import (
    datetime,
    timedelta,
)
import pytz


class Command(BaseCommand):
    help = "remove all expired otp codes"

    def handle(self, *args, **options):
        expired_time = datetime.now().replace(tzinfo=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
        OtpCode.objects.filter(created_at__lt=expired_time).delete()

        self.stdout.write(self.style.SUCCESS("successfully remove all otp codes"))
