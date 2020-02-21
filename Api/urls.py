from django.conf.urls import url, include
from .views import excursionView, singleExcursionView

urlpatterns = [
    url(r'', excursionView.as_view()),
    url(r'^get/(?P<pk>\d+)', singleExcursionView.as_view())
]











