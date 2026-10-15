from django.db import models

class Service(models.Model):
    title = models.CharField("عنوان" , max_length = 150)
    description = models.TextField("توضیح کوتاه")
    icon = models.CharField("نام ایکون" , max_length = 50 ,help_text = "مثلاً heart یا star")
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
