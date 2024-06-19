from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

def index(request):
    return render(request, 'myapp/example.html')

def render_task_item(request):
    title = request.GET.get('title')
    desc = request.GET.get('desc')
    assign = request.GET.get('assign')

    context = {
        'title': title,
        'desc': desc,
        'assign': assign,
    }

    html = render_to_string('myapp/task_item.html', context=context)
    return JsonResponse({'html': html})
