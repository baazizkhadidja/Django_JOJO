from django.urls import path
from store.views import listing
# , detail, search, nouv_alb, voir_albums

urlpatterns = [
    path('listing/', listing,  name = "listing"),
    #path('<int:album_id>', detail, name = "detail"),
    #path('search/', search, name = "search"),
    #path('form/', nouv_alb),
    #path('voir_albums/', voir_albums),

]