from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


class Command(BaseCommand):
    help = 'Create admin & guest user'

    def handle(self, *args, **options):
        def create_user(name, password=None):
            user = User.objects.create_user(name,
                                            password=os.urandom(1024) if password is None else password)
            user.is_superuser = False
            user.is_staff = False
            user.save()

        create_user("admin")
        create_user("guest", "guest")