from django.contrib import admin
from django.urls import path, include
from tickets import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api/', include('rest_framework.urls'))
    path("django/jsonresponsenomodel/", views.no_rest_no_model),
    #2
    path("django/jsonresponsefrommodel/", views.no_rest_from_model),
    #3 GET POST from rest framework function  based view @api_view
    path("rest/fbv/",views.FBV_List),
    #3.1 GET PUT DELETE from rest framework function  based view @api_view
    path("rest/fbv/<int:pk>",views.FBV_pk),
]
