# Generated by Django 3.2.8 on 2021-10-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('person_id', models.IntegerField(default=0)),
                ('data1', models.TextField(max_length=200, verbose_name='日報')),
                ('data2', models.TextField(max_length=200, verbose_name='日報')),
                ('data3', models.TextField(max_length=200, verbose_name='日報')),
                ('data4', models.TextField(max_length=200, verbose_name='日報')),
                ('data5', models.TextField(max_length=200, verbose_name='日報')),
                ('data6', models.TextField(max_length=200, verbose_name='日報')),
                ('data7', models.TextField(max_length=200, verbose_name='日報')),
                ('data8', models.TextField(max_length=200, verbose_name='日報')),
                ('data9', models.TextField(max_length=200, verbose_name='日報')),
                ('data10', models.TextField(max_length=200, verbose_name='日報')),
                ('data11', models.TextField(max_length=200, verbose_name='日報')),
                ('data12', models.TextField(max_length=200, verbose_name='日報')),
                ('data13', models.TextField(blank=True, max_length=200, verbose_name='日報')),
                ('data14', models.TextField(blank=True, max_length=200, verbose_name='日報')),
                ('data15', models.TextField(blank=True, max_length=200, verbose_name='日報')),
                ('data16', models.TextField(blank=True, max_length=200, verbose_name='日報')),
                ('data17', models.TextField(blank=True, max_length=200, verbose_name='日報')),
                ('data18', models.TextField(blank=True, max_length=200, verbose_name='日報')),
                ('data19', models.TextField(blank=True, max_length=200, verbose_name='日報')),
                ('data20', models.TextField(blank=True, max_length=200, verbose_name='日報')),
            ],
        ),
    ]
