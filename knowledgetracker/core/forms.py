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
        label='See what’s trending on the subject of',
        widget=forms.TextInput(attrs={
            'placeholder': 'keywords…',
            'required': 'required',
            'autofocus': 'autofocus',
            }
        ),
    )

    timeframe = forms.ChoiceField(
        label='in the last',
        choices=TIMEFRAMES,
    )

    page = forms.IntegerField(
        label='Pagination',
        initial=1,
        widget=forms.HiddenInput(),
    )

    def search(self):
        results = {}
        q = self.cleaned_data['q']
        timeframe = self.cleaned_data['timeframe']
        page = self.cleaned_data['page']
        endpoint = 'http://api.altmetric.com/v1/citations/{tf}?q={q}\
            &num_results={num_results}&page={p}&order_by={order_by}'
        url = endpoint.format(
            tf=timeframe,
            q=q,
            num_results=24,
            p=page,
            order_by='at_score',
        )
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
                results['message'] = 'KnowledgeTracker is down for \
                maintenance.'
            elif response.status_code == 429:  # TOO MANY REQUESTS
                results['message'] = 'Too many requests! Try again soon.'
            elif response.status_code == 403:  # FORBIDDEN
                results['message'] = 'You are not authorized to make this \
                request.'
        return results
