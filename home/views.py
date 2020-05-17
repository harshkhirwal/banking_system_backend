from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
	context = {}
	context['str'] = "hey there"
	return render(request, "home/home.html", context)
