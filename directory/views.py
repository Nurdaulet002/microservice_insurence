from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Insurance, Insurer, Service

class InsuranceListView(ListView):
    template_name = 'directory/insurance.html'
    model = Insurance
    context_object_name = 'insurances'


class UrlMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.request.GET.get('url', None)
        return context


class InsuranceMixin:
    model = Insurance
    fields = ['title']

    def get_success_url(self):
        return reverse_lazy('directory:insurence_list')

# Mixin редактирования insurance
class InsuranceEditMixin(InsuranceMixin, UrlMixin):
    template_name = 'directory/insurance/form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Создать категорию
class InsuranceCreateView(InsuranceEditMixin, CreateView):
    pass


# Обновить категорию
class InsuranceUpdateView(InsuranceEditMixin, UpdateView):
    pass


# Удалить категорию
class InsuranceDeleteView(InsuranceMixin, UrlMixin, DeleteView):
    template_name = 'directory/insurance/delete.html'


class InsurerListView(ListView):
    template_name = 'directory/insurer.html'
    model = Insurer
    context_object_name = 'insurers'


class InsurerMixin:
    model = Insurer
    fields = ['title']

    def get_success_url(self):
        return reverse_lazy('directory:insurer_list')

# Mixin редактирования insurance
class InsurerEditMixin(InsurerMixin, UrlMixin):
    template_name = 'directory/insurer/form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Создать категорию
class InsurerCreateView(InsurerEditMixin, CreateView):
    pass


# Обновить категорию
class InsurerUpdateView(InsurerEditMixin, UpdateView):
    pass


# Удалить категорию
class InsurerDeleteView(InsurerMixin, UrlMixin, DeleteView):
    template_name = 'directory/insurer/delete.html'



class ServiceListView(ListView):
    template_name = 'directory/service.html'
    model = Service
    context_object_name = 'services'

class ServiceMixin:
    model = Service
    fields = ['title', 'code']

    def get_success_url(self):
        return reverse_lazy('directory:service_list')

# Mixin редактирования insurance
class ServiceEditMixin(ServiceMixin, UrlMixin):
    template_name = 'directory/service/form.html'

    def form_valid(self, form):
        parent = self.kwargs.get('parent', None)
        form_obj = form.save()
        return super().form_valid(form)

# Создать категорию
class ServiceCreateView(ServiceEditMixin, CreateView):
    pass


# Обновить категорию
class ServiceUpdateView(ServiceEditMixin, UpdateView):
    pass


# Удалить категорию
class ServiceDeleteView(ServiceMixin, UrlMixin, DeleteView):
    template_name = 'directory/service/delete.html'