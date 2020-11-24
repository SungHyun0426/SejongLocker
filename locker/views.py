from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Locker

def v_index(request):
    return render(request, 'locker/index.html')

def v_showLockers(request, targetGroup):
    lockers = list(
        Locker.objects
            .filter(lockerId__contains=targetGroup)
                .order_by('lockerId')
                    .values('lockerId', 'availability'))
    col = len(lockers)//6
    lockers = [lockers[i:i+col] for i in range(0, len(lockers), col)]
    context = {'lockers': lockers}

    return render(request, 'locker/lockers.html', context)

def v_showLocker(request, targetId):
    locker = Locker.objects.get(lockerId__exact=targetId)
    context = {'locker': locker}

    return render(request, 'locker/locker.html', context)
