from django.db import models
from model_utils import FieldTracker
from asgiref.sync import async_to_sync
#from .notifications import update_post


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    tracker = FieldTracker(fields=("title",))


    def __str__(self):
    	return self.title

"""

    def save(self, *args, **kwargs):
        ret = super().save(*args, **kwargs)
        has_changed = self.tracker.has_changed("title")
        if has_changed:
        	pass
            #async_to_sync(update_post)(self)
        return ret
"""

