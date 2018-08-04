from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class SearchTemplateView(TemplateView):
	template_name = 'matchmaker/search.html'

	def get_context_data(self, **kwargs):
		#get query string from url
		#filter user by query string
		#update kwargs
		return kwargs

class UserProfileTemplateView(TemplateView):
	template_name = 'matchmaker/search.html'

	def get_context_data(self, **kwargs):
		#get query string from url
		#filter user by query string
		#update kwargs
		return kwargs


class ProfileSettingsUpdateView(FormView):
	template_name = 'matchmaker/settings.html'
	form_class = ''


class UserListView(ListView):
	template_name = 'matchmaker/user_list.html'
	query_set = User.objects.all()
	paginated_by = 30


class InterestListView(ListView):
	template_name = 'matchmaker/interest_listview.html'
	model = Interest

