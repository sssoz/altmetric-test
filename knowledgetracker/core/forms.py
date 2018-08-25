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
                results['message'] = 'No entry found for <strong>%s</strong> \
                in the last <strong>%s</strong>!' % (q, timeframe)
            elif response.status_code == 502:  # BAD GATEWAY
                results['message'] = 'KnowledgeTracker is down for maintenance.'
            elif response.status_code == 429:  # TOO MANY REQUESTS
                results['message'] = 'Too many requests! Try again soon.'
            elif response.status_code == 403:  # FORBIDDEN
                results['message'] = 'You are not authorized to make this request.'
        return results
