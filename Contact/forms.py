from django import forms

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError



class ContactForm(forms.Form):
	mail_or_num = forms.CharField(required=False, label=_('Mail/Number'))
	name        = forms.CharField(required=False, label=_('Name/Company'))
	message     = forms.CharField(required=False, max_length=500, label=_('Message'))

	# def clean_mail_or_num(self):
	# 	mail_or_num = self.cleaned_data['mail_or_num']

	# 	if '@' not in mail_or_num:
	# 		raise ValidationError( _('The mail should contain "@"'))

	# 	return mail_or_num

	# def clean(self):
	# 	data = self.cleaned_data

	# 	mail    = data['mail']
	# 	number  = data['number']
	# 	message = data['message']

	# 	len_num = len(number)

	# 	if len_num == 0 and len(mail) == 0:
	# 		raise ValidationError(_('We need either a mail or a number to contact you.'),
	# 			)

	# 	if len(mail) != 0:
	# 		if '@' not in mail: 
	# 			raise ValidationError({"mail": _('Theeeee mail should contain "@"')}
	# 			)
	# 	if len_num != 0:
	# 		for n in number:
	# 			try:
	# 				current = int(n)
	# 			except:
	# 				raise ValidationError(_('"{}" is not a number. Please try again').format(n)
	# 				)
	# 			else:
	# 				if len_num < 9:
	# 					raise ValidationError(_('The number is too short. It shoud contain, at least, 9 numbers.'),
	# 					)

	# 	if len(message) < 3:
	# 		raise ValidationError(_('The message is too short. Write at least 4 characters'))
	# 	elif len(message) > 800:
	# 		raise ValidationError(_('The message is too long. Max is 800 characters'))

	# 	return super().clean()


