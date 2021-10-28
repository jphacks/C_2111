from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    person_id = models.IntegerField(default=0)
    data1 = models.TextField('日報', max_length=200, blank=False)
    data2 = models.TextField('日報', max_length=200, blank=False)
    data3 = models.TextField('日報', max_length=200, blank=False)
    data4 = models.TextField('日報', max_length=200, blank=False)
    data5 = models.TextField('日報', max_length=200, blank=False)
    data6 = models.TextField('日報', max_length=200, blank=False)
    data7 = models.TextField('日報', max_length=200, blank=False)
    data8 = models.TextField('日報', max_length=200, blank=False)
    data9 = models.TextField('日報', max_length=200, blank=False)
    data10 = models.TextField('日報', max_length=200, blank=False)
    data11 = models.TextField('日報', max_length=200, blank=False)
    data12 = models.TextField('日報', max_length=200, blank=False)
    data13 = models.TextField('日報', max_length=200, blank=True)
    data14 = models.TextField('日報', max_length=200, blank=True)
    data15 = models.TextField('日報', max_length=200, blank=True)
    data16 = models.TextField('日報', max_length=200, blank=True)
    data17 = models.TextField('日報', max_length=200, blank=True)
    data18 = models.TextField('日報', max_length=200, blank=True)
    data19 = models.TextField('日報', max_length=200, blank=True)
    data20 = models.TextField('日報', max_length=200, blank=True)

    def __str__(self):
        return self.name