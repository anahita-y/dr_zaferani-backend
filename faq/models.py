from django.core.exceptions import ValidationError
from django.db import models
from core.models import SingletonModel


class FAQSettings(SingletonModel):
    badge_text = models.CharField("متن برچسب" , max_length = 100 , default = "سوالات متداول")
    badge_icon = models.CharField("نام ایکون برچسب" , max_length = 50 , default = "circle-help")
    title = models.CharField("تایتل" , max_length=150 , default = "پاسخ به سوالات پرتکرار")
    description = models.TextField("توضیح کوتاه" , blank = True)

    class Meta:
        verbose_name = "تنظیمات سوالات متداول"
        verbose_name_plural = "تنظیمات سوالات متداول"

    def __str__(self):
        return self.title


class FAQ(models.Model):
    MAX_IMPORTANT = 6

    question = models.CharField("سوال", max_length = 300)
    answer = models.TextField("پاسخ")
    is_important = models.BooleanField("مهم (نمایش در سایت)" , default = False)
    order = models.PositiveSmallIntegerField("ترتیب" , default = 0)
    is_active = models.BooleanField("فعال" , default = True)

    class Meta:
        ordering = ["order" , "id"]
        verbose_name = "سوال"
        verbose_name_plural = "سوالات"

    def clean(self):
        if self.is_important:
            important = FAQ.objects.filter(is_important = True).exclude(pk = self.pk)
            if important.count() >= self.MAX_IMPORTANT:
                raise ValidationError(
                    f"حداکثر {self.MAX_IMPORTANT} سوال را می‌توان «مهم» علامت زد."
                )

    def __str__(self):
        return self.question