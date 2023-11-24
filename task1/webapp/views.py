from django.shortcuts import render, redirect
from .cat import Cat

cat = Cat()

def main(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        cat.set_name(cat_name)
        return redirect('stats')
    return render(request, 'main.html')

def views(request):
    cat.check_state()
    return render(request, 'views.html', {'cat': cat})

def choose(request):
    if request.method == 'POST':
        command = request.POST.get('choose')
        if command == 'feed':
            cat.feed()
            cat.check_state()
        elif command == 'play':
            cat.play()
            cat.check_state()
        elif command == 'sleep':
            cat.sleep()
            cat.check_state()
    return redirect('stats')


