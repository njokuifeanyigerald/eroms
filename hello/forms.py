from django import forms

from .models import Entry, BMI

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']

    # text = forms.CharField(label='Repeat Password', widget=forms.Textinput(attrs={
    #     'id':"text",
    #     'class':"form-control form-control-user", 
        
    # }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'name':"update",
        'id':"update",
        'class':" form-control form-group col-md-12",
        'rows':"4",
    }), label="")
    
class BMIForm(forms.ModelForm):
    
    class Meta:
        model = BMI
        fields = ['weight', 'age', 'height']

    age = forms.CharField(widget=forms.NumberInput(attrs= {
        'name':"age",
        'id':"age",
        'placeholder': 'age',
        'class':" form-control form-group col-md-6",
    }))
    weight = forms.FloatField()
    height = forms.FloatField()