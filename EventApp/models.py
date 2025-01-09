from django.db import models

# Create your models here.

class Events(models.Model):
  title = models.CharField(max_length=200)
  id = models.IntegerField(primary_key=True)
  description = models.CharField(max_length=5000, default='')

  def __str__(self):
      return self.title

class Markets(models.Model):
  question = models.CharField(max_length=200)  # Specify max_length
  id = models.IntegerField(primary_key=True)  # Set as primary key
  description = models.CharField(max_length=500)  # Specify max_length
  event = models.ForeignKey(Events, 
                              related_name='markets', 
                              on_delete=models.CASCADE)
  def __str__(self):
      return self.question
  
  #NOTES:#
  ## Accessing markets related to an event
  #associated_markets = event.markets.all()
