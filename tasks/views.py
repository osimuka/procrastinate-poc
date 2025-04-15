from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .tasks import add

@csrf_exempt
def trigger_add_task(request):
    """
    Endpoint to trigger the 'add' task.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            x = data.get("x")
            y = data.get("y")
            if x is None or y is None:
                return JsonResponse({"error": "Both 'x' and 'y' are required"}, status=400)
            
            # Trigger the Procrastinate task using the Django-managed app
            add.defer(x=x, y=y)
            return JsonResponse({"message": "Task has been triggered"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)
