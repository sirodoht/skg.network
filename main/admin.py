from django.contrib import admin

from main import models


# Candidacy
class CandidacyAdmin(admin.ModelAdmin):
    list_display = ("leader", "party", "website", "id")


admin.site.register(models.Candidacy, CandidacyAdmin)
