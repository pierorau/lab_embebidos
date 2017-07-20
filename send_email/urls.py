from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [

                  url(r'^v1/', include('test_email.url')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
