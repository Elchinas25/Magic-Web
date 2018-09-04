from django.shortcuts import render

from django.views.generic import View, ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404

from .models import UserCard

class CustomCard(DetailView):
	template_name = "cards/custom_card.html"

	# def get_object(self, *args, **kwargs):
	# 	# slug = kwargs['slug']
	# 	print(kwargs)
	# 	print(args)
	# 	obj = get_object_or_404(UserCard, name__iexact = slug)

	# 	return obj

	def get_queryset(self):
		return UserCard.objects.all()

	# def get(self, request, *args, **kwargs):
	# 	return render(request, self.template_name, {})
