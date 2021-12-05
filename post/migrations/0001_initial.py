# Generated by Django 3.2.6 on 2021-12-04 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('viewed', models.IntegerField(null=True)),
                ('latest', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_txt', models.CharField(max_length=250, null=True)),
                ('reply_time', models.DateTimeField(auto_now=True)),
                ('replyCount', models.IntegerField(null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.postcategory'),
        ),
    ]
