from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path
=======
from django.urls import path, include
>>>>>>> d3737c12f4e6f58f7e54ef10e5bc580632cf75ab
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/', include('api.urls'))
]
