from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def user_data(request):
    data = {
        "name": "Ashish Gupta",
        "role": "Full Stack Developer",
        "language": "Python (Django)"
    }
    return JsonResponse(data)

@csrf_exempt
def echo(request):
    # simple POST endpoint to receive JSON and echo back
    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8'))
        except Exception:
            payload = {'error': 'invalid json'}
        return JsonResponse({'received': payload})
    return JsonResponse({'error': 'send a POST with JSON'})
