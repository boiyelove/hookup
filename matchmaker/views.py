import random
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.middleware.csrf import get_token
from django.views.generic.edit import FormView, UpdateView
from django.template.loader import render_to_string
from django.http import Http404, JsonResponse
from .forms import BasicForm, BasicForm, StatusForm, PersonalForm, ProfessionalForm, HabitForm, UserSimpleForm, UserProfileForm, PhotoForm
from .models import Interest, User, Membership


# Create your views here.


# class AjaxFormResponseMixin:
# 	def get_context_data(self, *args, **kwargs):	
# 		context = super().get_context_data(**kwargs)
# 		if self.request.is_ajax():	
# 			context.update({'pk':pk,
# 				'form_action': self.request.path,
# 				})
# 		return context

# 	def form_valid(form):
# 		response = super().form.valid(form)
# 		if self.request.is_ajax():
# 			return HttpResponse(response)
# 		else:
# 			return response

# 	def form_invalid(form):
# 		response = super().form.valid(form)
# 		# print(form.errors)
# 		if self.request.is_ajax():
# 			response.status_code = 422
# 			return super().render_to_response(response)
# 		else:
# 			return response

# class CheckUser(UserPassesTestMixin):
# 	allowed_membership = []

# 	def test_func(self):
# 		mbership = Membership.objects.get(user = self.request.user)
# 		if mbership.membership in self.allowed_membership:
# 			return True
# 		return False

# class AdminPages(CheckUser):
# 	allowed_membership = ['admin', 'council']

# class CouncilPages(CheckUser):
# 	allowed_membership = ['council']


# class MemberContext:
# 	def get_context_data(self, *args, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		pk = self.kwargs.get('pk', '')
# 		context.update({'pk':pk,
# 			'form_action':reverse_lazy('add-achievement', kwargs={'pk': pk})
# 			})
# 		return context


# class LoginView(SuccessMessageMixin, LoginView):
# 	success_message = "You were successfully logged in"
# 	def get_success_url(self):
# 		user = self.request.user
# 		url = reverse_lazy('list-achievements')
# 		if user.membership.is_admin() or user.membership.is_council():
# 			url = reverse_lazy('list-members')
# 		else:
# 			Profile.objects.get(user = self.request.user)
# 			if self.request.user.profile.force_password_change:
# 				url = reverse_lazy('password_change')
# 		return url



class DiscoveryTemplateView(TemplateView):
	template_name = 'matchmaker/discovery.html'

class UserBaseListView(LoginRequiredMixin, ListView):
	template_name = 'matchmaker/user_grid.html'
	context_object_name = 'user_list'
	paginate_by = 30

	def get_queryset(self):
		# print(self.request.user.id)
		# print(User.objects.all().values_list('id', flat=True))
		# return User.objects.exclude(id__exact = self.request.user.id)
		return self.request.user.get_matches()

class UserHomeView(UserBaseListView):
	pass


class UserProfileView(TemplateView):
	template_name = 'matchmaker/profile.html'

	def get_context_data(self, **kwargs):
		username = self.kwargs.get('username', None)
		user = self.request.user
		if username:
			user = get_object_or_404(User, username=username)
			user.profile.views += 1
			if self.request.user not in user.profile.visitors.all():
				user.profile.visitors.add(self.request.user)

		if self.request.user.is_authenticated and (self.request.user.username != user.username):
			user.profile.visitors.add(self.request.user)
		kwargs = super().get_context_data()
		kwargs['user'] = user
		if self.request.user.is_authenticated and (self.request.user.username == user.username):
			user.profile.visitors.add(self.request.user)
			kwargs['basicform'] = BasicForm(instance=user.basicinfo)
			kwargs['statusform'] = StatusForm(instance=user.statusinfo)
			kwargs['personalform'] = PersonalForm(instance=user.personalinfo)
			kwargs['professionalform'] = ProfessionalForm(instance=user.professionalinfo)
			kwargs['habitform'] = HabitForm(instance=user.habitinfo)
			kwargs['userform'] = UserSimpleForm(instance=user)
			kwargs['profileform'] = UserProfileForm(instance=user.profile)
		q = self.request.GET.get('q')
		if q == 'overview':
			self.template_name = 'matchmaker/ajax/overview.html'
		elif q == 'photo':
			self.template_name = 'matchmaker/ajax/photo.html'
		elif q == 'interests':
			self.template_name = 'matchmaker/ajax/interest.html'
		elif q == 'information':
			self.template_name = 'matchmaker/ajax/information.html'
		elif q == 'photoupload':
			kwargs['form'] = PhotoForm()
			self.template_name = 'matchmaker/ajax/photouploadform.html'
		return kwargs

	def post(self, request, *args, **kwargs):
		# if interest in request.user.profile.interests.all():
		# 	request.user.profile.interests.remove(interest)
		# 	request.user.profile.interests.add(interest)
		# 	basicform = BasicForm(instance=request.user.basicinfo)
		# 	statusform = StatusForm(instance=request.user.statusinfo)
		# 	personalform = PersonalForm(instance=request.user.personalinfo)
		# 	professionalform = ProfessionalForm(instance=request.user.professionalinfo)
		# 	habitform = HabitForm(instance=request.user.habitinfo)
		
		# Like User
		# Update Profile
		
		# Add To Contacts
		# Remove From Contact
		
		# Like User Photo
		# Unlike user photo


		# Add to interests
		# Remove from interests
		user = self.request.user
		submit = request.POST.get('submit', None)
		context = {}
		message = "Invalid information, please check form"
		if submit == "basicinfo":
			form = BasicForm(request.POST, instance=user.basicinfo)
			self.template_name = 'matchmaker/ajax/basicinfoform.html'
			if form.is_valid:
				form.save()
				message = 'Basic Information Updated'
			kwargs['basicform'] = form
		elif submit == "statusinfo":
			form = StatusForm(request.POST, instance=user.statusinfo)
			self.template_name = 'matchmaker/ajax/statusinfoform.html'
			if form.is_valid:
				form.save()
				message = 'Status Information Updated'
			kwargs['statusform'] = form
		elif submit == "personalinfo":
			form = PersonalForm(request.POST, instance=user.personalinfo)
			self.template_name = 'matchmaker/ajax/personalinfoform.html'
			if form.is_valid:
				form.save()
				message = 'Personal Information Updated'
			kwargs['personalform'] = form
		elif submit == "professionalinfo":
			form = ProfessionalForm(request.POST, instance=user.professionalinfo)
			self.template_name = 'matchmaker/ajax/professionalinfoform.html'
			if form.is_valid:
				form.save()
				message = 'Professional Information Updated'
			kwargs['professionalform'] = form
		elif submit == "profileinfo":
			form = UserProfileForm(request.POST, instance=user.profile)
			self.template_name = 'matchmaker/ajax/profileinfoform.html'
			if form.is_valid:
				form.save()
				message = 'Profile Information Updated'
			kwargs['profileform'] = form
		elif submit == "habitinfo":
			form = HabitForm(request.POST, instance=user.habitinfo)
			self.template_name = 'matchmaker/ajax/habitinfoform.html'
			if form.is_valid:
				form.save()
				message = 'Habit Information Updated'
			kwargs['habitform'] = form
		html = render_to_string(self.template_name, context=kwargs, request=request)

		return JsonResponse({
			'html': html,
			'message': message,
			'reload': False
			})


