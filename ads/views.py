from django.shortcuts import render
from .models import AdTitle

def index(request):
     return render(request, 'ads/index.html')

def ads(request):
    ads = AdTitle.objects.order_by()
    return render(request, 'ads/ad.html', {'ads': ads})

def ad(request, ad_id):
     ad = AdTitle.objects.get(id=ad_id)
     entries = ad.ad_set.order_by()
     context = {'ad': ad, 'entries': entries}
     return render(request, 'ads/ads.html', context)
