from __future__ import absolute_import
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
import json

class JsonForm(forms.Form):
    json = forms.CharField(label='JSON body', max_length=10000, widget=forms.Textarea,
            help_text =_("This field must contain a JSON object e.g. {}"))

    required_css_class = 'required'


    def clean_json(self):
        jsonf = self.cleaned_data.get('json')

        try:
            j = json.loads(jsonf)
            if type (j) != type({}):
                msg=_("The field does not contain a valid JSON object.")
                raise forms.ValidationError(msg)
        except ValueError:  
            msg=_("The field does not contain valid JSON.")
            raise forms.ValidationError(msg)
        
        return jsonf
        
    