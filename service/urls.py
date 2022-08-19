from django.urls import path
from .views import brand_service, smm_service, extra_service, web_service

urlpatterns = [
    path('brand/', brand_service, name='brand'),
    path('smm/', smm_service, name='smm'),
    path('extra_service/', extra_service, name='extra'),
    path('web/', web_service, name='web')
]