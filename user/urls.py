from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user import views

urlpatterns = [
	path('', views.UserListView.as_view(), name='user_list'),
	path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
	path('create/', views.UserCreateView.as_view(), name='user_create'),
	path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
	path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
	path('token/', TokenObtainPairView.as_view()),
	path('token/refresh/', TokenRefreshView.as_view()),

]
