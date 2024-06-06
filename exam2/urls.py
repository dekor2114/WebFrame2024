from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('blog/', include('blog.urls'))
    #path('<int:pk>/', views.single_page),
    #http://127.0.0.1:8000/
    path('', views.main), 
    path('cartrade/', views.carsale), 
]