class ProfileSettingsUpdateView(LoginRequiredMixin, TemplateView):
	template_name = 'matchmaker/settings.html'

	def get_context_data(self,**kwargs):
		q = self.request.GET.get('q', None)
		if q == 'change-email':
			self.template_name = "matchmaker/ajax/change_email.html"
		return super().get_context_data()

class UserListView(UserBaseListView):

	def get_context_data(self, **kwargs):
		# for x  in range(1,20):
		# 	message = random.choice(["This is %s message I am a very simple card. I am good at containing small bits of information." % x, "This is %s message I am a very simple card." % x, "This is %s message I am a" % x])
		# 	message_type = random.choice([messages.INFO, messages.WARNING, messages.SUCCESS, messages.ERROR])
		# 	messages.add_message(self.request, message_type, message)
		return super().get_context_data()
		# kwargs['user'] = user
		# return kwargsccxss

class LikedUserListView(UserBaseListView):
	template_name = 'matchmaker/likes.html'

	def get_queryset(self, *args, **kwargs):
		q = self.request.GET.get('q')
		if self.request.is_ajax():
			self.template_name = 'matchmaker/ajax/user_grid.html'
		qs = self.request.user.likes.likedUsers.all()
		if q == 'likedme':
			qs = self.request.user.likedusers.all()
		return qs

	def post(self, request, *args, **kwargs):
		form_name = request.POST.get('fname', None)
		if form_name == 'like':
			user_to_like = request.POST.get('username')
			try:
				user_to_like = User.objects.get(username= user_to_like)
				action_to_take = request.POST.get('user_action')
				if action_to_take == 'on':
					request.user.likes.likedUsers.add(user_to_like)
					message = "%s Liked" % user_to_like
					value = 'off'
				elif action_to_take == 'off':
					request.user.likes.likedUsers.remove(user_to_like)
					message = "%s Unliked" % user_to_like
					value = 'on'
			except User.DoesNotExist:
				raise Http404
		token = get_token(request)

		return JsonResponse({
			'value': value,
			'token': token,
			'message': message
			})

		

class VisitorsListView(UserBaseListView):
	def get_queryset(self, *args, **kwargs):
		return self.request.user.profile.visitors.all()


class ContactsListView(UserBaseListView):
	def get_queryset(self, *args, **kwargs):
		return self.request.user.profile.contacts.all()

	def post(self, request, *args, **kwargs):
		form_name = request.POST.get('fname', None)
		if form_name == 'contacts':
			user_to_like = request.POST.get('username')
			try:
				user_to_like = User.objects.get(username= user_to_like)
				action_to_take = request.POST.get('user_action')
				if action_to_take == 'on':
					request.user.profile.contacts.add(user_to_like)
					message = "%s added to contact list" % user_to_like
					value = 'off'
				elif action_to_take == 'off':
					request.user.profile.contacts.remove(user_to_like)
					message = "%s removed from contact list" % user_to_like
					value = 'on'
			except User.DoesNotExist:
				raise Http404
		token = get_token(request)

		return JsonResponse({
			'value': value,
			'token': token,
			'message': message
			})
class InterestListView(ListView):
	template_name = 'matchmaker/interest_listview.html'
	model = Interest

class MessagesView(LoginRequiredMixin, TemplateView):
	template_name = 'matchmaker/messages.html'


class MembershipListView(LoginRequiredMixin, ListView):
	model = Membership
	template_name = 'matchmaker/membership.html'
	def get_template_names(self):
		print('is request ajax', self.request.is_ajax())
		if self.request.is_ajax():
			self.template_name = "matchmaker/ajax/membership_list.html"
		return super(MembershipListView, self).get_template_names()
	# def get_context_data(self, **kwargs):

	# 	return super().get_context_data(**kwargs)

class NewsletterSubscription(TemplateView):
	pass
class BlockedUsers(LoginRequiredMixin, ListView):
	pass
class DeleteAccountView(LoginRequiredMixin, TemplateView):
	pass