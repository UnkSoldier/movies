
from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 1,
            'title': 'Les deux tours',
            'year': '2000',
        },
        {
            'id': 2,
            'title': 'Asterix: mission cléopatre',
            'year': '1967',
        },
        {
            'id': 3,
            'title': 'Lupin',
            'year': '2022',
        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse('this is the home page')