from django.contrib import admin
from .models import Symptom,ActiveSubstance,Disease,Medicine

admin.site.register(Symptom)
admin.site.register(Disease)
admin.site.register(ActiveSubstance)
admin.site.register(Medicine)

