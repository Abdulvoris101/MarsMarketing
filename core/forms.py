from django.forms import ModelForm, Textarea, TextInput, NumberInput, EmailInput
from .models import ReceiveContact

class ReceiveContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReceiveContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['company'].label = ""
        self.fields['phone'].label = ""
        self.fields['message'].label = ""

    class Meta:
        model = ReceiveContact
        fields = ('name', 'email', 'company', 'phone', 'message')

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-contact',
                'placeholder': 'Name*',
            }),
            'email': EmailInput(attrs={
                'class': 'form-contact',
                'placeholder': 'Email*',
            }),
            'company': TextInput(attrs={
                'class': 'form-contact',
                'placeholder': 'Company Name*',
            }),
            'phone': TextInput(attrs={
                'class': 'form-contact',
                'placeholder': 'Phone Number*',
            }),
            'message': Textarea(attrs={
                'class': 'form-contact contact-cn',
                'placeholder': 'Message*',
                'rows': '3',
            })
        }
