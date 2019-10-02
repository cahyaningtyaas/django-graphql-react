from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish
from .serializers import DishSerializer
from rest_framework import generics
from django.views.generic import ListView, DetailView
from .forms import DishForm

# Create your views here.
class DishListCreate(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishIndexView(ListView):
    template_name = 'dish/index.html'
    context_object_name = 'dish_list'
    def get_queryset(self):
        return Dish.objects.all()

class DishDetailView(DetailView):
    template_name = 'dish/detail.html'
    model = Dish

def dishview(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = PostForm()
    return render(request,'dish/dish.html',{'form':form})

def dishedit(request, template_name='dish/edit.html'):
    dish= get_object_or_404(Dish, pk = pk)
    form = PostForm(request.POST or None, instance=dish)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def dishdelete(request, template_name='dish/confirm_delete.html'):
    dish = get_object_or_404(Dish, pk = pk)
    if request.method=='POST':
        dish.delete()
        return redirect('index')
    return render(request, template_name, {'object':dish})
