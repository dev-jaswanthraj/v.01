# Generated by Django 3.1.1 on 2020-10-01 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=20000)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'ordering': ['-timestamp', '-update'],
            },
        ),
    ]
