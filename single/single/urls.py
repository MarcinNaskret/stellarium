from django.conf.urls import url,include


urlpatterns = [
    url(r'^', include('watcher.urls')),
    url(r'^lumen/', include('watcher.urls')),

]