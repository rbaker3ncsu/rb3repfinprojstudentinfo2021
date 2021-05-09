from django.shortcuts import render
from django.http import HttpResponse
from stinfo.models import StudentDetails, CourseDetails, CommentData, StudentEnrollment
from django.core.paginator import Paginator
#a decorator adds functionality on top of an existing function or view
from django.contrib.auth.decorators import login_required

from django.db import connection

# Create your views here.

#    return HttpResponse('Student Details Page')

@login_required
def home(request):
#	if request.session['username']:
#		uname = request.session['username']

	request.session['username'] = request.user.username

	studentData = StudentDetails.objects.all()
	gpaAverage = 0;
	for student in studentData:
		gpaAverage += student.gpa
	gpaAverage = gpaAverage/StudentDetails.objects.all().count()

	studentCount = StudentDetails.objects.all().count()
	courseCount = CourseDetails.objects.all().count()
	freshCount = StudentDetails.objects.filter(year = "Freshman").count()
	sophCount = StudentDetails.objects.filter(year = "Sophomore").count()
	jrCount = StudentDetails.objects.filter(year = "Junior").count()
	seniorCount = StudentDetails.objects.filter(year = "Senior").count()
	context = {	'stCount':studentCount,
				'crCount':courseCount,
				'stData':studentData,
				'freshCount':freshCount,
				'sophCount':sophCount,
				'jrCount':jrCount,
				'seniorCount':seniorCount,
				'gpaAverage':gpaAverage}
	return render(request,'stinfo/home.html', context)

@login_required
def studentdetails(request):
    studentData = StudentDetails.objects.filter()
    #pagination
    paginatorObj = Paginator(studentData, 10)
    page = request.GET.get('page')
    stMiniData = paginatorObj.get_page(page)
    #dictionary that holds paginated data
    context = {'stdata':stMiniData}
    return render(request,'stinfo/studentdetails.html', context)

@login_required
def coursedetails(request):
    #filters data
    courseData = CourseDetails.objects.filter()
    #paginate data
    paginatorObj = Paginator(courseData, 10)
    page = request.GET.get('page')
    crMiniData = paginatorObj.get_page(page)
    #dictionary that holds paginated data
    context = {'crdata':crMiniData}
    return render(request,'stinfo/coursedetails.html',context)

@login_required
def enrollment(request):
    return HttpResponse("Enrollment Page")

        #every row of data
    #    courseData = CourseDetails.objects.all()
        #filtered data
    #    courseData = CourseDetails.objects.filter()
    #    courseData = CourseDetails.objects.filter(department = 'economics')

#there is a way to retrieve data from a db differently:
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row))
        for row in cursor.fetchall()
    ]

#retrieving coursedetails data from mysql
#def coursedetails(request):
#    department = 'economics'
#    cursorobj = connection.cursor()
#    cursorobj.execute("SELECT * FROM stinfo_coursedetails WHERE department = %s",[department])
#    courseData = dictfetchall(cursorobj)
#    context = {'crdata':courseData}
#    return render(request, 'stinfo/coursedetails.html', context)

@login_required
def commentpage(request):
	#session variable
	request.session['username'] = request.user.username
#	request.session['favStudent'] = 'Rick'
	return render(request,'stinfo/comment.html')

@login_required
def savedata(request):
	#test:
	#print("7")
	if('email' and 'comment' in request.GET):
		emiId = request.GET.get('email')
		comData = request.GET.get('comment')
		dataObj = CommentData(emailId = emiId, comment = comData)
		dataObj.save()
	return HttpResponse("success 2")

@login_required
def studentenrollment(request):
	studentData = StudentDetails.objects.all()

	courseData = CourseDetails.objects.order_by('title')
	ccdata = CourseDetails.objects.all()

	if('stuid' in request.session):
		studentEnrollment = StudentEnrollment.objects.filter(studentId = request.session['stuid'])
	else:
		studentEnrollment = StudentEnrollment.objects.filter()

	paginatorObj = Paginator(studentEnrollment, 10)
	page = request.GET.get('page')
	steMiniData = paginatorObj.get_page(page)

	context = {'stdata':studentData,'crdata':courseData,'stenroll':steMiniData,'ccdata':ccdata,'stedata':steMiniData}
	return render(request, 'stinfo/studentenrollment.html', context)

@login_required
def saveenrollment(request):
	flag = False
	flagBoth = False
	if('studentId2' in request.GET and 'courseTitle2' not in request.GET):
		request.session['stuid'] = request.GET.get('studentId2')

	if('courseTitle2' in request.GET and request.session['stuid'] != ""):
		flagBoth = True
		stId = request.session['stuid']
		cTitle = request.GET.get('courseTitle2')
		allrecords = StudentEnrollment.objects.all()
		dataObj = StudentEnrollment(studentId = stId, courseTitle = cTitle)
		iflogic = StudentEnrollment.objects.filter(studentId = stId)
		print(iflogic)
		if(iflogic.count() < 3):
			for key in iflogic.values():
				if( cTitle == key['courseTitle'] ):
					HttpResponse("Error: duplicate record found.")
					flag = True
		else:
			HttpResponse("Error: only 3 courses are allowed for each student.")
			flag = True
	if(flag == False and flagBoth == True):
		dataObj.save()

	return HttpResponse('success 2')
