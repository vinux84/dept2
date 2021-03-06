from django.core.urlresolvers import reverse
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.conf import settings

User = settings.AUTH_USER_MODEL


class StaffProfile(models.Model):
    owner = models.ForeignKey(User)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    profile_timestamp = models.DateTimeField(auto_now_add=True)
    profile_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("staff:detail", kwargs={"slug": self.slug})

    @property
    def title(self):
        return self.first_name  # this adds the ability to change it to obj.title


def staff_profile_pre_save_receiver(sender, instance, *args, **kwargs):

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(staff_profile_pre_save_receiver, sender=StaffProfile)



