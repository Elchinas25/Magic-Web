from django.db import models

from django.core.exceptions import ValidationError


def forbid_new_instances(instance, main_instance):
	if instance != main_instance:
		raise ValidationError("You are not allowed to create more instances. Instead, modify the already existing ones.")

def check_text(instance):
	if instance.show_text:
		if instance.text_en == None:
			raise ValidationError({"text_en": "If you want to show text, you'll have to write something you moron."})
		elif instance.text_es == None:
			raise ValidationError({"text_es": "If you want to show text, you'll have to write something you moron."})
def check_hexadecimal(length):
	if length != 6:
		raise ValidationError("Hexadecimal code must be 6 characters long")




class VideoAdmin(models.Model):
	name         = models.CharField(max_length=120, null=True, editable=False)
	video_active = models.BooleanField()
	# controls_on  = models.BooleanField()

	class Meta:
		verbose_name_plural  = 'Video Admin'
	
	@staticmethod
	def get_name_main_admin():
		return "MainVideoAdmin"

	@classmethod
	def get_main_admin(cls):
		main_admin = cls.objects.get(name__iexact=cls.get_name_main_admin())

		return main_admin

	@classmethod
	def is_active(cls):
		return cls.get_main_admin().video_active

	@classmethod
	def controls_active(cls):
		return cls.get_main_admin().controls_on

	def __str__(self):
		return self.name

	def change_active_state(self, set_to):
		self.video_active = set_to
		self.save()

	def clean(self):
		main_video_admin = VideoAdmin.get_main_admin()
		forbid_new_instances(self, main_video_admin)

		main_slider_admin  = SliderAdmin.get_main_admin()
		slider_admin_state = not self.video_active

		main_slider_admin.change_active_state(set_to=slider_admin_state)

class SliderAdmin(models.Model):
	name          	    = models.CharField(max_length=120, null=True, editable=False)
	slider_active 	    = models.BooleanField()
	controls_on   	    = models.BooleanField()
	indicators_color 	= models.CharField(max_length=120, default="ffffff", help_text="Non-active bg color")
	indicators_active_color = models.CharField(max_length=120, default="000000", help_text="Active bg color")
	auto_slider		    = models.BooleanField(default=True)
	slider_interval     = models.IntegerField(default=5000 , help_text='Rate at which images change')
	transition_duration = models.IntegerField(default=500, help_text='Transition time between images')


	class Meta:
		verbose_name_plural  = 'Slider Admin'
	
	@staticmethod
	def get_name_main_admin():
		return "MainSliderAdmin"

	@classmethod
	def get_main_admin(cls):
		main_admin = cls.objects.get(name__iexact=cls.get_name_main_admin())

		return main_admin

	@classmethod
	def is_active(cls):
		return cls.get_main_admin().slider_active

	def __str__(self):
		return self.name


	def change_active_state(self, set_to):
		self.slider_active = set_to
		self.save()

	def clean(self):
		main_slider_admin = SliderAdmin.get_main_admin()
		forbid_new_instances(self, main_slider_admin)

		main_video_admin = VideoAdmin.get_main_admin()
		video_admin_state = not self.slider_active

		main_video_admin.change_active_state(set_to=video_admin_state) # We always want onw to be active and the other not to.
		


class SliderImage(models.Model):
	fkey         = models.ForeignKey(SliderAdmin, on_delete = models.CASCADE, null=True, editable=False)
	name         = models.CharField(max_length=120, null=True)
	active 		 = models.BooleanField()
	img  	     = models.ImageField(upload_to='images/')
	text 		 = models.CharField(max_length=160, blank=True, null=True)
	show_text 	 = models.BooleanField(default=False)


	CENTER		= 'center-align'
	LEFT 		= 'left-align'
	RIGHT 		= 'right-align'

	X_CHOICES = (
		(CENTER, 'Center'), 
		(LEFT, 'Left'),
		(RIGHT, 'Right')
	)

	x_text_pos	 = models.CharField(max_length=120, choices= X_CHOICES, default=CENTER)

	CENTER		= 'c'
	TOP 		= 't'
	BOTTOM 		= 'b'

	Y_CHOICES = (
		(CENTER, 'Center'), 
		(TOP, 'Top'),
		(BOTTOM, 'Bottom')
	)

	y_text_pos	 = models.CharField(max_length=120, choices= Y_CHOICES, default=CENTER)

	long_img	 = models.BooleanField(default=False)

	text_color 	 = models.CharField(max_length=120, default="000000", help_text="Default = BLACK")

	def __str__(self):
		return self.name

	def clean(self):
		if self.active:
			check_text(self)

		check_hexadecimal(len(self.text_color))

			
			

