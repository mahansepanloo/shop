from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('Internet_package.urls')),
    path('order/', include('order.urls')),
    path('accounts/', include('accounts.urls'))

]
