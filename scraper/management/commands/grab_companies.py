from httplib import HTTPException
import requests
from django.core.management import BaseCommand
from scraper.models import Company


class Command(BaseCommand):
    COMPONENTS = 'components'
    PROFILES = ['assetProfile', 'calendarEvents']
    components_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/%5EDJI'
    api_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{abbr}'

    @staticmethod
    def get_companies_names(components):
        url = 'https://query2.finance.yahoo.com/v7/finance/quote'
        params = {
            'symbols': ','.join(components),
            'fields': ['longName', 'shortName']
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            companies = {}
            for data in response.json()['quoteResponse']['result']:
                companies[data['symbol']] = data.get('longName', data.get('shortName'))
            return companies
        raise HTTPException()

    def handle(self, *args, **options):
        response = requests.get(self.components_url, params={'modules': self.COMPONENTS})
        if response.status_code == 200 and not response.json()['quoteSummary']['error']:
            components = response.json()['quoteSummary']['result'][0]['components']['components']
            names = self.get_companies_names(components)
            for component in components:
                url = self.api_url.format(abbr=component)
                response = requests.get(url, params={'modules': ','.join(self.PROFILES)})
                result = response.json()['quoteSummary']['result'][0]
                profile = result[self.PROFILES[0]]
                earnings = result[self.PROFILES[1]]['earnings']
                data = {
                    'name': names[component],
                    'revenue': float(earnings.get('revenueAverage')['raw']),
                    'site': profile.get('website'),
                    'street_address1': profile.get('address1'),
                    'street_address2': profile.get('address2'),
                    'city': profile.get('city'),
                    'zip_code': profile.get('zip'),
                    'country': profile.get('country'),
                    'number_of_employee': profile.get('fullTimeEmployees'),
                    'industry': profile.get('industry'),
                }
                company, created = Company.objects.update_or_create(
                    abbr=component,
                    defaults=data
                )
                if created:
                    print 'New company was created'
                else:
                    print 'Company {id} updated'.format(id=company.id)