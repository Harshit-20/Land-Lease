
from django.db import models;
from django.contrib.auth.models import User;
from django.db.models.signals import post_save;
from django.dispatch import receiver;

# Create your Models Here

class blocks(models.Model):
	block_id = models.IntegerField(primary_key=True);
	block_name = models.CharField(max_length=20, null=False, default=None); 

class transaction(models.Model):
	_id = models.AutoField(primary_key=True);
	acc_id = models.IntegerField(null=False, default=True);
	payment_by = models.CharField(max_length=30, null=True, default=None);
	payment_no = models.CharField(max_length=30, null=True, default=None);
	payment_date = models.DateTimeField(auto_now=True);
	is_20yr_free = models.IntegerField( null=True, default= 0);
	is_free_hold = models.IntegerField(null=True, default= 0);
	depositior_name = models.CharField(max_length=50, null=True, default=None);
	depositior_mob = models.CharField(max_length=15, null=True, default=None);
	user_id = models.ForeignKey(User, max_length=20, null=True, default=None);
	curr_date = models.DateTimeField(null=True, default= None);
	remark = models.TextField(null=True, default=None);

class audit_khasra(models.Model):
	_id = models.AutoField(primary_key=True);
	block_id = models.ForeignKey(blocks, null=False, default=None);
	mohalla_name = models.CharField(max_length=50, null=True, default=None);
	plot_no = models.CharField(max_length=50, null=True, default=None);
	area_total_resi = models.FloatField(max_length=10, null=False, default=0.0);
	area_total_non_resi = models.FloatField(max_length=10, null=False, default=0.0);
	area_free = models.FloatField(max_length=10, null=False, default=0.0);
	plot_desc = models.CharField(max_length=100, null=True, default=None);
	holder_name = models.CharField(max_length=500, null=True, default=None);
	revenue_resi = models.FloatField(max_length=10, null=False, default=0.0);
	revenue_non_resi = models.FloatField(max_length=10, null=False, default=0.0);
	lease_expiry_date = models.DateTimeField(null=True);
	remarks = models.TextField(null=True, default=None);
	page_no = models.IntegerField(null=True, default=None);
	mutation_id = models.IntegerField(null=True, default=None);
	per_plot_area = models.TextField(null=True, default=None);
	curr_date = models.DateTimeField(auto_now = True);
	operation = models.CharField(max_length=7, null=True, default=None);



class khasra(models.Model):
	khasra_id = models.AutoField(primary_key=True);
	block_id = models.ForeignKey(blocks, null=False, default=None);
	mohalla_name = models.CharField(max_length=50, null=True, default=None);
	plot_no = models.CharField(max_length=50, null=True, default=None);
	area_total_resi = models.FloatField(max_length=10, null=False, default=0.0);
	area_total_non_resi = models.FloatField(max_length=10, null=False, default=0.0);
	area_free = models.FloatField(max_length=10, null=False, default=0.0);
	plot_desc = models.CharField(max_length=100, null=True, default=None);
	holder_name = models.CharField(max_length=500, null=True, default=None);
	revenue_resi = models.FloatField(max_length=10, null=False, default=0.0);
	revenue_non_resi = models.FloatField(max_length=10, null=False, default=0.0);
	lease_expiry_date = models.DateTimeField(null=True);
	case_no = models.CharField(max_length=100, null=True, default = None);
	adesh_date = models.DateTimeField(null= True, default=None);
	remarks = models.TextField(null=True, default=None);
	corrected_entry = models.TextField(null=True, default=None);
	arrears_year = models.CharField(max_length=9, null= True, default = '2009-2010');
	arrear = models.FloatField(max_length=10, default=0.0, null=False);
	page_no = models.IntegerField(null=True, default=None);
	mutation_id = models.IntegerField(null=True, default=None);
	is_govt = models.IntegerField(null=False, default=0);
	per_plot_area = models.TextField(null=True, default=None); 
	islock = models.IntegerField(null=True, default = 0);
	operation = models.IntegerField(null=True, default=0);
	user_id = models.ForeignKey(User, null=True, default=None);
	curr_date = models.DateTimeField(null=True, default=None);
	entry_date = models.DateTimeField(null=True, default=None);

class print_count(models.Model):
	_id = models.AutoField(primary_key=True);
	acc_id = models.ForeignKey(transaction, max_length=20, null=True, default=None);
	print_date = models.DateTimeField(auto_now=True);
	user_name  = models.ForeignKey(User, null=True, default=None);


