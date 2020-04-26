from django.urls import path
from api import views
urlpatterns = [
    path('flowers/', views.flower_list),
    path('flowers/<int:flower_id>/', views.flower_detailed),
]