from django.contrib import admin
from scraper.models import Company


class CompanyAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        self.list_display = [field.name for field in Company._meta.fields if field.name != "id"]
        super(CompanyAdmin, self).__init__(*args, **kwargs)

    class Meta:
        model = Company


admin.site.register(Company, CompanyAdmin)
