from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    
    # def add_page(cat, title, url, views=0):
    #     p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    #     return p

    # def add_cat(name, views=0, likes=0):
    #     c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    #     return c

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
