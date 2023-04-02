from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PRIORITY_CHOICES=(
    ('LOW', 'LOW'),
    ('MEDIUM', 'MEDIUM'),
    ('HIGHT', 'HIGHT'),
)


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    begin = models.DateTimeField()
    end = models.DateField()
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.label