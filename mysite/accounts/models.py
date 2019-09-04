import uuid
from django.db import models
from django.contrib.auth.models import User
import re
import time

class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
# FileField
# PointField
# ManyToManyField
def get_filename_profile(instance, filename):
    username_name = instance.user.username
    username_name = re.sub('[@+]', '', username_name)
    time_name = str(time()).split('.')[0]
    ext = filename[filename.rfind('.'):]
    return 'photos/profiles/' + strftime('%Y/%m/%d/') + username_name + '_' + time_name + ext

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    image = models.ImageField(max_length=200, upload_to=get_filename_profile, default='photos/profiles/default.png')
    str_id = models.CharField(max_length=40, default=None, null=True, blank=True)
    city = models.ForeignKey(City, default=None,on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True, default=None)
    birthday = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    new_email = models.EmailField(null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    mobile = models.IntegerField()
    is_mobile_verified = models.NullBooleanField(default=None, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    order = models.SmallIntegerField(default=1, help_text='Set to 1 for this collection to be the first, 2 to be second etc.')
    big_field = models.BigIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    # location_latlon = models.PointField(blank=True, null=True)
    weight = models.FloatField(null=True)
    facebook_url = models.URLField(max_length=255, blank=False, null=False)
 
    def __unicode__(self):
        return u'%s (%s)' % (self.user.username, self.user.email)
 
    def get_user(self):
        cache_key = 'api_user_%d_json' % self.user.id
        cache_time = 86400
        data = cache.get(cache_key)
        print("getting caches")
        if not data:
            print("setting caches")
            try:
                user = User.objects.get(pk=self.user.id)
            except User.DoesNotExist:
                return None
    
            minimal_serializer = UserSerializer(user)
            data = minimal_serializer.data
            cache.set(cache_key, data, cache_time)
        return data
                               
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.str_id:
            self.str_id = str(uuid.uuid4())
 
        return super(Profile, self).save(force_insert=force_insert, force_update=force_update, using=using,
             update_fields=update_fields)





# @receiver(post_save, sender=City)
# def clean_cache(sender, instance, created, **kwargs):
#     cache.delete_many(
#         ['api_city_{0}_json'.format(instance.id),
#          'geo_city_{0}'.format(instance.id)])