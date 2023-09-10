from django import forms
from .models import Car, CarReview


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 'model', 'images', 'description', 'year', 'category', 'body_type',
                  'transmission', 'steering', 'drive_type', 'fuel_type', 'color', 'passenger',
                  'condition', 'fuel_consumption', 'amenities', 'safety', 'currency',
                  'rental_price', 'video', 'url', 'slug')


class CarReviewForm(forms.ModelForm):
    class Meta:
        model = CarReview
        fields = '__all__'
