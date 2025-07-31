from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from violations.models import User,Violation
from violations.models import StudentInfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os 

@api_view(['POST'])
def login(request):
	user = User.objects.filter(username=request.data.get('username'), password=request.data.get('password'))
	if not user.exists():
		return HttpResponse({"error": "User not found"}, status=404)
	return JsonResponse({"message": "Login successful", "user": {"username": user[0].username, "id": user[0].id}})
	
	return Response()

@api_view(['GET'])
def getViolations(request):
	violations = Violation.objects.all()
	return JsonResponse({"violations": list(violations.values())})

api_view(['GET'])
def getStudentDetails(request, student_id):
	try:
		student = StudentInfo.objects.get(student_id=student_id)
	except StudentInfo.DoesNotExist:
		return HttpResponse({"error": "Student not found"}, status=404)

@api_view(['POST'])
def addViolation(request, student_id):
	student_id = request.data.get('student_id')
	violation_type = request.data.get('violation_type')
	if not student_id or not violation_type:
		return HttpResponse({"error": "Invalid Violation"}, status=400)
	try:
		student = StudentInfo.objects.get(student_id=student_id)
	except StudentInfo.DoesNotExist:
		return HttpResponse({"error": "Student not found"}, status=404)
	violation = Violation.objects.create(student=student, violation_type=violation_type)
	violation.save()
	return JsonResponse({"message": "Violation added successfully", "violation": {"id": violation.id, "student_id": student.student_id, "violation_type": violation.violation_type}})

@api_view(['PUT'])
def updateViolation(request, student_id):
    try:
        violation = Violation.objects.get(student_id=student_id)  # or student_id__id=student_id
        violation_type = request.data.get('violation_type')

        if not violation_type:
            return JsonResponse({"error": "Missing violation_type"}, status=400)

        violation.violation_type = violation_type
        violation.save()
        return JsonResponse({"message": "Violation updated successfully"}, status=200)

    except Violation.DoesNotExist:
        return JsonResponse({"error": "Violation not found for this student"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(['POST'])
def getUserDetails(request):
	user_id = request.data.get('user_id')
	if not user_id:
		return HttpResponse({"error": "User ID is required"}, status=400)
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		return HttpResponse({"error": "User not found"}, status=404)
	return JsonResponse({"user": {"username": user.username, "id": user.id}})

@api_view(['POST'])
def addUser(request):
	username = request.data.get('username')
	password = request.data.get('password')
	if not username or not password:
		return HttpResponse({"error": "Username and password are required"}, status=400)
	if User.objects.filter(username=username).exists():
		return HttpResponse({"error": "Username already exists"}, status=400)
	try:
		user = User.objects.create(username=username, password=password)
		user.save()
		return JsonResponse({"message": "User added successfully", "user": {"username": user.username, "id": user.id}})
	except Exception as e:
		return HttpResponse({"response": str(e)}, status=500)





	