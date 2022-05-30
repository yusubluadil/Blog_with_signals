from django.urls import path
from . import views

urlpatterns = [
  path('blogs/', views.BlogListCreateApiView.as_view()),                  # CLASS based views da yazilan url
  path('blogs/<int:pk>', views.BlogDetailApiView.as_view()),              # CLASS based views da yazilan url
  
  path('author-point/', views.AuthorPointListCreateApiView.as_view()),
  path('author-point/<int:pk>', views.AuthorPointDetailApiView.as_view()),
  
  path('users/', views.UserListCreateApiView.as_view()),
  path('users/<int:pk>', views.UserDetailApiView.as_view(), name = 'user_detail'),
  
  # path('blogs/<int:pk>', views.blogs_list_detail_api_view),             # FUNCTION based views da yazilan url
]
