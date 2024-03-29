# Generated by Django 5.0.1 on 2024-01-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='Enter your full name', max_length=100)),
                ('email', models.EmailField(help_text='Enter your email address', max_length=254)),
                ('phone_number', models.CharField(help_text='Enter your phone number', max_length=20)),
                ('comments', models.TextField(help_text='Enter any additional comments')),
            ],
        ),
    ]
