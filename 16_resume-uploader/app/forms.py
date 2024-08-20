from django import forms
from app.models import Resume

GENDER_CHOICES = (
	('Male', 'Male'),
	('Female', 'Female')
)

CITY_CHOICES = (
	('Mumbai','Mumbai'),
	('Bengaluru','Bengaluru'),
	('Hyderabad','Hyderabad'),
	('Chennai','Chennai'),
	('Pune','Pune'),
	('Ahmedabad','Ahmedabad'),
)

class ResumeForm(forms.ModelForm):
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
	job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=CITY_CHOICES, widget=forms.CheckboxSelectMultiple)
	class Meta:
		model = Resume
		fields = '__all__'
		labels = {
			'name': 'Full Name',
			'dob': 'Date of Birth',
			'pin': 'Pin Code',
			'mobile': 'Mobile No.',
			'email': 'Email Id',
			'profile_img': 'Profile Image',
			'file': 'Document'
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
			'locality': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
			'pin': forms.NumberInput(attrs={'class': 'form-control'}),
			'state': forms.Select(attrs={'class': 'form-control'}),
			'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
		}