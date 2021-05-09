from django.contrib import admin
from stinfo.models import CourseDetails, StudentDetails, StudentEnrollment, CommentData

# Register your models here.

admin.site.register(StudentDetails)
admin.site.register(CourseDetails)
admin.site.register(StudentEnrollment)
admin.site.register(CommentData)
