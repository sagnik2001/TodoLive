from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(
        User,on_delete=models.CASCADE,null=True,blank=True
    )  # user log in authentication
    title=models.CharField(max_length=200) # title of todos 
    description=models.TextField(null=True,blank=True) # description of todos
    complete=models.BooleanField(default=False) # complete of todo tasks
    created=models.DateTimeField(auto_now_add=True) # creation date time stap


    def __str__(self) :
        return self.title


    class Meta:
        ordering=['complete']    # peck order
