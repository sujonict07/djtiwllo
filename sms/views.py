from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def sms_response(request):
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("Welcome to kutumbita. How are you ?")

    # body = request.values.get('Body', None)
    print("body {}".format(type(request)))
    print(str(resp))
    print(request.environ)
    return HttpResponse(str(resp))