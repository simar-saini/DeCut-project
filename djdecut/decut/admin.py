from django.contrib import admin
from .models import signup_model,SessionToken
# Register your models here.
admin.site.register(signup_model)
admin.site.register(SessionToken)