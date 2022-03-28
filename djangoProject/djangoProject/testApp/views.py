from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Comida


def about(request):
	return render(request, 'testApp/about.html', {'title':'About'})

class ComidaListView(ListView):
	ListView.model = Comida
	ListView.template_name = 'testApp/home.html'
	ListView.context_object_name = 'comidas'

class ComidaCreateView(CreateView):
	model = Comida
	fields = ['name','description']
	success_url = '../'

class ComidaDeleteView(DeleteView):
	model = Comida
	fields = ['name','description']
	success_url =  '../../../'

class ComidaUpdateView(UpdateView):
	model = Comida
	fields = ['name','description']
	success_url =  '../../../'