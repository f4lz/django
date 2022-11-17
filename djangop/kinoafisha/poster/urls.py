from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path ('', PosterHome.as_view(), name='home'),
    path ('about/', about, name='about'),
    path ('addpage/', AddPage.as_view(), name='add_page'),
    path ('contact/', ContactFormView.as_view(), name='contact'),
    path ('login/', LoginUser.as_view(), name='login'),
    path ('logout/', logout_user, name='logout'),
    path ('register/', RegisterUser.as_view(), name='register'),
    path ('post/<int:post_id>/', ShowPost.as_view(), name ='post'),
    path ('category/<int:cat_id>/', PosterCategory.as_view(), name ='category'),




     #http://127.0.0.1:8000/
    # path ('cats/<int:catid>/', categories), #http://127.0.0.1:8000/cats/1/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]