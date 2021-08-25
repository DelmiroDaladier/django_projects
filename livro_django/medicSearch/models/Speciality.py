from medicSearch.models import *

class Speciality(models.Model):
    name = models.CharField(null=False, max_lenth=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)