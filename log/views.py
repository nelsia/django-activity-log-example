from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from .models import ActivityLog
from .serializers import ActivityLogSerializer


class ActivityLogView(APIView, LimitOffsetPagination):
    def get(self, request):
        qs = ActivityLog.objects.all().order_by("-id")

        paginate_qs = self.paginate_queryset(qs, request, view=self)
        serializer = ActivityLogSerializer(paginate_qs, many=True, context={'request': request})

        res = {
            "data": serializer.data
        }

        return self.get_paginated_response(res)


def view_traceback_html(request, log_id):
    """
    Traceback html view
    """
    try:
        traceback_html = ActivityLog.objects.get(pk=log_id).traceback_html
    except ActivityLog.DoesNotExist:
        return HttpResponseNotFound("Activity Log Not Found")
    
    return HttpResponse(traceback_html,  content_type='text/html')
