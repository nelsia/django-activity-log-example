from django.urls import path

from .views import ActivityLogView, view_traceback_html

urlpatterns = [
    path("activity_log/", ActivityLogView.as_view()),
    path("activity_log/<int:log_id>/", view_traceback_html, name="activity_log"),
]
