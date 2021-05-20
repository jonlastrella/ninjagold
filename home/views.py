from django.shortcuts import render, redirect
import random

# Create your views here.

GOLD_MAP = {
    'farm': (10, 20),
    'cave': (10, 20),
    'house': (10, 20),
    'casino': (10, 20)
}


def index(request):
    if not "gold" in request.session or "activities" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')


def reset(request):
    request.session.clear()
    return redirect('/')


def getGold(request):
    if request.method == 'GET':
        return redirect('/')

    building_name = request.POST['building']
    building = GOLD_MAP[building_name]
    building_name_upper = building_name[0].upper() + building_name[1:]

    curr_gold = random.randint(building[0], building[1])
    result = 'earn'
    message = f"Earned {curr_gold} from the {building_name_upper}!"

    if building_name == 'casino':
        if random.randint(0, 1) > 0:
            message = f"Entered a {building_name_upper} and lost {curr_gold} gold...Ouch.. "
            curr_gold = curr_gold * -1
            result = 'lose'

    request.session['gold'] += curr_gold
    request.session['activities'].append(
        {"message": message, "result": result})
    return redirect('/')
