from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItem(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  object_id = models.PositiveSmallIntegerField()
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  content_object = GenericForeignKey('content_type', 'object_id')
