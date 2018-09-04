from django.shortcuts import render

from django.views.generic import View, ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Event, Image
from MediaAdmin.models import Style

class EventListView(ListView):
	template_name = "event_list.html"
	
	def get_queryset(self, *args, **kwkargs):
		print(Event.objects.filter(active=True).order_by('position'))
		return Event.objects.filter(active=True).order_by('position')

	def get_context_data(self):
		ctx = super().get_context_data()
		ctx['images'] = Event.objects.all()[0].image_set.all()

		style_admin = Style.get_main_admin()
		ctx['styles'] = style_admin

		return ctx

