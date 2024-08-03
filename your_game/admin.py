from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Skill, Task, Event


admin.site.register(Skill, MPTTModelAdmin)
admin.site.register(Task, MPTTModelAdmin)
admin.site.register(Event)
