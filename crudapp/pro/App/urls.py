from django.urls import path
from . import views

urlpatterns = [
    path('emp',views.emp,name='emp'),
    path('show',views.show,name = 'show'),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]