class Video(models.Model):
	fkey         = models.ForeignKey(VideoAdmin, on_delete = models.CASCADE, null=True, editable=False)
	name         = models.CharField(max_length=120, null=True)
	active 		 = models.BooleanField()
	video  	     = models.FileField(upload_to='videos/')
	play_pause_active = models.BooleanField(default=True)
	button_color = models.CharField(max_length=120, default="ffffff")
	# text 		 = models.CharField(max_length=160, blank=True, null=True)
	# text_color 	 = models.CharField(max_length=120, default="000000", help_text="Default = BLACK")
	# fade_away 	 = models.BooleanField(default=True)
	# time_fade 	 = models.IntegerField(blank=True, null=True, default=10)
	# show_text 	 = models.BooleanField(default=False)


	CENTER		= 'center-align'
	LEFT 		= 'left-align'
	RIGHT 		= 'right-align'

	X_CHOICES = (
		(CENTER, 'Center'), 
		(LEFT, 'Left'),
		(RIGHT, 'Right')
	)

	x_text_pos	 = models.CharField(max_length=120, choices= X_CHOICES, default=CENTER)

	CENTER		= 'c'
	TOP 		= 't'
	BOTTOM 		= 'b'

	Y_CHOICES = (
		(CENTER, 'Center'), 
		(TOP, 'Top'),
		(BOTTOM, 'Bottom')
	)

	y_text_pos	 = models.CharField(max_length=120, choices= Y_CHOICES, default=CENTER)

	def __str__(self):
		return self.name

	def clean(self):
		pass
		# check_text(self)
		# check_hexadecimal(len(self.text_color))

class Style(models.Model):
	name 			  = models.CharField(max_length=120, editable=False)

	nav_bg_color      = models.CharField(max_length=120)
	nav_link_color    = models.CharField(max_length=120)
	name_color        = models.CharField(max_length=120)

	drop_bg_color     = models.CharField(max_length=120)
	drop_link_color   = models.CharField(max_length=120)
	mobile_icon_color = models.CharField(max_length=120, default='ffffff')

	name_font_name	  = models.CharField(max_length=120, default='Great+Vibes', help_text='+ symbol for spaces')
	name_font_general = models.CharField(max_length=120, default='cursive')

	statement_font_name		= models.CharField(max_length=120, default='Great+Vibes')
	statement_font_general  = models.CharField(max_length=120, default='cursive')

	diags_font_name	  		= models.CharField(max_length=120, default='Great+Vibes')
	diags_font_general 		= models.CharField(max_length=120, default='cursive')

	gallery_font_name	  	= models.CharField(max_length=120, default='Great+Vibes')
	gallery_font_general 	= models.CharField(max_length=120, default='cursive')



	class Meta:
		verbose_name_plural='Landing Page Admin'

	@staticmethod
	def get_name_main_admin():
		return "MainStylesAdmin"

	@classmethod
	def get_main_admin(cls):
		main_admin = cls.objects.get(name__iexact=cls.get_name_main_admin())

		return main_admin

	def __str__(self):
		return self.name

	def clean(self):
		main_styles_admin = Style.get_main_admin()
		forbid_new_instances(self, main_styles_admin)

		check_hexadecimal(len(self.nav_bg_color))
		check_hexadecimal(len(self.nav_link_color))
		check_hexadecimal(len(self.name_color))
		check_hexadecimal(len(self.drop_bg_color))
		check_hexadecimal(len(self.drop_link_color))
		check_hexadecimal(len(self.mobile_icon_color))
		# check_hexadecimal(len(self.nav_bg_color))

