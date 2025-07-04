from django.urls import path
from blog.views import post_list, categories_list, post_detail, custom_post_detail


urlpatterns = [
    path('list/', post_list),
    path('categories/list/', categories_list),
    # path('detail/<str:post_title>/', post_detail),
    path('detail/hello/', custom_post_detail),
    path('detail/<slug:post_slug>/', post_detail),
    path('archive/<int:year>/', post_list),
    path('archive/<int:year>/<int:month>/', post_list),
]