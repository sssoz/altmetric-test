from django import forms
import requests


class KnowledgeTrackerForm(forms.Form):
    q = forms.CharField(max_length=250)

    def search(self):
        results = {}
        q = self.cleaned_data['q']
        endpoint = 'http://api.altmetric.com/v1/citations/1d?q={query}'
        url = endpoint.format(query=q)
        response = requests.get(url)

        if response.status_code == 200:  # SUCCESS
            results = response.json()
            results['success'] = True
        else:
            results['success'] = False
            if response.status_code == 404:  # NOT FOUND
                results['message'] = 'No entry found for "%s"' % q
        return results