class DigonalStyle(models.Model):
	name 			      = models.CharField(max_length=120, editable=False, default="MainDiagonalAdmin")

	first_sec_height	  = models.IntegerField(default=300)
	first_sec_mob_height  = models.IntegerField(default=300)
	first_sec_bg_color    = models.CharField(max_length=120, default='000000')
	statement_color 	  = models.CharField(max_length=120, default='ffffff')
	statement 			  = models.CharField(max_length=120)

	RIGTH		= 'r'
	LEFT 		= 'l'

	# SIDE_CHOICES = (
	# 	(RIGTH, 'Right'), 
	# 	(LEFT, 'Left'),
	# )

	second_sec_height	  = models.IntegerField(default=400)
	second_sec_mob_height = models.IntegerField(default=300)
	second_sec_img 		  = models.ImageField(upload_to='images/', blank=True, null=True)
	second_sec_rounded_img = models.BooleanField(default=False)
	second_sec_img_width  = models.IntegerField(default=250)
	second_sec_img_height = models.IntegerField(default=350)
	
	second_sec_bg_color   = models.CharField(max_length=120, default='000000')
	second_sec_title       = models.CharField(max_length=120, blank=True, null=True)
	second_sec_title_color = models.CharField(max_length=120, default='ffffff')
	second_sec_text       = models.CharField(max_length=120, blank=True, null=True)
	second_sec_text_color = models.CharField(max_length=120, default='ffffff')

	third_sec_height	  = models.IntegerField(default=350)
	third_sec_mob_height  = models.IntegerField(default=300)
	third_sec_img 		  = models.ImageField(upload_to='images/', blank=True, null=True)
	third_sec_rounded_img = models.BooleanField(default=False)
	third_sec_img_width   = models.IntegerField(default=300)
	third_sec_img_height  = models.IntegerField(default=400)
	
	third_sec_bg_color    = models.CharField(max_length=120, default='000000')
	third_sec_title       = models.CharField(max_length=120, blank=True, null=True)
	third_sec_title_color = models.CharField(max_length=120, default='ffffff')
	third_sec_text        = models.CharField(max_length=120, blank=True, null=True)
	third_sec_text_color  = models.CharField(max_length=120, default='ffffff')

	fourth_sec_height	  = models.IntegerField(default=350)
	fourth_sec_mob_height = models.IntegerField(default=300)
	fourth_sec_img 		  = models.ImageField(upload_to='images/', blank=True, null=True)
	fourth_sec_rounded_img = models.BooleanField(default=False)
	fourth_sec_img_width   = models.IntegerField(default=300)
	fourth_sec_img_height  = models.IntegerField(default=400)
	# fourth_sec_bg_effect   = models.BooleanField(default=False, help_text="If set to True, the image won't be sized in order to achieve the effect")
	fourth_sec_bg_color    = models.CharField(max_length=120, default='000000')
	fourth_sec_title       = models.CharField(max_length=120, blank=True, null=True)
	fourth_sec_title_color = models.CharField(max_length=120, default='ffffff')
	fourth_sec_text        = models.CharField(max_length=120, blank=True, null=True)
	fourth_sec_text_color  = models.CharField(max_length=120, default='ffffff')

	class Meta:
		verbose_name_plural='Diagonals Admin'

	@staticmethod
	def get_name_main_admin():
		return "MainDiagonalAdmin"

	@classmethod
	def get_main_admin(cls):
		main_admin = cls.objects.get(name__iexact=cls.get_name_main_admin())

		return main_admin

	def __str__(self):
		return self.name

	def clean(self):
		main_diags_admin = DigonalStyle.get_main_admin()
		forbid_new_instances(self, main_diags_admin)

		check_hexadecimal(len(self.first_sec_bg_color))
		check_hexadecimal(len(self.statement_color))
		check_hexadecimal(len(self.second_sec_text_color))
		check_hexadecimal(len(self.third_sec_text_color))

	



		



















