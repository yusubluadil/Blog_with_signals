from rest_framework.response import Response
from author.models import CustomUser, AuthorPoint
from blogs.models import Blogs
from . serializers import BlogSerializer, UserSerializer, AuthorPointSerializer
# from rest_framework.decorators import api_view        # bu FUNCTION based views ucundur
from rest_framework.views import APIView                # bu CLASS based views ucundur
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# @api_view(["GET"])
# def all_blogs(request):
#   blogs = Blogs.objects.all()
#   serializer = BlogSerializer(blogs, many = True)      # bloglarin sayi cox olacagina gore many = True yaziriq. ve burada JSONa cevrilir
#   return Response(serializer.data)           # heminn JSONu fronta gonderirik.




# FUNCTION BASED VIEWS





# @api_view(["GET", "POST"])
# def blogs_list_create_api_view(request):
#   if (request.method == "GET"):
#     blogs = Blogs.objects.all()
#     serializer = BlogSerializer(blogs, many = True)
#     return Response(serializer.data)
  
#   elif(request.method == "POST"):
#     serializer = BlogSerializer(data = request.data)     # istifadecinin gonderdiyi datalari alaraq python data typna ceviririk
#     if (serializer.is_valid()):
#       serializer.save()
#       return Response(data = serializer.data, status = status.HTTP_201_CREATED)

#     return Response(status = status.HTTP_400_BAD_REQUEST)     # eger melumatlar dogru olmasa bu return olunur


# @api_view(["GET", "PUT", "DELETE"])
# def blogs_list_detail_api_view(request, pk):
#   try:
#     blog_instance = Blogs.objects.get(pk = pk)    #blogu aliriq
#   except:
#     return Response(
#       {
#         'errors' : {
#           'code' : 404,
#           'message' : f"{pk} id-li blog tapilmadi."
#         }                                                 # Bu mesaj olaraq gedib body hissesine dusur
#       },
#       status = status.HTTP_404_NOT_FOUND
#     )                                           # eger idsi pk olan blog yoxdursa bura olacaq  
  
#   if (request.method == 'GET'):
#     serializer = BlogSerializer(blog_instance)      # blogun melumatlarin aliriq
#     return Response(serializer.data)
  
#   elif (request.method == 'PUT'):
#     serializer = BlogSerializer(blog_instance, data = request.data, partial = True)        # id-i pk olan blog,  partial = True yazanda melumatlari tek tek yazmaq olur.
#     if (serializer.is_valid()):
#       serializer.save()
#       return Response(serializer.data, status = status.HTTP_200_OK)
#     return Response(status = status.HTTP_400_BAD_REQUEST)
  
#   elif (request.method == 'DELETE'):
#     blog_instance.delete()
#     return Response(
#       {
#         'errors' : {
#           'code' : 204,
#           'message' : f"{pk} id-li blog silindi."
#         }                                                 # Bu mesaj olaraq gedib body hissesine dusur
#       },
#       status = status.HTTP_204_NO_CONTENT
#     )






# CLASS BASED VIEWS


# bloglara aiddir 
# class BlogListCreateApiView(APIView):
#   def get(self, request):
#     blogs = Blogs.objects.all()
#     serializer = BlogSerializer(blogs, many = True, context = {'request' : request})
#     return Response(serializer.data)
  
#   def post(self, request):
#     serializer = BlogSerializer(data = request.data, context = {'request' : request})
#     if (serializer.is_valid()):
      
#       #  Tutaq ki, biz gelen datadaki title-in herflerin boyuk etmek isteyirik
#       title = serializer.validated_data.get('title')    # titleni aliriq 
#       upper_title = title.upper()                       # titlenin herflerin boyuduruk
#       serializer.save(title = upper_title)              # boyudulmus titleni savenin icine yaziriq
      
#       return Response(data = serializer.data, status = status.HTTP_201_CREATED)
#     return Response(status = status.HTTP_400_BAD_REQUEST)


# class BlogDetailApiView(APIView):
#   def get_object(self, pk):
#     blog_instance = Blogs.objects.get(pk = pk)
#     return blog_instance
  
#   def get(self, request, pk):
#     blog = self.get_object(pk = pk)
#     serializer = BlogSerializer(blog)
#     return Response(serializer.data)
  
#   def put(self, request, pk):
#     blog = self.get_object(pk = pk)
#     serializer = BlogSerializer(blog, data = request.data)
#     if (serializer.is_valid()):
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request, pk):
#     blog = self.get_object(pk = pk)
#     blog.delete()
#     return Response(status = status.HTTP_204_NO_CONTENT)




#       # userlere aiddir

# class UserListCreateApiView(APIView):
#   def get(self, request):
#     users = CustomUser.objects.all()
#     serializer = UserSerializer(users, many = True)
#     return Response(serializer.data)
  
#   def post(self, request):
#     serializer = UserSerializer(data = request.data)
#     if (serializer.is_valid()):
#       serializer.save()
#       return Response(data = serializer.data, status = status.HTTP_201_CREATED)
#     return Response(status = status.HTTP_400_BAD_REQUEST)


# class UserDetailApiView(APIView):
#   def get_object(self, pk):
#     user_instance = CustomUser.objects.get(pk = pk)
#     return user_instance
  
#   def get(self, request, pk):
#     user = self.get_object(pk = pk)
#     serializer = UserSerializer(user)
#     return Response(serializer.data)
  
#   def put(self, request, pk):
#     user = self.get_object(pk = pk)
#     serializer = UserSerializer(user, data = request.data)
#     if (serializer.is_valid()):
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request, pk):
#     user = self.get_object(pk = pk)
#     user.delete()
#     return Response(status = status.HTTP_204_NO_CONTENT)





#         generics

class BlogListCreateApiView(generics.ListCreateAPIView):
  queryset = Blogs.objects.all()
  serializer_class = BlogSerializer
  permission_classes = [IsAuthenticated]    # sehifeye girende login olmagi teleb edir. amma settingssde yazanda hamsina tetbiq olunur
  
  # Tutaq ki, biz post metodun deyismek isteyirik. O zaman asagidaki emeliyyatlari yerine yetiririk.
  
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data = request.data)    # serializeri aliriq
    if (serializer.is_valid()):
      title = serializer.validated_data.get('title')
      upper_title = title.upper()
      serializer.save(title = upper_title)
      return Response({"detail" : "Blog ugurla create edildi."}, status = status.HTTP_201_CREATED)     # blog create olununanda burdaki mesaj cixacaq
  
  
  #        asagidaki emeliyyatda blog create olarken authorpoint 1 vahid artacaq
  
  # def create(self, request, *args, **kwargs):
  #   serializer = self.get_serializer(data=request.data)
  #   if (serializer.is_valid()):
  #     author = serializer.validated_data.get("author")      # elaqeli authoru tapiriq
  #     author_point = AuthorPoint.objects.get(author = author)   # hemin authorun authorpointin aliriq
  #     author_point.point += 1
  #     author_point.save()
  #     serializer.save()
  #     return Response(data = serializer.data)



class BlogDetailApiView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Blogs.objects.all()
  serializer_class = BlogSerializer

class UserListCreateApiView(generics.ListCreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

class AuthorPointListCreateApiView(generics.ListCreateAPIView):
  queryset = AuthorPoint.objects.all()
  serializer_class = AuthorPointSerializer

class AuthorPointDetailApiView(generics.RetrieveUpdateDestroyAPIView):
  queryset = AuthorPoint.objects.all()
  serializer_class = AuthorPointSerializer