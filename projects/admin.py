from django.contrib import admin
from .models import Profile, Project, Certificate, CertifyingInstitution


class CertificateInline(admin.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
