# from django import forms
# from django.core import validators
# from .models import Student


# ========================form api==========================
# class StudentRegistration(forms.Form):
    # age = forms.IntegerField(required=False)
    # lname = forms.CharField(label='Last name')
    # error_css_class = 'error'
    # required_css_class = 'required'
    # name = forms.CharField(min_length=5, max_length=20, error_messages={'required':'Enter your name'})
    # email = forms.EmailField(error_messages={'required':'Enter your email'})
    # stud_id = forms.IntegerField(error_messages={'required':'Enter your Id'}, label='Student ID')
    # password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter your password'}, min_length=4)
    # rpassword = forms.CharField(error_messages={'required':'Retype your password'}, min_length=4, label='Confirm password')
    
    # def clean(self):
    #     cleaned_data = super(StudentRegistration, self).clean()
    #     # print(cleaned_data)
    #     valpwd = self.cleaned_data['password']
    #     valrpwd = self.cleaned_data['rpassword']

    #     if valpwd != valrpwd:
    #         raise forms.ValidationError('Password does not matched!')
    
    # password = forms.CharField(label='Department password', widget=forms.PasswordInput)
    # from_cs = forms.CharField(widget=forms.CheckboxInput,label='Belong to CS Department')
    # room_no =  forms.IntegerField(disabled=True)
    # resume = forms.CharField(widget=forms.FileInput,label='Updated resume')
    # id = forms.CharField(widget=forms.TextInput(attrs={'id': 'unique_id'}),label='Id')
    # key = forms.CharField(widget=forms.HiddenInput())




# =============================model form======================================

# class StudentRegistration(forms.ModelForm):
#     class Meta:
#         model = Student
#         # fields = ['name', 'email']
#         fields = '__all__'
#         # exclude = ['password'] #except this
#         labels = {'name':'Student name', 'email':'Student email', 'password':'Your password'}
#         error_messages = {
#             'name': {'required':'Enter your fullname'}, 
#             'email':{'required':'Enter your org email'},
#             'password':{'required':'Enter your password'},
#         }
#         widgets = {
#             'name':forms.TextInput(attrs={'placeholder':'Your name'}),
#             'email':forms.TextInput(attrs={'placeholder':'Your email'}),
#             'password':forms.PasswordInput(attrs={'placeholder':'Your password'}),
#         }

# class StudentLogin(StudentRegistration):
#     class Meta(StudentRegistration.Meta):
#         fields = ['name', 'password']



# =====================================user creation form============================
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}


class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email': 'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}