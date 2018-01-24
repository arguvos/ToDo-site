from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)	
    name = models.TextField(max_length=1000)
    done = models.BooleanField(default=False)
    dateCreated = models.DateTimeField('Date created', auto_now_add=True)
	
    def __str__(self):
        if self.done:
            return "%s (done)" % self.name
        else:
            return self.name