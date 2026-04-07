from django.urls import path

from .views import IndexView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('test/', NotFoundView.as_view(), name='test'),
]
