from django.shortcuts import render

def home(request):
	return render(request, "vicevercsa.html")

def reverse(request):
	user_text = request.GET["usertext"]
	reversed_text = user_text[::-1]
	n = len(user_text.split())
	return render(request, "reverse.html", {"usertext" : user_text, "reversedtext" : reversed_text, "n" : n})