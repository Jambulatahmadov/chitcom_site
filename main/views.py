from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home page',
        'values': ['some', 'hello', '123'],
        'obj': {
            'car': 'bmw',
            'age': 18,
            'hobby': 'football',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
