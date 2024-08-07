import uuid

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class BaseEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.id}'


class Skill(BaseEntity, MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class TaskType(models.TextChoices):
    TASK = 'task', 'Task'
    REGULAR_TASK = 'regular_task'
    HABIT = 'habit'


class Task(BaseEntity, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    type = models.CharField(max_length=200, choices=TaskType.choices)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Event(BaseEntity):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

