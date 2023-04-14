from django.contrib import admin
from contacts.models import Contact,ContactNumber
# Register your models here.


class ContactNumberInline(admin.StackedInline):
    model = ContactNumber

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company')
    inlines = [ContactNumberInline]

admin.site.register(Contact,ContactAdmin)