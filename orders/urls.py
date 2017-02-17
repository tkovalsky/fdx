from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^accounts/$', views.AccountListView.as_view(), name='accounts'),
    url(r'^account/(?P<pk>[0-9]+)/$', views.AccountDetailView.as_view(), name='account-detail'),
    url(r'^account/create/$', views.CreateAccountView.as_view(), name='create-account'),
    url(r'^account/(?P<pk>\d+)/update/$', views.UpdateAccountView.as_view(), name='update-account'),
    url(r'^account/(?P<pk>\d+)/delete/$', views.DeleteAccountView.as_view(), name='delete-account'),
    url(r'^transactions/$', views.TransactionListView.as_view(), name='transactions'),
    url(r'^transaction/(?P<pk>[0-9]+)/$', views.TransactionDetailView.as_view(), name='transaction-detail'),
    url(r'^transaction/create/$', views.CreateTransactionView.as_view(), name='create-transaction'),
    url(r'^transaction/(?P<pk>\d+)/update/$', views.UpdateTransactionView.as_view(), name='update-transaction'),
    url(r'^transaction/(?P<pk>\d+)/delete/$', views.DeleteTransactionView.as_view(), name='delete-transaction'),

]
