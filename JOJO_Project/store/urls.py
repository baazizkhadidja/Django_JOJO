from django.urls import path, include
from store.api import api_create_gat, api_update_gat, api_detail_gat, api_delete_gat,api_all_gat,GateauAdd
# nouv_alb, voir_albums

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    #path('listing/', listing,  name = "listing"),
    #path('<int:album_id>/', detail, name = "detail"),
    #path('search/', search, name = "search"),
    #path('form/', nouv_alb),
    path('api/all/', api_all_gat),
    path('api/add/', api_create_gat),
    path('api/update/', api_update_gat),
    path('api/list/<int:id>', api_detail_gat),
    path('api/delete/<int:id>', api_delete_gat),
    #path('api/v2/gateaux/add', GateauAdd.as_view(), name = 'gatAPI'),
    path('api/v2/gateaux/add', GateauAdd.as_view(), name = 'gatAPI'),
    #path('voir_albums/', voir_albums),
]