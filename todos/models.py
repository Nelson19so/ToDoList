from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# todo model
class TodoItems(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
  todo = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  day = models.CharField(max_length=255)
  date_created = models.DateTimeField(auto_now_add=True)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.todo
  
  class Meta:
    ordering = ['-date_created']