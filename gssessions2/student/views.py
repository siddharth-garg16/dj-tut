from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Siddharth'
    return render(request, 'student/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name')
    keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', '21')
    return render(request, 'student/getsession.html', {'name':name, 'keys':keys, 'items':items})

def delsession(request):
    request.session.flush()
    return render(request, 'student/delsession.html')