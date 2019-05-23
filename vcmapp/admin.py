from django.contrib import admin
from vcmapp.models import ReleaseVersion

# Register your models here.
class ReleaseVersionAdmin(admin.ModelAdmin):
    list_display = [
        'project_name',
        'customer_name',
        'customer_id',
        'firmware_develop',
        'webui_develop',
        'software_version',
        'software_path',
        'modification',
        'plan_release_date',
        'actual_release_date',
        'release_delay_reason',
        'self_test_result',
        'self_test_fail_reason',
        'val_verify_result',
        'val_verify_fail_reason',
        'status',
        'create_time',
    ]

admin.site.register(ReleaseVersion, ReleaseVersionAdmin)
