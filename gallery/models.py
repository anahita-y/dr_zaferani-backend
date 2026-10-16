from django.core.exceptions import ValidationError
from django.db import models
from core.models import SingletonModel


class GallerySettings(SingletonModel): 
    badge_text = models.CharField("متن برچسب" , max_length = 100, default = "گالری تصاویر")
    badge_icon = models.CharField("نام ایکون برچسب" , max_length = 50 , default = "image")
    title = models.CharField("تایتل" , max_length = 150 , default = "گالری تصاویر")
    description = models.TextField("توضیح کوتاه" , blank = True)

    button_text = models.CharField("متن دکمه" , max_length = 50 , default = "مشاهده همه تصاویر")
    button_icon = models.CharField("نام ایکون دکمه" , max_length = 50, default = "arrow-left")
    button_link = models.CharField("لینک دکمه" , max_length = 200 , default = "/gallery")

    page_title = models.CharField("تایتل صفحه گالری" , max_length = 150 , default = "گالری تصاویر")
    page_description = models.TextField("توضیح صفحه گالری" , blank = True)

    class Meta:
        verbose_name = "تنظیمات گالری"
        verbose_name_plural = "تنظیمات گالری"

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    MAX_IMAGES = 50
    MAX_ON_HOME = 4

    image = models.ImageField("تصویر" , upload_to = "gallery/")
    alt_text = models.CharField("متن جایگزین (alt)" , max_length = 200 , blank = True)
    show_on_home = models.BooleanField("نمایش در صفحه اصلی" , default = False)
    order = models.PositiveSmallIntegerField("ترتیب" , default = 0)
    is_active = models.BooleanField("فعال" , default = True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["order" , "-id"]
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"

    def clean(self):
        if not self.pk and GalleryImage.objects.count() >= self.MAX_IMAGES:
            raise ValidationError(f"حداکثر {self.MAX_IMAGES} تصویر مجاز است.")
        if self.show_on_home:
            on_home = GalleryImage.objects.filter(show_on_home=True).exclude(pk=self.pk)
            if on_home.count() >= self.MAX_ON_HOME:
                raise ValidationError(
                    f"حداکثر {self.MAX_ON_HOME} تصویر را می‌توان در صفحه اصلی نمایش داد."
                )

    def __str__(self):
        return self.alt_text or f"تصویر {self.pk}"