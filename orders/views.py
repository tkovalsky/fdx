from django.contrib.auth.mixins import LoginRequiredMixin #TODO
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.db.models import Q
from django.forms.utils import ErrorList
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import TransactionForm
from .models import Transaction, Account

# Transaction views
class TransactionListView(ListView):
    model = Transaction

    def get_context_data(self, *args, **kwargs):
        context = super(TransactionListView, self).get_context_data(*args, **kwargs)

class TransactionDetailView(DetailView):
    model = Transaction

class CreateTransactionView(CreateView):
    #can use fields or form_class
    #form_class = AddSaleForm
    model = Transaction
    fields = '__all__'

class UpdateTransactionView(UpdateView):
    model = Transaction
    fields = '__all__'

class DeleteTransactionView(DeleteView):
    model = Transaction
    success_url = reverse_lazy('transactions')

# Account views
class AccountListView(ListView):
    model = Account

    def get_context_data(self, *args, **kwargs):
        context = super(AccountListView, self).get_context_data(*args, **kwargs)

class AccountDetailView(DetailView):
    model = Account

class CreateAccountView(CreateView):
    #can use fields or form_class
    #form_class = AddSaleForm
    model = Account
    fields = '__all__'

class UpdateAccountView(UpdateView):
    model = Account
    fields = '__all__'

class DeleteAccountView(DeleteView):
    model = Account
    success_url = reverse_lazy('accounts')


'''
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
'''

def index(request):
    """
    function based view  for the home page of this site
    """
    new_tranasactions=Transaction.objects.all()[:5]


    #Generate counts for some main objects
    num_transactions=Transaction.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count() #'All' is implied by default

    #Render the html template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'new_transactions':new_transactions,
            'num_transactions':num_transactions,
        },
    )
