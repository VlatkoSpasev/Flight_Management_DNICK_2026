from django.contrib import admin
from .models import Pilot, Baloon, Airline, PilotAirline, Flight
# Register your models here.

class PilotAirlineInline(admin.TabularInline):
    model = PilotAirline
    extra = 0

class FlightAdmin(admin.ModelAdmin):
    list_display = ('code', 'take_off_airport', 'landing_airport', 'pilot')
    list_filter = ('airline', 'pilot')
    exclude = ('user',)
    search_fields = ('code', 'landing_airport', 'take_off_airport', 'pilot__name_surname')
    fieldsets = [
        (
            None,
            {
                "fields": ["code", "take_off_airport", "landing_airport", "image"],
            },
        ),
        (
            "Advanced info",
            {
                "fields": ["pilot", "airline", "baloon"],
            },
        ),
    ]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class AirlineAdmin(admin.ModelAdmin):
    inlines = (PilotAirlineInline, )

admin.site.register(Pilot)
admin.site.register(Baloon)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)
