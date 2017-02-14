from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^contacts/$', views.ContactListView.as_view(), name='contacts'),
    url(r'^contact/(?P<pk>[0-9]+)/$', views.ContactDetailView.as_view(), name='contact-detail'),
    url(r'^contact/create/$', views.AddContactView.as_view(), name='add-contact'),
    url(r'^contact/(?P<pk>\d+)/update/$', views.UpdateContactView.as_view(), name='update-contact'),
    url(r'^contact/(?P<pk>\d+)/delete/$', views.DeleteContactView.as_view(), name='delete-contact'),
    url(r'^company/create/$', views.AddCompanyView.as_view(), name='add-company'),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetailView.as_view(), name='company-detail'),
    url(r'^companies/$', views.CompanyListView.as_view(), name='companies'),

]
