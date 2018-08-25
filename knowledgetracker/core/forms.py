from django import forms
import requests


TIMEFRAMES = (
    ('1d', 'day'),
    ('1w', 'week'),
    ('1m', 'month'),
    ('1y', 'year'),
)


class KnowledgeTrackerForm(forms.Form):
    q = forms.CharField(
        max_length=250,
        label='What’s trending on the subject of',
    )

    timeframe = forms.ChoiceField(
        label='in the last',
        choices=TIMEFRAMES,
    )

    def search(self):
        results = {}
        q = self.cleaned_data['q']
        timeframe = self.cleaned_data['timeframe']
        endpoint = 'http://api.altmetric.com/v1/citations/{tf}?q={query}'
        url = endpoint.format(tf=timeframe, query=q)
        response = requests.get(url)

        if response.status_code == 200:  # SUCCESS
            results = response.json()
            results['success'] = True
        else:
            results['success'] = False
            if response.status_code == 404:  # NOT FOUND
                results['message'] = 'No entry found for "%s"' % q
        return results
