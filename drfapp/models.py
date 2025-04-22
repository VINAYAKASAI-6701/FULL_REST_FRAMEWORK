from django.db import models

# Create your models here.
#serilization means just converting python obkects(like models) into JSON data so they can be used to the frontend or api clients

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    description=models.TextField()
    date_enrolled=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name