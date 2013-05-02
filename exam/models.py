from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200)
    level = models.IntegerField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.question

class UserDetail(models.Model):
    name = models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    grade = models.IntegerField()
    feedback = models.CharField(max_length=300)
    
    def __unicode__(self):
        return self.name
