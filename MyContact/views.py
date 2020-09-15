from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import TemplateView, DetailView

# Create your views here.
# def Home(request):
#     contacts = Contact.objects.all()
#     context = {'contacts':contacts}
#     return render(request, 'index.html', context)

def Detail(request, id):
    detail = get_object_or_404(Contact, pk=id)
    context = {
        'detail': detail
    }
    return render(request, 'detail.html', context)

# List View
def HomePage(TemplateView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'
