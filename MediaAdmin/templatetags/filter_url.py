from django import template

register = template.Library()

GALLERY_EN = "gallery"
GALLERY_ES = "galeria"
CARDS_EN = "cards"
CARDS_ES = "cartas"


def change(value, set_to):
	if value[2] != set_to:
		return value
	
	if value[2] == "n": 
		if GALLERY_EN in value:
			trans_value = value.replace(GALLERY_EN, GALLERY_ES)
			new_value = "/es" + trans_value[3:]
		elif CARDS_EN in value:
			trans_value = value.replace(CARDS_EN, CARDS_ES)
			new_value = "/es" + trans_value[3:]
		else:
			new_value = "/es" + value[3:]
 
	else: 
		if GALLERY_ES in value:
			trans_value = value.replace(GALLERY_ES, GALLERY_EN)
			new_value = "/en" + trans_value[3:]
		elif CARDS_ES in value:
			trans_value = value.replace(CARDS_ES, CARDS_EN)
			new_value = "/en" + trans_value[3:]
		else:
			new_value = "/en" + value[3:]
		
	

	return new_value

register.filter('changeURL', change)

def get_indexes(value, qs):
	index_counter = 0

	for img in qs:
		if img == value:
			value_index = index_counter
			break

		index_counter += 1

	last_index = len(qs) - 1

	if value_index == 0:
		return (value_index + 1, last_index)

	elif value_index == last_index:
		return (0, value_index - 1)

	return (value_index + 1, value_index - 1)

register.filter('get_indexes', get_indexes)

STATIC_NAVBAR = [GALLERY_ES, GALLERY_EN]

def static_navbar(value):
	is_static = False

	for var in STATIC_NAVBAR:
		if var in value:
			is_static = True

	return is_static
		

register.filter('static_navbar', static_navbar)

def is_home_view(value):
	print(value)
	if value == "/en/" or value == "/es/": 
		print(True)
		return True
	else: return False

register.filter('is_home_view', is_home_view)

def out_plus_sign(value):
	spaced_val = value.replace("+", " ")
	print(spaced_val)

	return spaced_val

register.filter('out_plus_sign', out_plus_sign)