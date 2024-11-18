from django.db import models
import datetime

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return f"{self.title} | updated on {self.updated_on.strftime("%m/%d/%Y, %H:%M:%S")}"