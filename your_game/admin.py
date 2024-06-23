from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Skill


admin.site.register(Skill, MPTTModelAdmin)
