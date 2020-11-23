from django.contrib import admin
from . models import Contact,Feedback,Postblog,Appointment,Medicine
# Register your models here.
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Postblog)
admin.site.register(Appointment)
admin.site.register(Medicine)