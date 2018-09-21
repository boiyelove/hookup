from django.urls import path
from . import views

app_name='matchmaker'
urlpatterns = [
	path('', views.UserHomeView.as_view(), name='view-user-home'),
	path('contacts/', views.ContactsListView.as_view(), name='list-contacts'),
	path('discovery/', views.DiscoveryTemplateView.as_view(), name='view-discovery'),
	path('profile/', views.UserProfileView.as_view(), name='view-profile'),
	path('profiles/<slug:username>/', views.UserProfileView.as_view(), name='view-user-profile'),
	path('visitors/', views.VisitorsListView.as_view(), name='list-visitors'),
	path('likes/', views.LikedUserListView.as_view(), name='list-likes'),
	path('msg/', views.MessagesView.as_view(), name='view-msg'),
	path('settings/', views.ProfileSettingsUpdateView.as_view(), name='view-settings'),
	path('membership/', views.MembershipListView.as_view(), name='list-membership'),
	path('newsletter/', views.NewsletterSubscription.as_view(), name='newsletter-subscription'),
	path('blocked-users/', views.BlockedUsers.as_view(), name='block-user'),
	path('delete-account/', views.DeleteAccountView.as_view(), name='delete-account'),


]