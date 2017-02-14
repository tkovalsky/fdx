from django.contrib.auth.mixins import LoginRequiredMixin #TODO
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.forms.utils import ErrorList
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import ContactForm
from .models import Contact, Company, Touch, Opportunity



# top page views



# Contacts views
class ContactListView(ListView):
    model = Contact

    def get_context_data(self, *args, **kwargs):
        context = super(ContactListView, self).get_context_data(*args, **kwargs)

class ContactDetailView(DetailView):
    model = Contact

class AddContactView(CreateView):
    #can use fields or form_class
    #form_class = AddSaleForm
    model = Contact
    fields = '__all__'

class UpdateContactView(UpdateView):
    model = Contact
    fields = '__all__'

class DeleteContactView(DeleteView):
    model = Contact
    #success_url = reverse_lazy('contacts')


# Company views
class CompanyListView(ListView):
    model = Company

    def get_context_data(self, *args, **kwargs):
        context = super(CompanyListView, self).get_context_data(*args, **kwargs)

class CompanyDetailView(DetailView):
    model = Company

class AddCompanyView(CreateView):
    #can use fields or form_class
    #form_class = AddSaleForm
    model = Company
    fields = '__all__'

class UpdateCompanyView(UpdateView):
    model = Company
    fields = '__all__'

class DeleteCompanyView(DeleteView):
    model = Company
    #success_url = reverse_lazy('companies')



# marketing page
def home(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']

            template = get_template('contact_template.txt')

            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message,
                })
            content = template.render(context)

            email = EmailMessage('New contact form submission',
                                    content,
                                    'Your website <hello@toddkovalsky.com>',
                                    ['youremail@gmail.com'],
                                    headers = {'Reply-To': contact_email },
                                    )
            email.send()
            return redirect('home')

    return render(request, 'home.html', { 'form': form_class, })

def index(request):
    """
    function based view  for the home page of this site
    """
    new_contacts=Contact.objects.all()[:5]


    #Generate counts for some main objects
    num_contacts=Contact.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count() #'All' is implied by default

    #Render the html template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'new_contacts':new_contacts,
            'num_contacts':num_contacts,
        },
    )
