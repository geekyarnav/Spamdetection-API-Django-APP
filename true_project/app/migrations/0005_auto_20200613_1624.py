# Generated by Django 2.2.13 on 2020-06-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200613_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_info',
            old_name='phone_number',
            new_name='contact_phone_number',
        ),
        migrations.AlterField(
            model_name='contact_info',
            name='contact_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='is_spam',
            field=models.BooleanField(default=False),
        ),
    ]
