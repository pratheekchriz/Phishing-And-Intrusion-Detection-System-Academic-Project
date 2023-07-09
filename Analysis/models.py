from django.db import models

# Create your models here.

class CapturedPacket(models.Model):
    packet_data = models.BinaryField()
    prediction = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


