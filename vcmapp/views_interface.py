from django.http import JsonResponse
from vcmapp.models import ReleaseVersion
from django.core.exceptions import ValidationError

def add_software(request):

    try:
        ReleaseVersion.objects.create(
            project_name=request.POST.get('project_name'),
            customer_name=request.POST.get('customer_name'),
            customer_id=request.POST.get('customer_id'),
            firmware_develop=request.POST.get('firmware_develop'),
            webui_develop=request.POST.get('webui_develop'),
            software_version=request.POST.get('software_version'),
            software_path=request.POST.get('software_path'),
            modification=request.POST.get('modification'),
            plan_release_date=request.POST.get('plan_release_date'),
            actual_release_date=request.POST.get('actual_release_date'),
            release_delay_reason=request.POST.get('release_delay_reason'),
            self_test_result=request.POST.get('self_test_result'),
            self_test_fail_reason=request.POST.get('self_test_fail_reason'),
            val_verify_result=request.POST.get('val_verify_result'),
            val_verify_fail_reason=request.POST.get('val_verify_fail_reason'),
            create_time=request.POST.get('create_time'),
            status=request.POST.get('status')
        )
    except ValidationError as e:
        return JsonResponse({'status':10024, 'message': e})

    return JsonResponse({'status': 200, 'message': 'add software success'})