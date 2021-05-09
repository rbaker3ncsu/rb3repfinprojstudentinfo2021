from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    # can say primary_key = true to create primary key
    studentId = models.IntegerField()
    first = models.CharField(max_length = 500)
    last = models.CharField(max_length = 500)
    major = models.CharField(max_length = 100)
    year = models.CharField(max_length = 100)
    gpa = models.FloatField(format(0.00))

class CourseDetails(models.Model):
    # can say primary_key = true to create primary key
    courseId = models.IntegerField()
    title = models.CharField(max_length = 500)
    cName = models.CharField(max_length = 500)
    selectionCode = models.IntegerField()
    department = models.CharField(max_length = 500)
    instructorName = models.CharField(max_length = 500)

class CommentData(models.Model):
	emailId = models.CharField(max_length = 500)
	comment = models.TextField()

def CreateSessionVariables():
	request.session['global'] = 'global value'
	#call with something like this:
#	user_logged_in.connect(CreateSessionVariables)

class StudentEnrollment(models.Model):
	studentId = models.IntegerField()
	courseTitle = models.CharField(max_length = 500)






#how to roll back changes:

# go to CMD, type: python manage.py showmigrations nameOfApp
#for us, nameOfApp = stinfo
#this shows us our migrations created
#rollback migration:
#in CMD: python manage.py migrate nameOfApp 001_initial
#this rolls back until the 001_initial migration, thereby erasing all migrations after it.
#we can see if this works by going into mySQL and searching for the migrated table
#go to app directory: studentinfoapp/stinfo/migrations/
#delete 0002 migration file (all files after the rollback)
#can now add attributes/column names in models.py

#add the changes back by going to CreateModel

#in CMD: python manage.py makemigrations
#in CMD: python manage.py migrate
