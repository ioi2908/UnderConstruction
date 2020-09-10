
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from under_construction_app import views

urlpatterns = [
    path('admin_maen/', admin.site.urls),
    path('', views.email_notify, name='notify'),
    path('thanks', views.thanks, name='thanks'),
    
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]


# urlpatterns += [(
#     static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
#     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
# )
# ]