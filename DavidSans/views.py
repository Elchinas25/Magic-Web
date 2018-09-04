from django.shortcuts import render

from django.views.generic import View, ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from django.views.generic.edit import FormView

from Contact.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

from MediaAdmin.models import Video, SliderImage, SliderAdmin, VideoAdmin, Style, DigonalStyle

from Gallery.models import Event, Image, GalleryStyleAdmin

def get_mail_errors(mail):
	if '@' not in mail: 
		return _('The mail should contain "@"')
	elif '.' not in mail:
		return _('The mail should contain "."')
	else:
		return False

def get_number_error(number):
	for n in number:
		try:
			current = int(n)
		except:
			return _('"{}" is not a number. Please try again').format(n)
		else:
			if len(number) < 9:
				return _('The number is too short. It shoud contain, at least, 9 numbers.')
			else:
				return False

def get_general_errors(mail, number):
	if len(number) == 0 and len(mail) == 0:
		return _('We need either a mail or a number to contact you.')
	else:
		return False




# class HomeView(View):
# 	template_name = 'home_view.html'

# 	def get(self, request, *args, **kwargs):
# 		ctx = {}
# 		ctx['hola'] = 'hola'

# 		if VideoAdmin.is_active():
# 			print("Video")
# 			video = Video.objects.filter(active=True)[0]
# 			ctx['video_active'] = True
# 			ctx['video']		= video
# 		else:
# 			slider_imgs = SliderImage.objects.filter(active=True)
# 			print("Helloooo")
# 			print(slider_imgs)
# 			ctx['slider_imgs'] = slider_imgs

# 		return render(self.request, self.template_name, ctx)

	




