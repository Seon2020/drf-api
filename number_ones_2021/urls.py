from django.urls import path
from .views import HitsList, HitsDetail

urlpatterns = [
    path('', HitsList.as_view(), name='hits_list'),
    path('<int:pk>', HitsDetail.as_view(), name='hits_detail'),
]