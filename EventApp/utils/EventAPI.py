import json
import requests
from EventApp.models import Events, Markets
#credit:https://github.com/Polymarket/agents/blob/main/agents/polymarket/gamma.py
class EventAPI:
  def __init__(self):
    self.PM_url="https://gamma-api.polymarket.com"
    self.PM_events_endpoint=self.PM_url+"/events"


  def parsePolyMarketOpenEvents(self):
    r = requests.get(self.PM_events_endpoint+"?closed=false&limit=1000")
    response = r.json()
    for event in response:
      #populate Events model with events
      event_id = event['id']
      if not Events.objects.filter(id=event_id).exists():
        # Populate Events model with new events
        event_title = event['title']
        event_description = event['description']
        cur_event = Events.objects.create(
          title=event_title, 
          id=event_id, 
          description=event_description
          )
        cur_event.save()
      else:
        cur_event = Events.objects.get(id=event_id)
      #map markets to events
      for market in event['markets']:
        market_id = market['id']
        if not Markets.objects.filter(id=market_id).exists():
          market_question = market['question']
          market_description = market['description']
          new_market = Markets.objects.create(
              question=market_question,
              id=market_id,
              description=market_description,
              event=cur_event
          )
          new_market.save()

    #def getEvents(self, title):
      #Turn title into vector
      #compute dot product ....
      #return events that the user wants
    


