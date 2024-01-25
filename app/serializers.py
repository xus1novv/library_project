from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id','title', 'subtitle','author', 'isbn', 'price',]


    def validate(self, data):
        title = data.get('title', None) # title bor bo'lsa oladi agar bo'lmasa None qiymat qaytaradi
        author = data.get('author', None)
        # Faqat harflardan tashkil topganligini tekshiradi
        if not title.isalpha():
            raise ValidationError(
                {
                    "status":False,
                    'message':"All of chars is not alpha!"
                }
            )
        # Agar DB da biz saqlayotgan kitoblarimiz bor bo'lsa Saqlamaydi
        if Book.objects.filter(title=title, author=author).exists(): # exists() metodi agar bazamizda shu kitob bo'lsa True qiymat qaytaradi.
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitob avval saqlangan!"
                }
            )
        return data


    def validate_price(self, price):
        if price<0:
            raise ValidationError(
                {
                    "status":False,
                    "message":"Narx noto'g'ri kiritildi!"
                }
            )

