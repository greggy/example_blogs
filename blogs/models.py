from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    visible = models.BooleanField(default=False)
    created_on = models.DateTimeField('datetime')

    
    def was_published_recently(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title
    
