import datetime

from django.db import models
from django.utils import timezone

# Models showns as classes in the database
# Each model has class variables that represent database fields will be shown as columns


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # Defines the string representation of the object
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    # This foreign key says each choice is related to a single question 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text