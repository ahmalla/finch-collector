from django.shortcuts import render, redirect
from .models import Finch, Trinket
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import FeedingForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

@login_required
def finches_index(request):
    finches = Finch.objects.filter(user=request.user)
    return render(request, "finches/index.html", {"finches": finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.trinkets.all().values_list("id")
    trinkets_finch_doesnt_have = Trinket.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(
        request,
        "finches/detail.html",
        {
            "finch": finch,
            "feeding_form": feeding_form,
            "trinkets": trinkets_finch_doesnt_have,
        },
    )


class FinchList(ListView):
    model = Finch
    template_name = "finches/index.html"


class FinchCreate(CreateView):
    model = Finch
    fields = ["name", "species", "description", "age"]
    success_url = "/finches/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
    return redirect("detail", finch_id=finch_id)

def remove_trinket (request, finch_id, trinket_id):
    Finch.objects.get(id=finch_id).trinkets.remove(trinket_id)
    return redirect('detail', finch_id=finch_id)


class TrinketList(ListView):
    model = Trinket


class TrinketDetail(DetailView):
    model = Trinket


class TrinketCreate(CreateView):
    model = Trinket
    fields = "__all__"
    success_url = "/trinkets/"


class TrinketUpdate(UpdateView):
    model = Trinket
    fields = ["name", "color"]


class TrinketDelete(DeleteView):
    model = Trinket
    success_url = "/trinkets/"


def assoc_trinket(request, finch_id, trinket_id):
    Finch.objects.get(id=finch_id).trinkets.add(trinket_id)
    return redirect('detail', finch_id=finch_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Sign Up not valid - Please Try Again'
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'registration/signup.html', context)