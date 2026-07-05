# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(["POST"])
# def zoho_webhook(request):

#     print("=" * 50)
#     print("Webhook Received")
#     print(request.data)
#     print("=" * 50)

#     return Response({"status": "success"})


from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(["POST"])
def zoho_webhook(request):

    print("=" * 60)
    print("HEADERS")
    print(request.headers)

    print("=" * 60)
    print("BODY")
    print(json.dumps(request.data, indent=4))

    return Response({"status": "success"})