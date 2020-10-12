from django.conf.urls import url
from . import views

urlpatterns = [
    url('^users/$', views.UserView.as_view()),
    url('^users/(?P<userEmail>.+)/$', views.UserView.as_view()),
    url('^places/$', views.PlaceListView.as_view()),
    url('^visits/$', views.VisitListView.as_view()),
    url('^visits/(?P<userID>.+)/$', views.VisitListView.as_view()),
    url('^tags/$', views.TagViewSet.as_view({'get': 'list'})),
    url('^coordinates/$', views.CoordinateView.as_view()),
    url('^coordinates/tags/(?P<tagID>.+)/$', views.CoordinateView.as_view()),
    url('^coordinates/places/(?P<placeID>.+)/$', views.CoordinatesView.as_view()),
]