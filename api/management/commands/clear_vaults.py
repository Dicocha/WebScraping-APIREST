# myapp/management/commands/clear_vaults.py

from django.core.management.base import BaseCommand
from api.models import Vault
from django.db import connection

class Command(BaseCommand):
    help = 'Deletes all data from the Vault table and resets the primary key sequence.'

    def handle(self, *args, **kwargs):
        # Delete all data
        Vault.objects.all().delete()

        # Reset the primary key sequence
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='myapp_vault';")

        self.stdout.write(self.style.SUCCESS('Successfully deleted all Vault records and reset the primary key sequence.'))
