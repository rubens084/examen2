# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import carModelForm
from .models import car
from .mixin import FormUserNeededMixin

# Create your views here.

def home(request):
    tweets = car.objects.all()

    return render(request, "home.html", context={"msg":"hola django", "tweets":tweets})


# Need to start crud

# Create form
class carCreateView(LoginRequiredMixin,FormUserNeededMixin, CreateView):
    form_class = carModelForm
    template_name = "tweets/create_view.html"
    success_url = "/car/list"
    login_url = "/admin"

class carUpdateView(UpdateView):
    queryset = car.objects.all()
    form_class = carModelForm
    template_name = "tweets/update_view.html"
    success_url = "/car/list"

class carDeleteView(LoginRequiredMixin, DeleteView):
    model = car
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("carList")


class carDetailView(DetailView):
    template_name = "tweets/car_detail.html"
    queryset = car.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return car.objects.get(id=id)


class carListView(ListView):
    template_name = "tweets/car_list.html"
    # queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = car.objects.all()
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(make__icontains=query) |
                            Q(Type__icontains=query)
                          )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(carListView, self).get_context_data(*args, **kwargs)
        print context
        context['create_form'] = carModelForm()
        context['create_url'] = reverse_lazy("carCreate")
        return context
