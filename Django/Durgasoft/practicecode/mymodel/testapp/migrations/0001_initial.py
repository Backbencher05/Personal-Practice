# Generated by Django 3.2.5 on 2021-09-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('name', models.CharField(max_length=52)),
                ('esal', models.IntegerField()),
                ('eaddr', models.CharField(max_length=85)),
            ],
        ),
    ]