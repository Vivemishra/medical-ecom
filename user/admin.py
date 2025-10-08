from django.contrib import admin

from . models import *

class tbl_orderlistAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Mobile', 'City', 'Address', 'NL', 'OS')
admin.site.register(tbl_orderlist,tbl_orderlistAdmin)

