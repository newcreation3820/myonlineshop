# Generated by Django 2.2 on 2020-09-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200904_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='inactive', max_length=100),
        ),
    ]
