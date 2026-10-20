from django.db import models

class Service(models.Model):
    class Icon(models.TextChoices):
        HEART = "heart", "قلب (heart)"
        SHIELD = "shield", "سپر (shield)"
        STAR = "star", "ستاره (star)"
        CHECK = "check", "تیک (check)"
        EYE = "eye", "چشم (eye)"
        SEARCH = "search", "ذره‌بین (search)"
        SPARKLES = "sparkles", "درخشش (sparkles)"
        SCAN = "scan", "اسکن (scan)"
        SERVICES = "services", "خدمات (services)"
    
    title = models.CharField("عنوان" , max_length = 150)
    description = models.TextField("توضیح کوتاه")
    icon = models.CharField(
        "نام ایکون" , 
        max_length = 50 ,
        choices = Icon.choices , 
        default = Icon.HEART ,
    )
    more_info = models.TextField("اطلاعات بیشتر" , blank = True)
    order = models.PositiveSmallIntegerField("ترتیب نمایش" , default = 0)
    show_on_home = models.BooleanField("نمایش در صفحه اصلی" , default = True)
    is_active = models.BooleanField("فعال" , default = True)

    class Meta :
        ordering = ["order"]
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"

    def __set__(self):
        return self.title
