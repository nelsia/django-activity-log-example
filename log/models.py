from django.db import models


class ActivityLog(models.Model):
    # Request Info
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    query_params = models.TextField(null=True, blank=True)
    headers = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    # Response Info
    response_code = models.PositiveIntegerField()
    response_body = models.TextField(null=True, blank=True)

    # Meta Info
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)

    # Django Traceback HTML
    traceback_html = models.TextField(null=True, blank=True)

    request_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.path)
