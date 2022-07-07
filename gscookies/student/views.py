from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('name', 'siddharth')
    return response

def getcookie(request):
    # nm = request.COOKIES['name']
    nm = request.COOKIES.get('name', 'Guest User') #defualt value
    return render(request, 'student/getcookie.html', {'name':nm})

def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response