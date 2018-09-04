from django.shortcuts import render

from django.views.generic import View, ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Video, SliderImage, SliderAdmin, VideoAdmin

class HomeView(View):
	template_name = 'home_view.html'

	def get(self, request, *args, **kwargs):
		return super().get(request, *args, **kwargs)
		# return render(self.request, self.template_name, ctx)

	def get_context_data(self, *args, **kwargs):
		ctx = self.get_context_data(**kwargs)
		print("Locococococococo")

		if VideoAdmin.is_active():
			video = Video.objects.filter(active=True)[0]
			ctx['video_active'] = True
			ctx['video']		= video
			print("e")
		else:
			slider_imgs = SliderImage.objects.filter(active=True)
			short_imgs	= slider_imgs.filter(long_img=False)
			long_imgs	= slider_imgs.filter(long_img=True)

			ctx['short_imgs'] = short_imgs
			ctx['long_imgs'] = long_imgs
			print('a', long_imgs)

		return ctx



