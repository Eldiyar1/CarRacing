from django.contrib import admin

from cars.models import Car, CarReview


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'rental_price')
    list_filter = ('brand', 'model', 'year', 'rental_price')
    search_fields = ('brand', 'model', 'year')
    prepopulated_fields = {'slug': ('brand', 'model')}


@admin.register(CarReview)
class CarReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'comment', 'date_added')
    list_filter = ('car', 'comment', 'date_added')
    search_fields = ('car', 'comment', 'date_added')
