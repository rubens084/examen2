from django import forms

from .models import car

class carModelForm(forms.ModelForm):
    content = forms.CharField(label='',
                              widget=forms.Textarea(
                                        attrs={'placeholder':"car",
                                               'class': "textarea"}
                              ))

    class Meta:
        model = car
        fields = [
            "make", "Type", "year", "colour", "price"
        ]
