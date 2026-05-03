from django.forms import ModelForm
from .models import Flight

class FlightForm(ModelForm):
    class Meta:
        model = Flight
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'