# Generated by Django 2.2 on 2019-09-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
