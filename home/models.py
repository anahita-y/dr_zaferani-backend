from django.db import models


class HomePage(models.Model):
    doctor_name = models.CharField("نام دکتر (تایتل)" , max_length = 150)
    subtitle = models.CharField("زیرعنوان" , max_length = 200 , blank = True)
    biography = models.TextField("بیوگرافی")
    doctor_image = models.ImageField("عکس دکتر" , upload_to = "home/")
    experience_years = models.PositiveSmallIntegerField("تعداد سال تجربه" , default = 20)
    experience_label = models.CharField("برچسب زیر عدد" , max_length = 50 ,default = "سال تجربه")
    badge_text = models.CharField("متن برچسب" , max_length = 100 , default = "بیش از ۲۰ سال تجربه")
    
    booking_button_text = models.CharField("متن دکمه رزرو نوبت" , max_length  = 50 , default = "رزرو نوبت")
    booking_button_icon = models.CharField("نام ایکون رزرو نوبت" , max_length = 50 , default = "calendar")
    booking_button_link = models.CharField("لینک رزرو نوبت" , max_length = 50 , default = "/booking")

    consult_button_text = models.CharField("متن دکمه مشاوره", max_length=50, default="دریافت مشاوره")
    consult_button_icon = models.CharField("نام ایکون مشاوره" , max_length = 50 , default = "phone")
    consult_button_link = models.CharField("لینک مشاوره" , max_length = 200 , default = "/contact")

    services_badge_text = models.CharField("برچسب بخش خدمات" , max_length = 100 , default =  "خدمات تخصصی")
    services_title = models.CharField("تایتل بخش خدمات" , max_length = 150 , default = "خدمات چشم پزشکی")
    services_description = models.TextField("متن کوتاه زیر تایتل خدمات" , blank = True)

    services_button_text = models.CharField("متن دکمه مشاهده خدمات" , max_length = 50 , default = "مشاهده همه خدمات")
    services_button_icon = models.CharField("نام ایکون مشاهده خدمات" , max_length = 50 , default = "arrow-left")
    services_button_link = models.CharField("لینک مشاهده خدمات" , max_length = 200 , default = "/services")

    articles_badge_text = models.CharField("برچسب بخش مقالات" , max_length = 100 , default = "مقالات")
    articles_title = models.CharField("تایتل بخش مقالات" , max_length = 150 , default = "آخرین مطالب آموزشی")
    articles_description = models.TextField("متن زیر تایتل مقالات" , blank = True)

    articles_button_text = models.CharField("متن دکمه مشاهده مقالات" , max_length = 50 , default = "مشاهده همه مقالات")
    articles_button_icon = models.CharField("نام ایکون مشاهده مقالات", max_length=50, default="arrow-left")
    articles_button_link = models.CharField("لینک مشاهده مقالات", max_length=200, default="/articles")
    class Meta:
        verbose_name = "صفحه اصلی"
        verbose_name_plural = "صفحه اصلی"

    def save(self , *args , **kwargs):
        self.pk = 1
        super().save(*args , **kwargs)

    def delete(self , *args , **kwargs):
        pass 

    def __str__(self):
        return self.doctor_name
    