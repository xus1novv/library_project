from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from  .models import Book

class Bookserializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title', 'subtitle','description', 'author', 'isbn','price')


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        title_no = title.replace(" ","") # titledagi probellarni o'chiradi
        if not title_no.isalpha():
                raise serializers.ValidationError({
                    'status': False,
                    'msg': 'Faqat harflardan iborat bolishi kerak'
                })

        book = Book.objects.filter(title=title, author=author)
        if book.exists():
            raise serializers.ValidationError(
                {
                    'status':False,
                    'msg':'Bu kitob bazamizda mavjud'
                }
            )
        return data