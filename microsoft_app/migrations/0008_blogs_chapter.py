# Generated by Django 4.0.4 on 2022-04-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microsoft_app', '0007_remove_blogs_chapter_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='chapter',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
