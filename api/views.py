from django.http import JsonResponse
from django.views import View
from .models import Vault
from .scraper import VaultScraper
from .serializers import VaultSerializer

# Create your views here.

class ScrapeView(View):
    def get(self, request, *args, **kwargs):
        data = Vault.objects.all()

        if not data.exists():
            scraper = VaultScraper()
            data = scraper.scrape()
            data = Vault.objects.all()  # Re-fetch after scraping to include new data

        serializer = VaultSerializer(data, many=True)
        return JsonResponse({'status': 'success', 'data': serializer.data})
