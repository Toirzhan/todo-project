from django.contrib import admin
from django.urls import path, include

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
    path('feedback/', include('feedback.urls')),
    path('reviews/', include('feedback.urls')),
    path('ai/', include('ai_assistant.urls')),
]