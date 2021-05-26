from django.shortcuts import render
from .models import *
import telepot

token = '1854156164:AAG2UKj7ZPO4RwOb4UsLiwElpo5Wi7LLpmo'
my_id = 1487750916
admin = 1523944378
# Create your views here.

def index(request):
	posts = Posts.objects.all()
	context = {
		'posts':posts,
	}
	if request.method == 'POST':
		t = request.POST['title']
		Ordering.objects.create(title=t)
	return render(request, 'index.html', context)
def contact(request):
	if request.method == 'POST':
		n = request.POST['name']
		s = request.POST['surname']
		p = request.POST['phone']
		m = request.POST['message']
		Contact.objects.create(name=n, surname=s, phone=p, message=m)
		bot = telepot.Bot(token)
		bot.sendMessage(my_id, f"\bIsmi: {n}\nFamilyasi: {s}\nTelefon: {p}\nXabari: {m}")
		bot.sendMessage(admin, f"\bIsmi: {n}\nFamilyasi: {s}\nTelefon: {p}\nXabari: {m}")
	return render(request, 'contact.html')


	