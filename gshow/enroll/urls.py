from django.urls import path
from enroll import views

urlpatterns = [
    path('registration/', views.ShowStudentData),
    # path('success/', views.thankyou),
]