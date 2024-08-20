from django.shortcuts import render, redirect
from app.forms import ResumeForm
from app.models import Resume
from django.views import View

class Home(View):
	def get(self, request):
		form = ResumeForm()
		candidates = Resume.objects.all()
		return render(request, 'app/home.html', {'candidates':candidates,'form':form})

	def post(self, request):
		form = ResumeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('/')


class Candidate(View):
	def get(self, request, pk):
		candidate = Resume.objects.get(id=pk)
		return render(request, 'app/candidate.html', {'candidate':candidate})