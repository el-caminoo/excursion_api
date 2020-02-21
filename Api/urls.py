from django.conf.urls import url, include
from .views import singleExcursionView, excursionView, editExcursionView, signup
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    # url endpoint to obtain access token 
    url(r'^token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url endpoint to obtain a new access token
    url(r'^refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # url endpoint to list all excursions
    url(r'^list', excursionView.as_view()),
    # url endpoint to view a single excursion object
    url(r'^get/(?P<pk>\d+)', singleExcursionView.as_view()),
    # url endpoint to edit a single excursion endpoint
    url(r'^edit/(?P<pk>\d+)', editExcursionView.as_view()),
    # form to create user to obtain an access token
    url(r'^users/$', signup)
]











