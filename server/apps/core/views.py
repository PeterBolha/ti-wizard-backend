import json
import os

from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@extend_schema(summary="Get API logs")
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_logs(request):
    log_file_path = os.path.join('api.json')
    try:
        with open(log_file_path, 'r') as log_file:
            logs = [json.loads(line) for line in log_file if line.strip()]
    except FileNotFoundError:
        return JsonResponse({"error": "Log file not found."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Error decoding log file."}, status=500)

    # return JsonResponse(logs, safe=False) change for httpresponse
    return HttpResponse(json.dumps(logs), content_type="application/json")
