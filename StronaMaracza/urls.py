#
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from Homepage import views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home),
#
# ] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
#
# from django.views.generic import TemplateView
# from emailer import views
#
# urlpatterns = [
#     path('', TemplateView.as_view(template_name="home.html"), name='home'),
#     path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
# ]

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Homepage import views
from django.conf.urls import url

from Homepage.views import alpha
from Homepage.views import beta


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', beta.home),
    path('', alpha.TemplateView.as_view(template_name="home.html"), name='home'),
    path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
    path('opisproduktu/<int:id>/',beta.homeles, name='opisproduktu'),
    path('politykaprywatnosci/', beta.polityka),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
