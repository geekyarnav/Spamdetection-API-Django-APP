# Generated by Django 2.2.13 on 2020-06-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='is_spam',
            field=models.BooleanField(choices=[('True', 'True'), ('False', 'False')], default=False),
        ),
    ]
