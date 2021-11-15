from django.db import models


class ContactForm(models.Model):
    address = models.TextField()
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    date = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.message
