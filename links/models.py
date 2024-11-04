from django.db import models
from django.utils.text import slugify
# Create your models here.
# save a shrotended link to our database


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.url}"

    def click(self):
        # increment clicks each time a click happens
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        # check if someone created a slug when entering a link, if not we generate it using slugify
        if not self.slug:
            # slugify converts any spaces into dashes
            self.slug = slugify()
        super().save(*args, **kwargs)
