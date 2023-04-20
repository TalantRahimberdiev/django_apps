
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Studies
# Create your views here.


class StudiesList(ListView):
    model = Studies
    template_name = 'list.html'


class StudiesCreate(CreateView):
    model = Studies
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('studies-list')


class StudiesUpdate(UpdateView):
    model = Studies
    template_name = 'update.html'
    fields = '__all__'
    success_url = reverse_lazy('studies-list')


class StudiesDelete(DeleteView):
    model = Studies
    template_name = 'delete.html'
    fields = '__all__'
    success_url = reverse_lazy('studies-list')


class StudiesDetail(DetailView):
    model = Studies
    template_name = 'detail.html'
    fields = '__all__'
