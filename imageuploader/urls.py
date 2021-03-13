
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('upload',views.Upload,name="upload"),
    path('contact',views.Contact, name="contact"),
    path('gallery',views.Gallery,name="gallery"),
    path('bg',views.Bg,name="bg"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
