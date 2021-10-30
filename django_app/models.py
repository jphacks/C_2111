from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth import get_user_model
import uuid


class Questionnaire(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True, null=True, help_text='作成日')
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class DailyReport(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    text = models.TextField('日報', max_length=200, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=True, help_text='作成日')
    score = models.FloatField(blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text
