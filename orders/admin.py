from django.contrib import admin

from .models import Contact, Company, Note, Touch, Opportunity
# Register your models here.

class ContactsInline(admin.TabularInline):
    model = Contact
    extra = 1

class TouchesInline(admin.TabularInline):
    model = Touch
    extra = 1

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
        TouchesInline,
        NotesInline,
    ]



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
            'name', 'type_of_business', 'web_site_url', 'phone', 'email_composition')
    list_display_links = (
            'name',)
    list_filter = (
            'name',)
    search_fields = ['name','email_composition', 'type_of_business', 'company__contacts',]
    fieldsets = (
        (None, {
            'fields': ('name', 'type_of_business', 'web_site_url', 'phone', 'email_composition' )
        }),

    )
    inlines = [
        ContactsInline,
        NotesInline,
    ]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Touch)
class TouchAdmin(admin.ModelAdmin):
    pass

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)
