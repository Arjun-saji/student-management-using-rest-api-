from .models import *
from  rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model =Student
		fields = ['name', 'email', 'enroll_date']


class AttendanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=Attendance
		fields = ['id', 'status', 'attendance_date', 'student']


	def get_student_name(self, obj):
		return obj.student.name