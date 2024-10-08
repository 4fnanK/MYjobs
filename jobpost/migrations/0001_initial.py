# Generated by Django 3.2.21 on 2023-12-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('jobpost_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_post', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'job_post',
                'managed': False,
            },
        ),
    ]
