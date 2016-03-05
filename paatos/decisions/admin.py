from django.contrib import admin
from decisions.models import Case, Action


class CaseAdmin(admin.ModelAdmin):
    fields = ('iri', 'title', 'description', 'summary', 'category')
admin.site.register(Case, CaseAdmin)
admin.site.register(Action)