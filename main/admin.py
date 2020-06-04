from django.contrib import admin

# Register your models here.

from .models import User
from .models import Activity_peroid


admin.site.register(User)
admin.site.register(Activity_peroid)