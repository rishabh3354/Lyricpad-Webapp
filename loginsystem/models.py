from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=100,)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=500)

    class Meta:

        db_table = 'contact_us'






