from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('flowers/', views.flower_list),
    path('flowers/<int:flower_id>/', views.flower_detailed),
    path('flowers/admin/<int:flower_id>/', views.flower_admin),
    path('order/', views.ShippingView.as_view()),
    path('flowers/comment/', views.CommentView.as_view()),
    path('login/', obtain_jwt_token)
]