from django import forms
from myapp1.models import OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['itemServing', 'clientServing', 'totalItemsOrder']
        labels = {'clientServing': 'Client Name', 'totalItemsOrder': 'Quantity'}
        widgets = {'clientServing': forms.RadioSelect}


class InterestForm(forms.Form):
    interested = forms.RadioSelect({'Yes': 1, 'No': 0})
    quantity = forms.IntegerField(min_value=1, initial=1)
    comments = forms.CharField(widget=forms.Textarea, max_length=500, label='Additional Comments')


