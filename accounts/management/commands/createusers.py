from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

def createUser(name, password):
    if not User.objects.filter(username=name).exists():
        User.objects.create_superuser(name, "", password)
        print("  ==  Added " + username + "  ==  ")


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Insert admins here
        users = {}
        users['admin'] = "admin"
        users['emilte'] = "django123"

        for (username, password) in users.items():
            createUser(username, password)
