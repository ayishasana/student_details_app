from django.contrib import admin

from new_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.admregister)
admin.site.register(models.Mark)




