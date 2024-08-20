from django.contrib import admin
from app.models import Resume

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'name', 'dob', 
		'gender', 'locality', 'city', 
		'pin', 'state', 'mobile',
		'job_city', 'profile_img', 'file'
	]
