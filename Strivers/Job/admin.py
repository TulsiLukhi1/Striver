from django.contrib import admin
from .models import SearchDetails,UpdateDetails,JobDetails,JobCategory

admin.site.register(SearchDetails)
admin.site.register(UpdateDetails)
admin.site.register(JobDetails)
admin.site.register(JobCategory)

