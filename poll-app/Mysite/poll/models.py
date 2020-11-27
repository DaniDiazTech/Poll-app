from django.db import models

# Create your models here.
# See /NOTES_files/Models.md

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(("Date Published"))

    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    n_votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
    