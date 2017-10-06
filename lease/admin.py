from django.contrib import admin
from . models import print_count, khasra, audit_khasra, transaction, blocks;

# Register your models here.
admin.site.register(blocks);
admin.site.register(print_count);
admin.site.register(khasra);
admin.site.register(audit_khasra);
admin.site.register(transaction);
