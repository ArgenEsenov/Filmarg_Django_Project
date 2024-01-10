from django.db import models

from django.db import models


class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return self.email
