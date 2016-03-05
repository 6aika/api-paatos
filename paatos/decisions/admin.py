from django.contrib import admin
from decisions.models import Case, Action
from decisions.models import Event, Organization, Post, Person, Area


class CaseAdmin(admin.ModelAdmin):
    fields = ('iri', 'title', 'description', 'summary', 'category')
admin.site.register(Case, CaseAdmin)

admin.site.register(Action)

# Popolo
admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Area)
