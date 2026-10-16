from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from core.models import SingletonModel


class TestimonialsSettings(SingletonModel):
    badge_text = models.CharField("متن برچسب" , max_length = 100 , default = "نظرات بیماران")
    badge_icon = models.CharField("نام ایکون برچسب" , max_length = 50 , default = "message-square")
    title = models.CharField("تایتل" , max_length = 150 , default = "تجربه بیماران از همراهی با ما")
    description = models.TextField("توضیح کوتاه" , blank = True)
    button_text = models.CharField("متن دکمه مشاهده همه نظرات" , max_length = 50 , default = "مشاهده همه نظرات")
    button_icon = models.CharField("نام ایکون دکمه" , max_length = 50 , default = "chevron-down")

    
    form_badge_text = models.CharField("متن برچسب فرم" , max_length = 100 , default = "نظر شما")
    form_icon = models.CharField("نام ایکون فرم" , max_length = 50 , default = "user")
    form_title = models.CharField("تایتل فرم" , max_length = 150 , default = "تجربه خود را با ما در میان بگذارید")
    form_description = models.TextField("توضیح فرم" , blank = True)
    form_note = models.CharField("نکته‌ی کنار ایکون" , max_length = 200 , blank = True)

    notify_email = models.EmailField("ایمیل دریافت نظرهای جدید" , blank = True)
    auto_publish = models.BooleanField(
        "انتشار خودکار نظرهای جدید", 
        default = False ,
        help_text = "اگر خاموش باشد، نظر جدید بعد از تأیید شما در سایت قرار می‌گیرد" ,
    )

    class Meta:
        verbose_name = "تنظیمات نظرات"
        verbose_name_plural = "تنظیمات نظرات"

    def __str__(self):
        return self.title


class ReviewSubject(models.Model):
    title = models.CharField("عنوان" , max_length = 100)
    order = models.PositiveSmallIntegerField("ترتیب" , default = 0)
    is_active = models.BooleanField("فعال" , default = True)

    class Meta:
        ordering = ["order"]
        verbose_name = "موضوع نظر"
        verbose_name_plural = "موضوع‌های نظر"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField("نام" , max_length = 100)
    subject = models.ForeignKey(
        ReviewSubject , 
        on_delete = models.SET_NULL , 
        null = True , 
        blank = True ,
        related_name = "testimonials" , 
        verbose_name = "موضوع نظر" ,
    )
    rating = models.PositiveSmallIntegerField(
        "امتیاز" , 
        default = 5 , 
        validators = [MinValueValidator(1) , MaxValueValidator(5)] ,
    )
    text = models.TextField("متن نظر" , validators = [MaxLengthValidator(500)])
    is_verified = models.BooleanField("بیمار تأیید شده" , default = False)
    is_published = models.BooleanField("منتشر شده" , default = True)
    date = models.DateField("تاریخ" , default = timezone.localdate)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ["-date" , "-id"]
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return f"{self.name} ({self.rating}★)"