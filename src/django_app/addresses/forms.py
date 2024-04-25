from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import InlineCheckboxes
from .models import IPAddress, Label, Group, Vlan


class IPAddressForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = ["address", "mask", "group", "label", "vlan", "subnet", "description"]
        widgets = {
            "label": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(IPAddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            "address",
            "mask",
            "group",
            InlineCheckboxes("label"),
            "vlan",
            "subnet",
            "description",
            Submit("submit", "Submit"),
        )


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "description"]


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ["name", "description"]


class VlanForm(forms.ModelForm):
    class Meta:
        model = Vlan
        fields = ["number", "name", "description"]
