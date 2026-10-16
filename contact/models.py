from django.db import models
from core.models import SingletonModel


class ContactInfo(SingletonModel):
   
    logo = models.ImageField("لوگو" , upload_to = "contact/")
    title = models.CharField("تایتل (نام دکتر)" , max_length = 150)
    subtitle = models.CharField("زیرعنوان" , max_length = 200 , blank = True)
    description = models.TextField("توضیحات" , blank = True)

    quick_links_title = models.CharField("عنوان بخش دسترسی سریع" , max_length = 100 , default = "دسترسی سریع")
    services_links_title = models.CharField("عنوان بخش خدمات" , max_length=100 , default = "خدمات")
    contact_title = models.CharField("عنوان بخش اطلاعات تماس" , max_length=100 , default = "اطلاعات تماس")

    clinic_phone = models.CharField("تلفن مطب" , max_length = 20)
    mobile_phone = models.CharField("شماره همراه" , max_length = 20 , blank = True)
    email = models.EmailField("ایمیل" , blank = True)
    address = models.TextField("آدرس")
    latitude = models.DecimalField("عرض جغرافیایی" , max_digits = 9 , decimal_places = 6 , null = True , blank = True)
    longitude = models.DecimalField("طول جغرافیایی" , max_digits = 9 , decimal_places =6 , null = True , blank = True)

    copyright_text = models.CharField("متن کپی‌رایت" , max_length = 300 , blank = True)

    class Meta:
        verbose_name = "اطلاعات تماس و فوتر"
        verbose_name_plural = "اطلاعات تماس و فوتر"

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    title = models.CharField("عنوان" , max_length = 50 , help_text = "مثلاً اینستاگرام")
    icon = models.CharField("کلید ایکون" , max_length = 50 , help_text = "مثلاً instagram یا whatsapp یا telegram")
    url = models.URLField("لینک")
    order = models.PositiveSmallIntegerField("ترتیب" , default = 0)
    is_active = models.BooleanField("فعال" , default = True)

    class Meta:
        ordering = ["order"]
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه‌های اجتماعی"

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    class Group(models.TextChoices):
        QUICK = "quick" , "دسترسی سریع"
        SERVICES = "services" , "خدمات"

    group = models.CharField("گروه" , max_length = 20, choices = Group.choices)
    title = models.CharField("عنوان" , max_length = 100)
    link = models.CharField("لینک" , max_length = 200, help_text = "مثلاً /about یا /services یا /articles")
    order = models.PositiveSmallIntegerField("ترتیب", default = 0)
    is_active = models.BooleanField("فعال" , default = True)

    class Meta:
        ordering = ["group", "order"]
        verbose_name = "لینک فوتر"
        verbose_name_plural = "لینک‌های فوتر"

    def __str__(self):
        return f"{self.get_group_display()} - {self.title}"