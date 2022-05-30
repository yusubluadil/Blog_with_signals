# burda python datalari JSONa ve JSONda pytohona cevrilir.
from author.models import CustomUser, AuthorPoint
from blogs.models import Blogs
from rest_framework import serializers


# class BlogSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only = True) #read_only = True yazdiqda bu o demek olur ki, deyismek olmur.
#   title = serializers.CharField()
#   content = serializers.CharField() # textfield-in yerine de charfield istifade olunur.
#   author = serializers.IntegerField()
#   created = serializers.DateField(read_only = True) #deyisilmediyine gore read_only = True yazdiq

#   def create(self, validated_data):
#     return Blogs.objects.create(**validated_data) #yuxarida olan butun datalari bura gonderir


#   def update(self, instance, validated_data):
#     instance.title = validated_data('title', instance.title) #title fieldinde olan melumati bura menimsedirik.
#     # bu fieldlerin hamisi bir-bir yazilir. Biz bu metoddan yox 2ci metoddan istifade edeceyik. Sadece muellim bunu gormeyimiz ucun gosterdi.

#     instance.save()
#     return instance



class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ['id', 'username', 'author_points']
    # fields = "__all__"


class AuthorPointSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuthorPoint
    fields = "__all__"


class UserforBlogSerializer(serializers.ModelSerializer):        # eger bunu asagidaki author-a menimsetsek o zaman burda olan fieldler gorsenecek (blog olan hissedeki author adinin icinde)
  class Meta:
    model = CustomUser
    fields = ["username", "email", "password", "is_superuser"]


class BlogSerializer(serializers.ModelSerializer):
  #author = serializers.StringRelatedField(read_only = True)           # bu olmasa authorun id-i gorsenir. Bu olanda ise adi.       # eger authora tekce UserSerializer yazsaq o zaman ona aid olan hersey cixacaq
  
  author = serializers.HyperlinkedRelatedField(       # bunu yazdiqda author haqqinda melumat link formasinda verilir
    read_only = True,
    view_name = 'user_detail'           # burdaki name urlsdeki name ile eynidir
  )
  author_id = serializers.PrimaryKeyRelatedField(                     # Bunu yazaraq id ile blog yarada bilirik
    queryset = CustomUser.objects.all(), source = "author", write_only = True      # bura many = True yazmali olsaq grek author_id-e de yazaq
  )
  class Meta:
    model = Blogs
    fields = "__all__"
    # exclude = ["title", "author"] # Bunun icine yazilan fieldler gorsenmir.
    # read_only_fields = ["title"] # ancaq  gosterile bilen fieldler. yeni bunlari update falan etmek olmur.