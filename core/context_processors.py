from .models import Company, ContactUs
from .forms import ReceiveContactForm

def get_companies(request):
    companies =  Company.objects.all()
    
    return {'companies': companies}

def get_form(request):
    form = ReceiveContactForm()

    return {'form': form}

def get_contact_info(request):
    contact_s = ContactUs.objects.filter(pk=1).exists()
    contact = None
    if contact_s:
        contact = ContactUs.objects.get(pk=1)

    return {'contact': contact}