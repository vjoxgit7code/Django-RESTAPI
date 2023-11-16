from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restapp.views import TaskViewset,Createuserview,DueTaskViewset,CompletedTaskViewset
from restapp import views
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('task', TaskViewset)
router.register('completed_task', views.CompletedTaskViewset)
router.register('due_task', views.DueTaskViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Createuserview.as_view(),name='user'),
    path('api_auth/',include('rest_framework.urls')),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)