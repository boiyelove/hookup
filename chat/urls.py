from django.urls import path, re_path


from .views import SingleThreadView

app_name = 'chat'
urlpatterns = [
    # path("", InboxView.as_view()),
    re_path(r"^(?P<username>[\w.@+-]+)/$", SingleThreadView.as_view()),
]
