from django.db import models

from django.db.models.signals import pre_save

from django.core.exceptions import ValidationError

# Create your models here.

def validate_name(self, name):
	name = self.name
	obj  = UserCard.objects.filter(slug__iexact=name)

	if obj.exists and obj != self:
		raise ValidationError(
			('{} is already stored'.format(name)),
			params={'name': name},
		)

class UserCard(models.Model):
	CORAZONES	= '♥'
	PICAS 		= '♠'
	TREBOLES 	= '♣'
	DIAMANTES	= '♦'

	PALOS = (
		(CORAZONES, 'Corazones'), 
		(PICAS, 'Picas'),
		(TREBOLES, 'Treboles'),
		(DIAMANTES, 'Diamantes')
		)

	# language = models.CharField(max_length=120, choices=LANGUAGE_CHOICES, default=ENGLISH)
	palo 	 = models.CharField(max_length=120, choices=PALOS, default=CORAZONES)
	number 	 = models.CharField(max_length=120, blank=False, null=True)
	card 	 = models.CharField(max_length=120, blank=True, null=True, editable=False)
	slug 	 = models.SlugField(blank=False, null=False, verbose_name='name')
	message  = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.slug

	def clean(self):
		name = self.slug
		obj  = UserCard.objects.filter(slug__iexact=name)

		if obj.exists() and obj[0] != self:
			raise ValidationError(
				('{} is already stored'.format(name)),
				params={'name': name},
			)

def pre_save_usercard_receiver(sender, instance, *args, **kwargs):
	instance.card = instance.number + instance.palo


pre_save.connect(pre_save_usercard_receiver, sender=UserCard)
