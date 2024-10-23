import sys

from django.views import debug

from log.models import ActivityLog


class ActivityLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.traceback_html = None # technical 500 error html

    def __call__(self, request):
        request_body = request.body
        response = self.get_response(request)
        self.process_request(request, response, request_body)
        return response

    def process_request(self, request, response, request_body):
        if not request.path.startswith("/log/"):
            try:
                ActivityLog.objects.create(
                    path=request.path,
                    method=request.method,
                    query_params=request.META.get("QUERY_STRING", ""),
                    headers=str(request.headers),
                    body=request_body.decode("utf-8") if request_body else None,
                    response_body=response.content.decode("utf-8") if response.content else None,
                    response_code=response.status_code,
                    ip_address=request.META.get("HTTP_X_CLIENT_SOURCE", request.META.get("REMOTE_ADDR")),
                    user_agent=request.META.get("HTTP_USER_AGENT", None),
                    traceback_html=self.traceback_html,
                )

            except Exception as e:
                print(e)

        return None

    def process_exception(self, request, exception):
        exc_info = sys.exc_info()
        self.traceback_html = debug.technical_500_response(request, *exc_info).content.decode("utf-8")
