from django.contrib import admin
from decisions.models import Case


class CaseAdmin(admin.ModelAdmin):
    fields = ('iri', 'title', 'description', 'summary', 'category')
admin.site.register(Case, CaseAdmin)

