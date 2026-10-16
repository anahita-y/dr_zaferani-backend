from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField("نام دسته" , max_length = 100)
    slug = models.SlugField("اسلاگ" , allow_unicode = True , unique = True)

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField("عنوان" , max_length = 200)
    slug = models.SlugField("اسلاگ (آدرس مقاله)"  , allow_unicode = True, unique = True)
    excerpt = models.TextField("خلاصه‌ی کوتاه" , max_length = 400)
    cover_image = models.ImageField("تصویر شاخص" , upload_to = "articles/")
    category = models.ForeignKey(
        Category ,
        on_delete = models.SET_NULL , 
        null = True , 
        blank = True ,
        related_name = "articles" , 
        verbose_name = "دسته‌بندی" , 
    )

    content = models.TextField("متن مقاله (HTML)")
    read_time = models.PositiveSmallIntegerField("زمان مطالعه (دقیقه)" , default = 3)
    published_at = models.DateField("تاریخ انتشار"  , default = timezone.localdate)

    is_featured = models.BooleanField("مقاله ویژه" , default = False)
    is_published_at = models.BooleanField("منتشر شده" , default = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ["-published_at" , "-id"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)

        if self.is_featured:
            Article.objects.exclude(pk = self.pk).filter(is_featured = True).update(is_featured = False)


    def __str__(self):
        return self.title


class ArticlesPageSettings(models.Model):
    title = models.CharField("تایتل صفحه" , max_length = 150 , default = "مقالات آموزشی")
    description = models.TextField("متن زیر تایتل" , blank = True)


    class Meta:
        verbose_name = "تنظیمات صفحه مقالات"
        verbose_name_plural = "تنظیمات صفحه مقالات"

    def save(self , *args , **kwargs):
        self.pk = 1
        super().save(*args , **kwargs)

    def delete(self , *args , **kwargs):
        pass 

    def __str__(self):
        return self.title