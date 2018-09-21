from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import User, BasicInfo, StatusInfo, PersonalInfo, ProfessionalInfo, HabitInfo, UserProfile
# from .utils import (GENDER_CHOICES,
# 						LANGUAGE_CHOICES,
# 						ETHINICITY_CHOICES,
# 						RELIGION_CHOICES,
# 						SIGN_CHOICES,
# 						BODY_TYPE_CHOICES,
# 						SEXUAL_ORIENTATION_CHOICES,
# 						REL_STATUS_CHOICES,
# 						REL_TYPE_CHOICES,
# 						CHILDREN_CHOICES,
# 						PETS_CHOICES,
# 						CAR_CHOICES,
# 						HOME_OWNERSHIP_CHOICES,
# 						PROFESSION_CHOICES,
# 						INDUSTRY_CHOICES,
# 						EDUCATION_CHOICES,
# 						SMOKING_CHOICES,
# 						DRINKING_CHOICES,
# 						DRUG_CHOICES,
# 						DIET_CHOICES,)


class SignUpForm(UserCreationForm):
	date_of_birth = forms.DateField(input_formats=['%b %d, %Y'], widget=forms.TextInput())

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username', 'email', 'gender', 'date_of_birth']
	date_of_birth.widget.attrs.update({'class':'datepicker'})

	def clean_email(self):
		email = self.cleaned_data['email']
		qs = User.objects.filter(email = email.strip())
		if qs.exists():
			raise forms.ValidationError("Email address already exists")
		return email

	def clean_username(self):
		username = super().cleaned_data['username']
		return username.lower().strip()

	def clean_date_of_birth(self):
		born = self.cleaned_data.get("date_of_birth")
		today = date.today()
		age =  today.year - born.year - ((today.month, today.day) < (born.month, born.day))
		if ((age > settings.MIN_AGE) and (age < settings.MAX_AGE)):
			return age
		raise forms.ValidationError('user has to be 18 or above to signup')


	def save(self, request):
		user = super(SignUpForm, self).save(request)
		return user


class UserSimpleForm(forms.ModelForm):
	date_of_birth = forms.DateField(input_formats=['%b %d, %Y'], widget=forms.TextInput(attrs={'class':'datepicker'}))
	class Meta:
		model = User
		fields = ['date_of_birth', 'gender']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['about', 'city']
		widgets = {
			'about': forms.Textarea(attrs={'data-length':'160'}),
		}
class BasicForm(forms.ModelForm):
	class Meta:
		model = BasicInfo
		fields = ['ethnicity', 'religion', 'sign', 'body_type']
		# widgets = {
		# 	'ethnicity': forms.Select(choices=ETHINICITY_CHOICES),
		# 	'religion': forms.Select(choices=RELIGION_CHOICES),
		# 	'sign': forms.Select(choices=SIGN_CHOICES),
		# 	'body_type': forms.Select(choices=BODY_TYPE_CHOICES),
		# }



class StatusForm(forms.ModelForm):
	class Meta:
		model = StatusInfo
		fields = ['sexual_orientation', 'relationship_type', 'relationship_status', ]
		# widgets = {
		# 	'sexual_orientation': forms.Select(choices=SEXUAL_ORIENTATION_CHOICES),
		# 	'relationship_type': forms.Select(choices=REL_STATUS_CHOICES),
		# 	'relationship_status': forms.Select(choices=REL_TYPE_CHOICES),
		# }
class PersonalForm(forms.ModelForm):
	class Meta:
		model = PersonalInfo
		fields = ['children','home_ownership','pets','car']
		# widgets = {
		# 	'children': forms.Select(choices=CHILDREN_CHOICES),
		# 	'home_ownership': forms.Select(choices=PETS_CHOICES),
		# 	'pets': forms.Select(choices=HOME_OWNERSHIP_CHOICES),
		# }  


class ProfessionalForm(forms.ModelForm):
	class Meta:
		model = ProfessionalInfo
		fields = ['profession', 'industry', 'education']
		# widgets = {

		# }

class HabitForm(forms.ModelForm):
	class Meta:
		model = HabitInfo
		fields = ['smoking', 'drinking', 'drug', 'diet']
		# widgets = {

		# }

class PhotoForm(forms.Form):
	photo = forms.ImageField()
	photo.widget.attrs.update({'accept':'image/*'})