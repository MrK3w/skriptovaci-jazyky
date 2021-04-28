from django import forms

class ClassSearchForm(forms.Form):
    from_class = forms.IntegerField(label='from')
    to_capacity = forms.IntegerField(label='to')