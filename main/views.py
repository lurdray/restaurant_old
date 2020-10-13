from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import *
from django.contrib import messages

# Create your views here.

def index(request):
	
	settings = Setting.objects.all()
	sliders = Slider.objects.all()
	mainmenus = MainMenu.objects.all().order_by('-pub_date')[:5]
	mainbs = MainB.objects.all().order_by('-pub_date')
	dessertmenus = DessertMenu.objects.all().order_by('-pub_date')
	dessertbs = DessertB.objects.all().order_by('-pub_date')
	drinkmenus = DrinkMenu.objects.all().order_by('-pub_date')
	drinkbs = DrinkB.objects.all().order_by('-pub_date')
	context = {"mainmenus": mainmenus,
				"mainbs":mainbs, 
				"dessertmenus":dessertmenus,
				"dessertbs":dessertbs, 
				'drinkmenus':drinkmenus,
				"drinkbs":drinkbs, 
				"sliders":sliders,
				"settings":settings,

				}
	#messages.success(request, "Your message has been delivered thank you")
	return render(request, "main/index.html", context)

def about(request):
	settings = Setting.objects.all()
	sliders = Slider.objects.all().order_by('?')[:1]
	#products_picked = Products.objects.all().order_by('?')[:8] #random
	context = {"sliders":sliders, "settings":settings}
	return render(request, "main/about.html", context)



def specialties(request):
	context = {}
	return render(request,"main/specialties.html", context)

def contact(request):
	settings = Setting.objects.all()
	sliders = Slider.objects.all().order_by('?')[:1]

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')


		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message)
		contact_model.save()
		messages.success(request, "Your message has been delivered")
		return HttpResponseRedirect('/contact')

	else:

	
		response = ""


	context = {"response": response, "sliders":sliders, "settings":settings}
	return render(request, "main/contact.html", context)

def reservation(request):
	settings = Setting.objects.all()
	sliders = Slider.objects.all().order_by('?')[:1]
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		number = request.POST.get('number')
		date = request.POST.get('date')
		time = request.POST.get('time')


		reservation = Reservation.objects.create(name=name, email=email, phone=phone, number=number, date=date, time=time,)
		reservation.save()
		messages.success(request, "Your message has been delivered")
		return HttpResponseRedirect('/reservation')

	else:

	
		response = ""
	context = {"sliders":sliders, "settings":settings}
	return render(request, 'main/reservation.html', context)

def mainmenu(request):
	mainmenus = MainMenu.objects.all().order_by('-pub_date')[:5]
	mainbs = MainB.objects.all().order_by('-pub_date')
	dessertmenus = DessertMenu.objects.all().order_by('-pub_date')
	dessertbs = DessertB.objects.all().order_by('-pub_date')
	drinkmenus = DrinkMenu.objects.all().order_by('-pub_date')
	drinkbs = DrinkB.objects.all().order_by('-pub_date')
	settings = Setting.objects.all()
	sliders = Slider.objects.all().order_by('?')[:1]
	context = {"mainmenus": mainmenus,
				"mainbs":mainbs, 
				"dessertmenus":dessertmenus,
				"dessertbs":dessertbs, 
				'drinkmenus':drinkmenus,
				"drinkbs":drinkbs,
				"sliders": sliders,
				"settings": settings
				}
	return render(request, 'main/menu.html', context)
