from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Task

def index(request):
    return render(request, 'myapp/example.html')

def render_task_item(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        desc = request.GET.get('desc')
        assign_email = request.GET.get('assign')

        # try:
        #     assigned_user = User.objects.get(email=assign_email)
        # except User.DoesNotExist:
        #     return JsonResponse({'error': 'El usuario asignado no existe'})

        # task = Task.objects.create(
        #     title=title,
        #     description=desc,
        #     assigned_to="eeq@com.co"
        # )

        user = "tatianahoyos"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'user_{user}',
            {
                'type': 'send_notification',
                'message': f'Nueva tarea asignada: {title}'
            }
        )

        context = {
            'title': title,
            'desc': desc,
            'assign': assign_email,
            'user': user
        }

        html = render_to_string('myapp/task_item.html', context=context)
        return JsonResponse({'html': html})
    return JsonResponse({'error': 'Método no permitido'})
        
