# Generated by Django 2.1 on 2020-02-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.IntegerField()),
                ('f', models.FloatField()),
                ('nullable', models.CharField(max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
