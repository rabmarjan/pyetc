from django.conf.urls import include, url
from django.contrib import admin
from cv_api.face_detector import views
urlpatterns = [
    # Examples:

    url(r'^face_detection/detect/$', views.detect),

    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