class HomeView(FormView):
	template_name = 'mat_home_final.html'
	form_class = ContactForm
	success_url = '/'

	def get_context_data(self, *args, **kwargs):
		ctx = super().get_context_data(**kwargs)

		if VideoAdmin.is_active():
			video = Video.objects.filter(active=True)[0]
			ctx['video_active'] = True
			ctx['video']		= video
			

		ctx['slider_admin'] = SliderAdmin.get_main_admin()
		

		slider_imgs = SliderImage.objects.filter(active=True)
		short_imgs	= slider_imgs.filter(long_img=False)
		long_imgs	= slider_imgs.filter(long_img=True)

		if len(short_imgs) == 0:
			short_imgs = SliderImage.objects.filter(long_img=False)[0:2]
			if len(short_imgs) == 0:
				short_imgs = SliderImage.objects.filter(long_img=True)[0:2]



		if len(long_imgs) == 0:
			long_imgs = SliderImage.objects.filter(long_img=True)[0:2]
			if len(long_imgs) == 0:
				long_imgs = SliderImage.objects.filter(long_img=False)[0:2]

		ctx['short_imgs'] = short_imgs
		ctx['long_imgs'] = long_imgs



		style_admin = Style.get_main_admin()
		ctx['styles'] = style_admin

		diag_admin = DigonalStyle.get_main_admin()
		ctx['diagonals'] = diag_admin

		gallery_admin = GalleryStyleAdmin.get_main_admin()
		ctx['gallery'] = gallery_admin


		try:
			main_event = Event.objects.get(main_event = True)
			theres_event = True

		except:
			theres_event = False

		ctx['theres_event'] = theres_event
		if theres_event:
			ctx['main_event'] = main_event

		FIELD_REQUIRED = _("This field is required")
		NUM_SHORT = _("The number is too short")
		NUM_LARGE = _("The number is too large")
		MAIL_INCORRECT = _("Mail not correct")
		TOO_SHORT = _('Too short to be a valid mail or number')

		LESS_THAN = _("The message should contain less than")
		CHARS = _("characters")

		ALBUM = _("Image %1 of %2")
		CLICK = _("Click the right half of the image to move forward.")

		ctx['field_required_msg'] = FIELD_REQUIRED
		ctx['num_short_msg'] = NUM_SHORT
		ctx['num_large_msg'] = NUM_LARGE
		ctx['mail_incorrect_msg'] = MAIL_INCORRECT
		ctx['too_short_msg'] = TOO_SHORT

		ctx['less_than_msg'] = LESS_THAN
		ctx['chars_msg'] = CHARS

		ctx['album_msg'] = ALBUM
		ctx['click_msg'] = CLICK




		return ctx

	def form_valid(self, form):
		

		mail_num = self.request.POST['mail_or_num']
		name = self.request.POST['name']

		try:
			message = self.request.POST['message']
		except:
			message = 'No message'

		
			
			

		cleaned_mail_message = 'Mail/Num: {} \n\nName: {} \n\nMessage: {}'.format(mail_num, name, message)

		send_mail(
					'New message from web page',
					cleaned_mail_message,
					settings.EMAIL_HOST_USER,
					[str(settings.DEFAULT_TO_EMAIL)],
					fail_silently = False
		)



		return super().form_valid(form)




















	# def get(self, request, *args, **kwargs):
	# 	ctx = {}
	# 	ctx['hola'] = 'hola'

	# 	if VideoAdmin.is_active():
	# 		print("Video")
	# 		video = Video.objects.filter(active=True)[0]
	# 		ctx['video_active'] = True
	# 		ctx['video']		= video
	# 	else:
	# 		slider_imgs = SliderImage.objects.filter(active=True)
	# 		print("Helloooo")
	# 		print(slider_imgs)
	# 		ctx['slider_imgs'] = slider_imgs

	# 	return render(self.request, self.template_name, ctx)


	# def get_context_data(self, *args, **kwargs):
	# 	ctx = {}

	# 	if VideoAdmin.is_active():
	# 		print("Video")
	# 		video = Video.objects.filter(active=True)[0]
	# 		ctx['video_active'] = True
	# 		ctx['video']		= video
	# 	else:
	# 		slider_imgs = SliderImage.objects.filter(active=True)
	# 		ctx['slider_imgs'] = slider_imgs

	# 	form = ContactForm(self.request.POST)
	# 	ctx['form'] = form

	# 	return ctx

	# def form_valid(self, form):
	# 	print('hi', form)
	# 	return super().form_valid(form)

	# def post(self, *args, **kwargs):
	# 	# print(self.request.POST)

	# 	ctx = self.get_context_data(**kwargs)
	# 	theres_error = False

	# 	mail = self.request.POST['mail']
	# 	number = self.request.POST['number']
	# 	message = self.request.POST['message']
	# 	contact_data = {}

	# 	if len(mail) != 0:
	# 		mail_error = get_mail_errors(mail)
	# 		if mail_error != False:
	# 			ctx['mail_error'] = mail_error
	# 			theres_error = True
	# 		else:
	# 			contact_data['Mail'] = mail
	# 	else:
	# 		contact_data['Mail'] = 'No mail'

	# 	if len(number) != 0:
	# 		number_error = get_number_error(number)
	# 		if number_error != False:
	# 			ctx['number_error'] = number_error
	# 			theres_error = True
	# 		else:
	# 			contact_data['Number'] = number
	# 	else:
	# 		contact_data['Number'] = 'No number'

	# 	general_error = get_general_errors(self.request.POST['mail'], self.request.POST['number'])
	# 	if general_error != False:
	# 		ctx['general_error'] = general_error
	# 		theres_error = True

	# 	if len(message) == 0:
	# 		ctx['message_error'] = _("Blank messages are not permitted")
	# 		theres_error = True

	# 	# if theres_error:
	# 	# 	return render(self.request, self.template_name, ctx)
	# 	# else:
	# 	# 	cleaned_mail_message = 'Mail: {} \nNumber: {} \nMessage: {}'.format(contact_data['Mail'], contact_data['Number'], message)
			
	# 	# 	send_mail(
	# 	# 			'New message from web page',
	# 	# 			cleaned_mail_message,
	# 	# 			settings.EMAIL_HOST_USER,
	# 	# 			[str(settings.DEFAULT_TO_EMAIL)],
	# 	# 			fail_silently = False
	# 	# 	)
	# 	return super().post(self)







# class HomeView(View):
# 	template_name = 'home_view.html'

# 	def get(self, request, *args, **kwargs):
# 		return render(self.request, self.template_name, {})

# 	def get_context_data(self, *args, **kwargs):
# 		ctx = self.get_context_data(**kwargs)
# 		ctx['hola'] = 'hola'

# 		if VideoAdmin.is_active():
# 			print("Video")
# 			video = Video.objects.filter(active=True)[0]
# 			ctx['video_active'] = True
# 			ctx['video']		= video
# 		else:
# 			slider_imgs = SliderImage.objects.filter(active=True)
# 			print("Helloooo")
# 			print(slider_imgs)
# 			ctx['slider_imgs'] = slider_imgs

# 		return ctx



