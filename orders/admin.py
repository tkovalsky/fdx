from django.contrib import admin

from .models import Transaction, Account
# Register your models here.

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
            'timestamp', 'trade_date', 'settlement_date', 'transaction_type',
            'symbol', 'quantity', 'price',)#'account__number',
    list_display_links = (
            'symbol',)
    list_filter = (
            'symbol','trade_date',)
    search_fields = ['symbol',]
#    fieldsets = (
#        (None, {
#            'fields': ('name', 'type_of_business', 'web_site_url', 'phone', 'email_composition' )
#        }),
#    )
#    inlines = [
#        ContactsInline,
#        NotesInline,
#    ]


'''
class NotesInline(admin.TabularInline):
    model = Note
    extra = 1


class ContactAdmin(admin.ModelAdmin):
    list_display = (
            'name', 'email_address', 'phone', 'last_contact_date')
    list_display_links = (
            'name', 'email_address',)
    list_filter = (
            'last_contact_date', 'company__name',)
    search_fields = ['name','email_address', 'company__name',]
    fieldsets = (
        (None, {
            'fields': ('name', 'email_address', 'phone', 'last_contact_date' )
        }),

    )
    inlines = [
        NotesInline,
    ]

'''

#admin.site.register(Transaction, TransactionAdmin)
