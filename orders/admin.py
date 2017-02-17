from django.contrib import admin

from .models import Transaction, Account, Order
# Register your models here.


class TransactionsInline(admin.TabularInline):
    model = Transaction
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
            'timestamp', 'status', 'quantity', 'symbol', 'stop_price',
            'limit_price',)
    list_display_links = (
            'symbol',)
    list_filter = (
            'symbol','timestamp',)
    search_fields = ['symbol',]
#    fieldsets = (
#        (None, {
#            'fields': ('name', 'type_of_business', 'web_site_url', 'phone', 'email_composition' )
#        }),
#    )
    inlines = [
        TransactionsInline,
    ]


@admin.register(Account)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
            'number', 'name',)
    list_display_links = (
            'number',)
    #list_filter = (
    #        'symbol','trade_date',)
    search_fields = ['number', 'name',]



@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
            'execution_timestamp', 'trade_date', 'settlement_date', 'transaction_type',
            'filled_quantity', 'executed_price',)#'account__number',
    list_filter = (
            'broker_of_record','trade_date',)
    search_fields = ['broker_of_record',]
#    fieldsets = (
#        (None, {
#            'fields': ('name', 'type_of_business', 'web_site_url', 'phone', 'email_composition' )
#        }),
#    )
#    inlines = [
#        ContactsInline,
#        NotesInline,
#    ]
