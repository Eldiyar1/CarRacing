from django.shortcuts import get_object_or_404
from .models import Car, CarReview
from .forms import CarForm, CarReviewForm
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


class CarListView(ListView):
    template_name = 'car_list.html'
    queryset = Car.objects.all()

    def get_queryset(self):
        return Car.objects.all()


class CarDetailView(DetailView):
    template_name = 'car_detail.html'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(Car, id=car_id)


class CreateCarView(CreateView):
    template_name = 'create_car.html'
    form_class = CarForm
    queryset = Car.objects.all()
    success_url = '/cars/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(Car, id=car_id)

    def form_valid(self, form):
        return super(CreateCarView, self).form_valid(form=form)


class DeleteCarView(DeleteView):
    template_name = 'delete_car.html'
    success_url = '/cars/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(Car, id=car_id)


class UpdateCarView(UpdateView):
    template_name = 'update_car.html'
    form_class = CarForm
    success_url = '/cars/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(Car, id=car_id)

    def form_valid(self, form):
        return super(UpdateCarView, self).form_valid(form=form)


class CarReviewView(CreateView):
    template_name = 'car_review.html'
    queryset = Car.objects.all()
    form_class = CarReviewForm
    success_url = '/cars/'

    def get_object(self, **kwargs):
        add_review = self.kwargs.get('id')
        return get_object_or_404(CarReview, id=add_review)

    def form_valid(self, form):
        return super(CarReviewView, self).form_valid(form=form)


class CarSearch(ListView):
    template_name = 'car_list.html'
    context_object_name = 'car'
    paginate_by = 2

    def get_queryset(self):
        return Car.objects.filter(brand__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context