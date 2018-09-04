from django.db import models

from django.core.exceptions import ValidationError

from django.db.models.signals import pre_save


from django.core.exceptions import ValidationError


def forbid_new_instances(instance, main_instance):
	if instance != main_instance:
		raise ValidationError("You are not allowed to create more instances. Instead, modify the already existing ones.")

class Event(models.Model):
	title		= models.CharField(max_length=120, blank=False, null=False)
	event_title_color = models.CharField(max_length=120, default='ffffff')
	description = models.TextField()
	active 		= models.BooleanField(default=True)
	position    = models.IntegerField(blank=False, null=False)
	main_event  = models.BooleanField(default=False)

	def __str__(self):
		if self.main_event:
			return '(Main Event) Position {}, {} imgs: "{}" '.format(self.position, self.image_set.all().count(), self.title)
		return 'Position {}, {} imgs: "{}" '.format(self.position, self.image_set.all().count(), self.title)

	def clean(self):
		try:
			same_position = Event.objects.filter(active=True).filter(position=self.position)[0]
		except IndexError:
			pass
		else:
			if same_position != self:
				raise ValidationError({"position": "There is already an event with that position."})

		if self.main_event and not self.active:
			raise ValidationError({"active": "You shouldn't set a main event if it is not active."})
	
	def get_active_imgs(self):
		return self.image_set.filter(active=True)
		

class Image(models.Model):
	event 		 = models.ForeignKey(Event, on_delete=models.CASCADE)
	name 		 = models.CharField(max_length=120, blank=True, null=True)
	img  	     = models.ImageField(upload_to='images/')
	active 		 = models.BooleanField()

	def __str__(self):
		return self.name



# class GalleryStyle(models.Model):
# 	name          	    = models.CharField(max_length=120, null=True, editable=False, default="MainGalleryAdmin")
# 	show_gallery 	= models.BooleanField()

# 	def __str__(self):
# 		return GalleryStyle.get_name_main_admin()

# 	@staticmethod
# 	def get_name_main_admin():
# 		return "MainGalleryAdmin"

# 	@classmethod
# 	def get_main_admin(cls):
# 		main_admin = cls.objects.get(name__iexact=cls.get_name_main_admin())

# 		return main_admin

# 	@classmethod
# 	def show_gallery(cls):
# 		return cls.get_main_admin().show_gallery

# 	def clean(self):
# 		main_gallery_admin = GalleryStyle.get_main_admin()
# 		# forbid_new_instances(self, main_gallery_admin)

class GalleryStyleAdmin(models.Model):
	name          	= models.CharField(max_length=120, null=True, editable=False, default="MainGalleryAdmin")
	# show_gallery 	= models.BooleanField(default=True)
	gallery_active  = models.BooleanField(default=True)
	gallery_bg_color = models.CharField(max_length=120, default='808080')

	class Meta:
		verbose_name_plural = 'Gallery styles'

	def __str__(self):
		return self.name

	@staticmethod
	def get_name_main_admin():
		return "MainGalleryAdmin"

	@classmethod
	def get_main_admin(cls):
		main_admin = cls.objects.get(name__iexact=cls.get_name_main_admin())

		return main_admin

	@classmethod
	def show_gallery(cls):
		return cls.get_main_admin().gallery_active

	def clean(self):
		main_gallery_admin = GalleryStyleAdmin.get_main_admin()
		forbid_new_instances(self, main_gallery_admin)


def pre_save_event_receiver(sender, instance, *args, **kwargs):
	print("helllo")
	if instance.main_event:
		print("yes")
		try:
			prev_main_event = Event.objects.get(main_event=True)
			print(prev_main_event)
			prev_main_event.main_event = False
			prev_main_event.save()

		except:
			pass


pre_save.connect(pre_save_event_receiver, sender=Event)
