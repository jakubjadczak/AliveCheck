from django import forms
from .models import IPAddress
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class IPAddressForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = ["address", "mask", "group", "label", "vlan", "subnet", "description"]

    def __init__(self, *args, **kwargs):
        super(IPAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))
