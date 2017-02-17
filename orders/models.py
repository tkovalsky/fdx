import datetime

from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.urls import reverse


class Order(TimeStampedModel):
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    ORDER_STATUS_CHOICES = (
        ('u', 'Undefined'),
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES,
            blank=True, default='u')
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    symbol = models.CharField(max_length=10, null=False, blank=False)
    cusip = models.CharField(max_length=10, null=True, blank=True)
    stop_price = models.DecimalField(max_digits=10, decimal_places=4)
    limit_price = models.DecimalField(max_digits=10, decimal_places=4)
    #average_price = models.DecimalField(max_digits=10, decimal_places=4)

class Broker(TimeStampedModel):
    transactions = models.ForeignKey('Transaction', blank=True, null=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    short_code = models.CharField(max_length=10, null=False, blank=False)

    BROKER_STATUS_CHOICES = (
        ('a', 'Approved'),
        ('n', 'Not Approved'),
    )

    status = models.CharField(max_length=1, choices=BROKER_STATUS_CHOICES,
            blank=True, default='n')
    default_commission_per_share = models.DecimalField(max_digits=4, decimal_places=4, default=0.03)


class Transaction(TimeStampedModel):
    order = models.ForeignKey('Order', blank=True, null=True)
    execution_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    trade_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    settlement_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    ACCOUNT_TYPE_CHOICES = (
        ('c', 'Cash'),
        ('m', 'Margin'),
        ('s', 'Short'),
    )

    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES,
            blank=True, default='c')

    TRANSACTION_TYPE_CHOICES = (
        ('b', 'Buy'),
        ('bx', 'Buy Cancel'),
        ('bo', 'Buy Option'),
        ('bc', 'Buy Cover'),
        ('d', 'Dividend'),
        ('s', 'Sell'),
        ('sx', 'Sell Cancel'),
        ('so', 'Sell Option'),
        ('ss', 'Sell Short'),
    )
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES,
            blank=False, help_text="type")
    filled_quantity = models.DecimalField(max_digits=10, decimal_places=4)
    executed_price = models.DecimalField(max_digits=10, decimal_places=4)
    fee = models.DecimalField(max_digits=10, decimal_places=4)
    cents_per_share = models.DecimalField(max_digits=10, decimal_places=4, default=0.03)
    transaction_amount_gross = models.DecimalField(max_digits=25, decimal_places=4)

    SLEEVE_TYPE_CHOICES = (
        ('e', 'Equity'),
        ('b', 'Bonds'),
        ('u', 'Unmanaged'),
        ('n', 'None'),
    )
    sleeve = models.CharField(max_length=1, choices=SLEEVE_TYPE_CHOICES,
            blank=False, default='n')
    broker_of_record = models.CharField(max_length=4, blank=False, null=False, default='FDX')
    reason = models.TextField(blank=True, null=True)


    def __str__(self):
        return "%s  %s  %s  %s  %s" % (self.transaction_type, self.filled_quantity, self.executed_price,
                                self.broker_of_record, self.cents_per_share)

    def get_absolute_url(self):
         """
         Returns the url to access a contact.
         """
         return reverse('transaction-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-trade_date"]


class Account(TimeStampedModel):
    transactions = models.ForeignKey('Transaction', on_delete=models.SET_NULL, null=True, blank=True)
    number = models.CharField(max_length=20, unique=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "%s   %s" % (self.number, self.name)

    def get_absolute_url(self):
         """
         Returns the url to access a contact.
         """
         return reverse('account-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-created"]




'''
class Touch(TimeStampedModel):
    contact = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    touch_type = models.CharField(max_length=20) #add a reference for a dropdown selector
    follow_up_days = models.PositiveIntegerField(default=0)
    follow_up_date = models.CharField(max_length=20, null=True, blank=True) #add a reference for a dropdown selector

    def __str__(self):
        return "#s - #s" % (self.date, self.touch_type)

    def get_absolute_url(self):
         """
         Returns the url to access a particular touch.
         """
         return reverse('touch-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "touches"


class Note(TimeStampedModel):
    contact = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    note = models.TextField()

    def __str__(self):
        return "#s - #s - #s" % (self.contact, self.company, self.note )

    def get_absolute_url(self):
         """
         Returns the url to access a particular note.
         """
         return reverse('note-detail', args=[str(self.id)])
'''
