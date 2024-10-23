from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def view_sample(request):
    """
    sample view
    """
    response_status_code = request.query_params.get("status", "200")

    if response_status_code == "500":
        # 500 error(Name Error)
        aaa

    return Response({"message": "status 200"}, status=200)
