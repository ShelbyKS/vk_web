from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('hot/', include('main.urls')),
    path('tag/tag1/', include('main.urls')),
    path('question/q_number/', include('main.urls')),
    path('login/', include('main.urls')),
    path('signup/', include('main.urls')),
    path('ask/', include('main.urls')),
]
