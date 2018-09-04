from django.shortcuts import render

from django.views.generic import View, ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from django.views.generic.edit import FormView

from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


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
			

class ContactView(FormView):
	template_name = 'Contact/contact.html'
	form_class = ContactForm
	success_url = '/'

	def get(self, request, *args, **kwargs):

		return super().get(self, *args, **kwargs)

	def post(self, *args, **kwargs):
		# print(self.request.POST)

		ctx = self.get_context_data(**kwargs)
		theres_error = False

		mail = self.request.POST['mail']
		number = self.request.POST['number']
		message = self.request.POST['message']
		contact_data = {}

		if len(mail) != 0:
			mail_error = get_mail_errors(mail)
			if mail_error != False:
				ctx['mail_error'] = mail_error
				theres_error = True
			else:
				contact_data['Mail'] = mail
		else:
			contact_data['Mail'] = 'No mail'

		if len(number) != 0:
			number_error = get_number_error(number)
			if number_error != False:
				ctx['number_error'] = number_error
				theres_error = True
			else:
				contact_data['Number'] = number
		else:
			contact_data['Number'] = 'No number'

		general_error = get_general_errors(self.request.POST['mail'], self.request.POST['number'])
		if general_error != False:
			ctx['general_error'] = general_error
			theres_error = True

		if len(message) == 0:
			ctx['message_error'] = _("Blank messages are not permitted")
			theres_error = True

		# if theres_error:
		# 	return render(self.request, self.template_name, ctx)
		# else:
			# cleaned_mail_message = 'Mail: {} \nNumber: {} \nMessage: {}'.format(contact_data['Mail'], contact_data['Number'], message)
			
			# send_mail(
			# 		'New message from web page',
			# 		cleaned_mail_message,
			# 		settings.EMAIL_HOST_USER,
			# 		[str(settings.DEFAULT_TO_EMAIL)],
			# 		fail_silently = False
			# )
		return super().post(self)

	# def form_valid(self, form):
	# 	return super().form_valid(form)

