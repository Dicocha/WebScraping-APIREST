from django.urls import path, include

from .api import VaultViewSet, VaultDetails
from .views import ScrapeView

'''
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'vault', VaultViewSet, basename='vault')
'''

app_name = 'API'

urlpatterns = [
    path('', VaultViewSet.as_view(), name='vault'),
    path('scrape/', ScrapeView.as_view(), name='scrape'),
    path('<int:pk>', VaultDetails.as_view(), name='detail')
]
