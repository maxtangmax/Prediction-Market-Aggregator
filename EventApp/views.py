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
  user_prediction = request.GET.get('bet_query', '')
  if user_prediction:
        Events_obj = Events.objects.filter(title__icontains=user_prediction)  # Case-insensitive search
  else:
      Events_obj = Events.objects.all()  # Show all events if no prediction is provided

  return render(request, "events.html", {"Events": Events_obj, "user_prediction": user_prediction})

