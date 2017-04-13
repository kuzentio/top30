from django.contrib import admin
from scraper.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Company._meta.fields if field.name not in ['id', 'site']
    ]

    class Meta:
        model = Company

    def __init__(self, *args, **kwargs):
        self.list_display.append('company_url')
        super(CompanyAdmin, self).__init__(*args, **kwargs)

    def company_url(self, company):
        return '<a href="{0}">{1}</a>'.format(company.site, company.site)

    company_url.allow_tags = True


admin.site.register(Company, CompanyAdmin)
