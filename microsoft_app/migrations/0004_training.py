# Generated by Django 4.0.4 on 2022-04-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microsoft_app', '0003_admin_remove_feedback_private_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training', models.CharField(max_length=1000)),
            ],
        ),
    ]
