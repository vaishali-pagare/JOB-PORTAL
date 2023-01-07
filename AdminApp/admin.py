from django.contrib import admin
from AdminApp.models import Industry,Payment
# Register your models here.
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("id","type")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("cardno","cvv","expiry","balance")
admin.site.register(Industry,IndustryAdmin)
admin.site.register(Payment,PaymentAdmin)


