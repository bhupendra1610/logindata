# Generated by Django 3.2.14 on 2022-08-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('address', models.TextField(max_length=100)),
                ('phoneno', models.IntegerField()),
                ('password', models.TextField(max_length=34)),
            ],
        ),
    ]
