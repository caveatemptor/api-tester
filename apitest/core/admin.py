from django.contrib import admin
from core.models import Project, Endpoint


class EndpointInline(admin.TabularInline):
    model = Endpoint


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        EndpointInline,
    ]


admin.site.register(Project, ProjectAdmin)
