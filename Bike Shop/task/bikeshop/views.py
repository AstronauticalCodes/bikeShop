from django.http import HttpResponse


def index(request):
    return HttpResponse('''<h3>To visit our bike shop, click on the link below</h3>
    <button><a href="/bikes">Click Here</a></button>''')