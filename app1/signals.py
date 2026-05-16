from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from .models import Pilot, Flight

@receiver(pre_save, sender=Pilot)
def update_rank(sender, instance, **kwargs):
    if instance.total_hours >= 200:
        instance.role = "SR"
    elif instance.total_hours >= 100:
        instance.role = "MD"
    else:
        instance.role = "JR"

@receiver(pre_delete, sender=Pilot)
def update_pilot(sender, instance, **kwargs):
    flights_to_update = Flight.objects.filter(pilot=instance)
    for flight in flights_to_update:
        flight.pilot = Pilot.objects.exclude(id=instance.id).order_by("total_hours").first()
        flight.save()