from django.shortcuts import render, redirect
from .models import Finch, Trinket
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(
        request, "finches/detail.html", {"finch": finch, "feeding_form": feeding_form}
    )


class FinchList(ListView):
    model = Finch
    template_name = "finches/index.html"


class FinchCreate(CreateView):
    model = Finch
    fields = "__all__"
    success_url = "/finches/"


class FinchUpdate(UpdateView):
    model = Finch
    fields = ["species", "description", "age"]


class FinchDelete(DeleteView):
    model = Finch
    success_url = "/finches/"

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


class TrinketList(ListView):
    model = Trinket

class TrinketDetail(DetailView):
    model = Trinket

class TrinketCreate(CreateView):
    model = Trinket
    fields = '__all__'
    success_url = '/trinkets/'

class TrinketUpdate(UpdateView):
    model = Trinket
    fields = ['name', 'color']

class TrinketDelete(DeleteView):
    model = Trinket
    success_url = '/trinkets/'
