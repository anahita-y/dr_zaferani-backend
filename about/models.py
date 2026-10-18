from django.db import models

class AboutPage(models.Model):
    badge_text = models.CharField("برچسب بالای عنوان" , max_length = 100 , default = "درباره پزشک")
    doctor_name = models.CharField("نام دکتر (تایتل)" , max_length = 150)
    doctor_name_en = models.CharField("نام انگلیسی زیر عکس" , max_length = 150 , blank = True)
    short_bio = models.CharField("بیوگرافی کوتاه" , max_length = 250)
    long_bio = models.TextField("بیوگرافی بلند")
    doctor_image = models.ImageField("عکس دکتر" , upload_to = "about/")

    experience_badge_value= models.CharField("عدد کارت تجربه" , max_length = 20 , default = "+20")
    experience_badge_label = models.CharField("برچسب کارت تجربه" , max_length = 50 , default = "سال تجربه")
    experience_badge_icon = models.CharField("نام ایکون کارت تجربه" , max_length = 50 , default = "graduation-cap")

    award_title = models.CharField("عنوان کارت افتخار" , max_length = 100 , default = "پزشک برگزیده")
    award_subtitle = models.CharField("زیرعنوان کارت افتخار", max_length=100, blank=True)
    award_icon = models.CharField("نام ایکون کارت افتخار" , max_length = 50 , default = "trophy")

    booking_button_text = models.CharField("متن دکمه رزرو" , max_length = 50 , default = "رزرو نوبت مشاوره")
    booking_button_icon = models.CharField("نام ایکون دکمه رزرو" , max_length = 50 , default = "calendar")
    booking_button_link = models.CharField("لینک رزرو نوبت" , max_length = 200 , default = "/booking")

    class Meta :
        verbose_name = "درباره دکتر"
        verbose_name_plural = "درباره دکتر"

    def save(self , *args , **kwargs):
        self.pk = 1
        super().save(*args , **kwargs)

    def delete(self, *args , **kwargs):
        pass

    def __str__(self):
        return self.doctor_name


class AboutSpecialty(models.Model):
    about = models.ForeignKey(AboutPage , on_delete = models.CASCADE , related_name = "specialties")
    title = models.CharField("عنوان" , max_length = 100)
    icon = models.CharField("نام ایکون" , max_length = 50 , default = "circle-check")
    order = models.PositiveSmallIntegerField("ترتیب نمایش" , default = 0)

    class Meta:
        ordering = ["order"]
        verbose_name = "تخصص"
        verbose_name_plural = "تخصص‌ها"

    def __str__(self):
        return self.title


class AboutStat(models.Model):
    about = models.ForeignKey(AboutPage , on_delete = models.CASCADE , related_name = "stats")
    value = models.CharField("مقدار" , max_length = 20 , help_text = "مثلاً 98% یا +3796")
    label = models.CharField("برچسب" , max_length = 100)
    icon = models.CharField("نام ایکون" , max_length = 50 , blank = True)
    order = models.PositiveSmallIntegerField("ترتیب نمایش" , default = 0)


    class Meta:
        ordering = ["order"]
        verbose_name = "آمار"
        verbose_name_plural = "آمار"

    def __str__(self):
        return f"{self.value} {self.label}"


    
