# Generated by Django 4.2 on 2023-04-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.CharField(default='Error in username', max_length=255),
        ),
    ]