from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'Fully functional portfolio website'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'This is a work in project. Watch this space'
    },
]

def projects(request):
    page = 'Projects'
    number = 11
    context = {'page':page, 'number': number, 'projects':projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj} )
