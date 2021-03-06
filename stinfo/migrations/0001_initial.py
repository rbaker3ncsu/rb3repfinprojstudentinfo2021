# Generated by Django 3.2 on 2021-05-09 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailId', models.CharField(max_length=500)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.IntegerField()),
                ('title', models.CharField(max_length=500)),
                ('cName', models.CharField(max_length=500)),
                ('selectionCode', models.IntegerField()),
                ('department', models.CharField(max_length=500)),
                ('instructorName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.IntegerField()),
                ('first', models.CharField(max_length=500)),
                ('last', models.CharField(max_length=500)),
                ('major', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('gpa', models.FloatField(verbose_name='0.0')),
            ],
        ),
        migrations.CreateModel(
            name='StudentEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.IntegerField()),
                ('courseTitle', models.CharField(max_length=500)),
            ],
        ),
    ]
