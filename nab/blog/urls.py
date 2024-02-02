from django.urls import path, include
from .views import ListPost, PostView, createpost
urlpatterns = [
    path('', ListPost.as_view(), name='ListPost'),
    path('post/<int:pk>', PostView.as_view(), name='PostView'),
    path('createpost', createpost, name='createpost'),
    path('sinup/', include('account.urls'))
]