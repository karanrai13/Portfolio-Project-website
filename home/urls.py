from django.contrib import admin
from django.urls import  path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('goal/', views.goal, name='goal'),
   path('vision/', views.vision, name='visioin'),
   path('contact/', views.contact, name='contact'),
    # path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header  =  "Portfolio website admin"  
admin.site.site_title  =  "Portfolio admin site"
admin.site.index_title  =  "portfolio  Admin"