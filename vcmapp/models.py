from django.db import models

# Create your models here.
# class Users(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(null=True, blank=True)
#     position = models.CharField(max_length=20, null=True, blank=True)
#     password = models.CharField(max_length=20, null=True, blank=True)
#
#     def __str__(self):
#         return self.name

class ReleaseVersion(models.Model):
    project_name = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=30)
    customer_id = models.CharField(max_length=10)
    firmware_develop = models.EmailField(null=True, blank=True)
    webui_develop = models.EmailField(null=True, blank=True)
    software_version = models.CharField(max_length=256, null=True, blank=True)
    software_path = models.TextField(null=True, blank=True)
    modification = models.TextField(null=True, blank=True)
    plan_release_date = models.DateTimeField('Plan Release Date', null=True, blank=True)
    actual_release_date = models.DateTimeField('Actual Release Date', null=True, blank=True)
    release_delay_reason = models.TextField(null=True, blank=True)
    self_test_result = models.CharField(max_length=10, null=True, blank=True)
    self_test_fail_reason = models.TextField(null=True, blank=True)
    val_verify_result = models.CharField(max_length=10, null=True, blank=True)
    val_verify_fail_reason = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)
    compiler = models.EmailField(null=True, blank=True)
    verifier = models.EmailField(null=True, blank=True)
    vpm = models.EmailField(null=True, blank=True)

    class Meta:
        unique_together = ("project_name", "customer_id", "software_version")



    def __str__(self):
        return self.software_version
