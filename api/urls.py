from django.conf.urls import url
from . import views

urlpatterns = [
    url('^users/$', views.UserView.as_view()),
    url('^users/(?P<userID>.+)/$', views.UserView.as_view()),
    url('^places/$', views.PlaceListView.as_view()),
    url('^visits/$', views.VisitListView.as_view()),
    url('^visits/(?P<userID>.+)/$', views.VisitListView.as_view()),
]