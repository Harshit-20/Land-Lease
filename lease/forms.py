from django import forms;
from . models import blocks, transaction, audit_khasra, khasra, print_count;
from django.contrib.auth.models import User;
from django.contrib.auth.forms import UserCreationForm;
from datetime import datetime;

class UserForm(forms.ModelForm):

	class Meta:
		model = User;
		fields = ('username','email');

class KhasraForm(forms.ModelForm):

	class Meta:
		model = khasra;
		fields = ('block_id', 'revenue_resi', 'plot_no', 'khasra_id', 'lease_expiry_date', 'case_no');

		widgets = {
			'lease_expiry_date': forms.SelectDateWidget(),
		}		 