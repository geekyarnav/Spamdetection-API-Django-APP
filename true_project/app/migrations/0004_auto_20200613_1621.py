# Generated by Django 2.2.13 on 2020-06-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200613_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='is_spam',
            field=models.BooleanField(default=True),
        ),
    ]
