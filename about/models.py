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


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"