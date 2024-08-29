from django.urls import path
from . import views

urlpatterns = [
    path('sp/',views.Sing_in_p.as_view()),
    path('sc/', views.Sing_in_c.as_view())

]
