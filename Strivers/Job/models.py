from django.db import models
from django.db.models import Model,CharField



class SearchDetails(models.Model):
    search=CharField(max_length=256)
    username = CharField(max_length=25)
    siteurl = CharField(max_length=256)
    # email = CharField(max_length=25)

    def __str__(self):
        return self.username
