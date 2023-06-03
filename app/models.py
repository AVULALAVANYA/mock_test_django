from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    questions=models.TextField()
    def __str__(self): 
        return self.questions
class Answer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    questions=models.ForeignKey(Question,on_delete=models.CASCADE)
    answers=models.TextField()
    def __str__(self):
        return self.questions