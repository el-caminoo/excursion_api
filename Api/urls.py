from django.conf.urls import url, include
from .views import singleExcursionView, excursionView, editExcursionView

urlpatterns = [
    # url endpoint to list all excursions
    url(r'^list', excursionView.as_view()),
    # url endpoint to view a single excursion object
    url(r'^get/(?P<pk>\d+)', singleExcursionView.as_view()),
    # url endpoint to edit a single excursion endpoint
    url(r'^edit/(?P<pk>\d+)', editExcursionView.as_view())
]











