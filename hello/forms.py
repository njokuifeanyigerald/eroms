from django import forms

from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']

    # text = forms.CharField(label='Repeat Password', widget=forms.TextArea(attrs={
    #     'id':"text",
    #     'class':"form-control form-control-user", 
        
    # }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'name':"update",
        'id':"update",
        'class':" form-control form-group col-md-12",
        'rows':"4",
    }), label="")
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'How do you feel today?'})