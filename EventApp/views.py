from django.shortcuts import render, HttpResponse
from .models import Events,Markets
from .utils.EventAPI import EventAPI

# Create your views here.
def home(request):
  return render(request, "home.html")

def events(request):
  #populate model database
  event_api = EventAPI()
  event_api.parsePolyMarketOpenEvents()
  Events_obj = Events.objects.all()
  return render(request, "events.html", {"Events":Events_obj})

