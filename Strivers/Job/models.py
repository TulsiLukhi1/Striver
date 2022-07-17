from django.db import models
from django.db.models import Model,CharField,IntegerField



class SearchDetails(models.Model):
    search=CharField(max_length=256)
    username = CharField(max_length=25)
    siteurl = CharField(max_length=256)
    # email = CharField(max_length=25)

    def __str__(self):
        return self.username




class JobDetails(models.Model):
    # searchjob = CharField(max_length=256)
    username = CharField(max_length=25)
    jobdetailurl= CharField(max_length=256)
    jobtitle = CharField(max_length=100)
    location=CharField(max_length=100)
    company_name=CharField(max_length=256)

    def __str__(self):
        return self.username



class UpdateDetails(models.Model):
    siteurl=CharField(max_length=256)
    search=CharField(max_length=256)
    total_div=IntegerField()

    def __str__(self):
        return self.search

class JobCategory(models.Model):
    category=CharField(max_length=256)
    siteurl=CharField(max_length=256)
    def __str__(self):
        return self.siteurl


        