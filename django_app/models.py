from django.db import models
from django.db.models.fields import DateTimeField


class DailyReport(models.Model):
    organization_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    person_name = models.CharField(max_length=100)
    text = models.TextField('日報', max_length=200, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=True, help_text='作成日')

    person_id = models.IntegerField(unique=True, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.person_name
