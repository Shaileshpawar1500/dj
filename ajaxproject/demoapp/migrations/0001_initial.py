# Generated by Django 3.0.2 on 2020-02-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
