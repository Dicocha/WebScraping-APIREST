from django.db import models

# Create your models here.

class Vault(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    purpose = models.TextField()
    additional_details = models.TextField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.name