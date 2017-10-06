from django.shortcuts import render, HttpResponseRedirect;
from django.http import HttpResponse;
from . models import blocks, transaction, audit_khasra, khasra, print_count;
from django.contrib.auth.decorators import login_required;
from . forms import UserForm, KhasraForm;
import os;

# Create your views here.

# Function to show the kahasra templeate to the user

@login_required(login_url='/login')
def getKhasraTemplate(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));
	if request.method == 'POST':
		return HttpResponse('Congratzzzz');

	else:
		kahsraForm = KhasraForm();

	return render(request, BASE_DIR + "/templates/pages/home.html", {'khasra_form': kahsraForm});



