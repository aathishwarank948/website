
from django.shortcuts import render

def home(request):
	return render(request, 'webapp/home.html')

def menu(request):
	food_items = [
		{'name': 'Margherita Pizza', 'description': 'Classic delight with 100% real mozzarella cheese', 'price': 199, 'image': '/static/webapp/food1.jpg'},
		{'name': 'Farmhouse Pizza', 'description': 'Delightful combination of onion, capsicum, tomato & grilled mushroom', 'price': 199, 'image': '/static/webapp/food2.jpg'},
		{'name': 'Veggie Burger', 'description': 'Loaded with fresh veggies and cheese', 'price': 99, 'image': '/static/webapp/food3.jpg'},
		{'name': 'Chicken Burger', 'description': 'Juicy chicken patty with lettuce and mayo', 'price': 249, 'image': '/static/webapp/food4.jpg'},
		{'name': 'Pasta Alfredo', 'description': 'Creamy Alfredo sauce with penne pasta', 'price': 469, 'image': '/static/webapp/food5.jpg'},
		{'name': 'Pasta Arrabiata', 'description': 'Spicy tomato sauce with penne pasta', 'price': 149, 'image': '/static/webapp/food6.jpg'},
		{'name': 'Caesar Salad', 'description': 'Fresh lettuce, parmesan, croutons, Caesar dressing', 'price': 799, 'image': '/static/webapp/food7.jpg'},
		{'name': 'Greek Salad', 'description': 'Cucumber, tomato, feta cheese, olives', 'price': 549, 'image': '/static/webapp/food8.jpg'},
		{'name': 'Grilled Chicken', 'description': 'Tender grilled chicken breast', 'price': 899, 'image': '/static/webapp/food9.jpg'},
		{'name': 'Paneer Tikka', 'description': 'Spicy grilled paneer cubes', 'price': 899, 'image': '/static/webapp/food10.jpg'},
		{'name': 'Chocolate Cake', 'description': 'Rich and moist chocolate cake', 'price': 499, 'image': '/static/webapp/food11.jpg'},
		{'name': 'Ice Cream Sundae', 'description': 'Vanilla ice cream with chocolate sauce and nuts', 'price': 399, 'image': '/static/webapp/food12.jpg'},
	]
	return render(request, 'webapp/menu.html', {'food_items': food_items})

def administration(request):
	admins = [
		{'name': 'Aathishwaran K', 'designation': 'Founder', 'photo': '/static/webapp/admin1.jpg'},
		{'name': 'Swetha K', 'designation': 'Head Chef', 'photo': '/static/webapp/admin2.jpg'},
		{'name': 'Ashwin baalaji V K', 'designation': 'Sous Chef', 'photo': '/static/webapp/admin3.jpg'},
		{'name': 'Indhu V', 'designation': 'Restaurant Supervisor', 'photo': '/static/webapp/admin4.jpg'},
		{'name': 'Harish K', 'designation': 'Marketing Manager', 'photo': '/static/webapp/admin5.jpg'},
		{'name': 'Elon Musk mama', 'designation': 'tea supplier', 'photo': '/static/webapp/admin6.jpg'},
	]
	return render(request, 'webapp/administration.html', {'admins': admins})

def contact(request):
	contact_info = {
		'address': '123 TVK STREET, DOLAKPUR,JUPYTER',
		'phone': '9876543210',
		'email': 'idlywiththakkalithokku@myrestaurant.com',
	}
	return render(request, 'webapp/contact.html', {'contact': contact_info})
