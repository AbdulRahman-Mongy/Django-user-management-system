from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home_page , name= 'home'),
    path('login/' , views.login_page , name= 'login'),
    path('logout/' , views.logout_page , name= 'logout'),
    path('register/', views.register_page , name= 'register'),
    path('profile/', views.profile_page, name='profile'),

]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)