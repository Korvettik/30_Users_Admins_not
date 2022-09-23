from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import ad.views
from HW_30 import settings
from ad import views
from user.views import LocationViewSet

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', ad.views.IndexView.as_view()),
	path('ad/', include('ad.urls')),
	path('cat/', include('category.urls')),
	path('user/', include('user.urls')),

	path('selection/', views.SelectionListView.as_view(), name='selection_list'),
	path('selection/<int:pk>/', views.SelectionDetailView.as_view(), name='selection_detail'),
	path('selection/create/', views.SelectionCreateView.as_view(), name='selection_create'),
	path('selection/<int:pk>/update/', views.SelectionUpdateView.as_view(), name='selection_update'),
	path('selection/<int:pk>/delete/', views.SelectionDestroyView.as_view(), name='selection_delete'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = routers.SimpleRouter()
router.register('location', LocationViewSet)
urlpatterns += router.urls
