from django.shortcuts import render

def index(request):
    return render(request, "coins/index.html", 
    {'title': 'All Coins Price'})
