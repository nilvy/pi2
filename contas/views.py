from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def painel_admin(request):
    return render(request, 'contas/painel_admin.html')
