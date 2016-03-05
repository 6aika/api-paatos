from django.contrib import admin
from decisions.models import Case, Action, Organization, Post, Event


class CaseAdmin(admin.ModelAdmin):
    fields = ('iri', 'title', 'description', 'summary', 'category')

admin.site.register(Case, CaseAdmin)
admin.site.register(Action)
admin.site.register(Organization)
admin.site.register(Post)
admin.site.register(Event)
