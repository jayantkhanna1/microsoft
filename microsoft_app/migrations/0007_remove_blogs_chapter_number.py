# Generated by Django 4.0.4 on 2022-04-18 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microsoft_app', '0006_blogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='chapter_number',
        ),
    ]