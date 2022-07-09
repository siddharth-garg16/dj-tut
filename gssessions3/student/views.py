from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Siddharth'
    request.session.set_expiry(150) #150 sec life
    request.session.set_expiry(0) #expire on browser close
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session['name']
    # name = request.session.get('name')
    cur_age = request.session.get_session_cookie_age()
    exp_age = request.session.get_expiry_age()
    exp_date = request.session.get_expiry_date()
    return render(request, 'student/getsession.html', {'name':name, 'current_age':cur_age, 'expiry_age':exp_age, 'expiry_date':exp_date})

def delsession(request):
    request.session.flush()
    request.session.clear_expired() #clears expired sessions from database
    return render(request, 'student/delsession.html')

#set_test_cookie(), check_test_cookie().....are used to check cookie support on the user end. 