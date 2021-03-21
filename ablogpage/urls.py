from django.urls import path
from .views import home,add_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home.as_view(),name="home"),
    path('add_post/',add_post.as_view(),name="add_post"),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)