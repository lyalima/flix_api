from rest_framework import serializers
from django.db.models import Avg
from .models import Movie
from datetime import date


class MovieModelSerializer(serializers.ModelSerializer):
    # campo calculado de serializer
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
    
    # função para a lógica do campo calculado
    def get_rate(self, obj):
        #calculo com ORM:
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        
        return None

        # calculo sem ORM:
        # obj é um movie; reviews é a relação entre movies e reviews; all() pega todas as reviews
        #reviews = obj.reviews.all()

        #if reviews:
        #   sum_reviews = 0

        #   for review in reviews:
        #        sum_reviews += review.stars
            
        #    count_reviews = reviews.count()

        #    return round(sum_reviews / count_reviews, 1)
        

    def validate_release_date(self, value):
        current_date = date.today()

        if value > current_date:
            raise serializers.ValidationError('A data de lançamento não pode ser posterior à data atual.') 
        if value.year < 1990:
            raise serializers.ValidationError('O ano de lançamento não pode ser anterior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O resumo não pode ter mais de 200 caracteres.') 
        return value