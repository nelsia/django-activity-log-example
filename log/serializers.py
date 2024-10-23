from django.urls import reverse
from rest_framework import serializers

from .models import ActivityLog


class ActivityLogSerializer(serializers.ModelSerializer):
    traceback_url = serializers.SerializerMethodField()

    class Meta:
        model = ActivityLog
        fields = ["id", "path", "method", "query_params", "headers", "body", "response_code", 
                  "ip_address", "user_agent", "request_at", "traceback_url"]

    def get_traceback_url(self, obj):
        if obj.traceback_html is None:
            return ""

        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(reverse("activity_log", kwargs={"log_id": obj.id}))
        return reverse("activity_log", kwargs={"log_id": obj.id})
