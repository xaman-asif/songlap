# Generated by Django 3.2.6 on 2021-12-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20211206_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]