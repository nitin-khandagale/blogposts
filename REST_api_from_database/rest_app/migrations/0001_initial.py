# Generated by Django 3.0.1 on 2020-06-08 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeApi',
            fields=[
                ('serial_number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'home_api',
                'managed': False,
            },
        ),
    ]
