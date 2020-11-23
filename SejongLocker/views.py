#----------------------------------------------------------------------
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
#----------------------------------------------------------------------
def v_index(request):
    return render(request, 'index.html')
#----------------------------------------------------------------------
@login_required
def v_account(request):
    return render(request, 'account.html')
#----------------------------------------------------------------------
@login_required
def v_accountEdit(request):
    if(request.method == 'POST'):
        # change user password
        user = User.objects.get(id=request.user.id)
        user.set_password(request.POST.get('newPassword'))
        user.save()
        # login
        login(request, user)
        return redirect('account')
    else:
        return render(request, 'accountEdit.html')
#----------------------------------------------------------------------
@login_required
def v_logout(request):
    logout(request)
    return redirect('login')
#----------------------------------------------------------------------
def v_join(request):
    if(request.method == 'POST'):
        newUser = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            request.POST.get('password')
        )
        newUser.first_name = request.POST.get('firstName')
        newUser.last_name = request.POST.get('lastName')
        newUser.save()
        login(request, newUser)
        return redirect('account')
    else:
        return render(request, 'join.html')
#----------------------------------------------------------------------
def v_login(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            return render(request, 'err_msg.html', {'err_msg': 'failed to login'})
    else:
        return render(request, 'login.html')
#----------------------------------------------------------------------
