from django.shortcuts import render
from .forms import KnowledgeTrackerForm


def home(request):
    search_results = {}
    if 'q' in request.GET:
        form = KnowledgeTrackerForm(request.GET)
        if form.is_valid():
            search_results = form.search()
    else:
        form = KnowledgeTrackerForm()
    return render(request, 'core/home.html', {
        'form': form,
        'search_results': search_results,
    })
