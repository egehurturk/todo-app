
from django.contrib import admin
from django.urls import path, include
from add_smt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('add_smt.urls'))
]
