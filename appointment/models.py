from django.core.validators import RegexValidator
from django.db import models 
from core.models import SingletonModel

link_validator = RegexValidator(
    regex = r"^(https?://|tel:|mailto:|/)" ,
    message = "لینک باید با http://، https://، tel:، mailto: یا / شروع شود." ,
)


class AppointmentPageSettings(SingletonModel):
    title = models.CharField("تایتل صفحه" , max_length = 150 , default = "رزرو نوبت")
    description = models.TextField(
        "متن زیر تایتل" ,
        blank = True ,
        default = "برای دریافت نوبت، از یکی از راه‌های ارتباطی زیر استفاده کنید." ,
    )

    class Meta:
        verbose_name = "تنظیمات صفحه رزرو نوبت"
        verbose_name_plural = "تنظیمات صفحه رزرو نوبت"


    def __str__(self):
        return self.title 

class AppointmentMethod(models.Model):
    icon = models.CharField(
        "نام ایکون" , 
        max_length = 50 ,
        help_text="مثلاً phone، smartphone، whatsapp، telegram، clock، map-pin" ,
    )
    title = models.CharField("عنوان" , max_length =100)
    value = models.TextField("متن کارت" , help_text = "برای چند خط، هر خط را جدا بنویسید")
    link = models.CharField(
        "لینک (اختیاری)" ,
        max_length = 300 , 
        blank = True ,
        validators = [link_validator] ,
        help_text = "مثلاً tel:02188650501 یا https://t.me/username" ,
    )
    order = models.PositiveSmallIntegerField("ترتیب" , default = 0)
    is_active = models.BooleanField("فعال" , default = True)


    class Meta:
        ordering = ["order"]
        verbose_name = "راه ارتباطی"
        verbose_name_plural =  "راه‌های ارتباطی"

    def __str__(self):
        return self.title