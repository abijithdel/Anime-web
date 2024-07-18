from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField(upload_to='img')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video')
    image = models.ImageField(upload_to='img/thumbnail')

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return f"{self.title} ({self.category.name})"

class animes(models.Model):
    atitle = models.CharField(max_length=50)
    adescription = models.TextField(max_length=300)
    acategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    avideo = models.FileField(upload_to='video')
    aimage = models.ImageField(upload_to='img/thumbnail')

    class Meta:
        verbose_name = "animes"
        verbose_name_plural = "animes"

    def __str__(self):
        return f"{self.atitle} ({self.acategory.name})"

class Movies(models.Model):
    mtitle = models.CharField(max_length=50)
    mdescription = models.TextField(max_length=300)
    mcategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    mvideo = models.FileField(upload_to='video')
    mimage = models.ImageField(upload_to='img/thumbnail')

    class Meta:
        verbose_name = "Movies"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.mtitle} ({self.mcategory.name})"
