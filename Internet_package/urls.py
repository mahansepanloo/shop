from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Show.as_view()),
    path('create/',views.create_i.as_view())

]
