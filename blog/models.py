from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها "

class Article (models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="نویسنده")
    title = models.CharField(max_length=70, verbose_name="عنوان")
    category = models.ManyToManyField(Category,related_name='articles', verbose_name="دسته")
    body = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to="image/article", verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت ")
    update = models.DateTimeField(auto_now=True, verbose_name="اخرین به روز رسانی")
    summary = models.CharField(max_length=20, verbose_name="خلاصه")
    slug = models.SlugField(null=True, unique=True)



    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        if self.body :
            self.summary = self.body[20]
        super(Article,self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:dtails', kwargs={'slug': self.slug})



    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="70px" height="60px">')

    class Meta :
        ordering = ('-created',)
        verbose_name = "مقاله"
        verbose_name_plural = "مفالات"




class Comment (models.Model) :
    article = models.ForeignKey(Article,on_delete=models.CASCADE , related_name='comment', verbose_name="مقاله")
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='user', verbose_name="کاربر")
    text = models.TextField(verbose_name="کامنت")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")
    parent = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE, related_name='reply')


    @property
    def __str__(self):
        return  self.text[:5]

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها "

class Massage(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    phonnumber = models.IntegerField(verbose_name="شماره تلفن")
    titl = models.CharField(max_length=30, verbose_name="عنوان")
    body = models.TextField(verbose_name="متن پیام")

    def __str__(self):
        return self.titl[:5]


    class Meta :
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها "


class Like(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like", verbose_name="کاربر")
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name="like", verbose_name="مقاله")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}--{self.article.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"

