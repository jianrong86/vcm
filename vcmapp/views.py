from django.shortcuts import render, get_object_or_404

# Create your views here.
from vcmapp.models import ReleaseVersion
from datetime import datetime
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

data_list = [
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
    'self_test_fail_reason ',
    'val_verify_result',
    'val_verify_fail_reason',
    'create_time',
    'status'
]

class SoftwareView(View):
    def get(self, request):
        software_list = ReleaseVersion.objects.all()
        return render(request, "index.html", {"ver_lists": software_list})

class SoftwareCreate(View):
    def get(self,request):
        return render(request, "software_create.html")

    # @csrf_exempt
    def post(self,request):
        ret = dict()
        if request.is_ajax():
            print("aaaaaaaaaaaa")
            project_name = request.POST.get('project_name')

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
                status=request.POST.get('status'),
                compiler=request.POST.get('compiler'),
                verifier=request.POST.get('verifier'),
                vpm=request.POST.get('vpm')
            )
            print("plan_release_date:" + request.POST.get('plan_release_date'))
            print("actual_release_date:" + request.POST.get('actual_release_date'))
            # print("submit_items")
            # ver_list = ReleaseVersion.objects.all()

            # ret['ver_lists'] = ver_list
            ret['status'] = "success"
            # print("ret:%s" % ret)
            # return JsonResponse(ret)
        else:
            ret['status'] = "fail"
        print(ret)
        return HttpResponse(json.dumps(ret), content_type='application/json')
        # return render(request, 'index.html', {"ver_lists": ver_list})
# @login_required
# def release_ver_manage(request):
#     ver_list = ReleaseVersion.objects.all()
#     return render(request, "index.html", {"ver_lists": ver_list})

def new_items(request):
    # ver_list = ReleaseVersion.objects.all()
    return render(request, "new_items.html")

def edit_items(request, id):
    ver = ReleaseVersion.objects.get(id=id)
    return render(request, "edit_items.html", {"ver": ver})

def update_items(request, id):
    ver = ReleaseVersion.objects.get(id=id)

    if not ver:
        pass

    try:
        ver.project_name = request.POST.get('project_name')
        ver.customer_name = request.POST.get('customer_name')
        ver.customer_id = request.POST.get('customer_id')
        ver.firmware_develop = request.POST.get('firmware_develop')
        ver.webui_develop = request.POST.get('webui_develop')
        ver.software_version = request.POST.get('software_version')
        ver.software_path = request.POST.get('software_path')
        ver.modification = request.POST.get('modification')

        plan_release_time = "%s %s" % (request.POST.get('plan_release_date_0'), request.POST.get('plan_release_date_1'))
        ver.plan_release_date = datetime.strptime(plan_release_time, "%Y-%m-%d %H:%M%S")

        actual_releaes_time = "%s %s" % (request.POST.get('actual_release_date_0'), request.POST.get('actual_release_date_1'))
        ver.actual_release_date = datetime.strptime(actual_releaes_time, "%Y-%m-%d %H:%M%S")

        ver.release_delay_reason = request.POST.get('release_delay_reason')
        ver.self_test_result = request.POST.get('self_test_result')
        ver.self_test_fail_reason = request.POST.get('self_test_fail_reason')
        ver.val_verify_result = request.POST.get('val_verify_result')
        ver.val_verify_fail_reason = request.POST.get('val_verify_fail_reason')
        ver.create_time = request.POST.get('create_time')
        ver.status = request.POST.get('status')
        print("ver.status: %s" % ver.status)
        ver.save()
    except BaseException as e:
        render(request, "404.html")

    return render(request, "edit_items.html", {"ver": ver})


def submit_items(request):
    project_name = request.POST.get('project_name')

    ReleaseVersion.objects.create(
        project_name=request.POST.get('project_name'),
        customer_name=request.POST.get('customer_name'),
        customer_id = request.POST.get('customer_id'),
        firmware_develop = request.POST.get('firmware_develop'),
        webui_develop = request.POST.get('webui_develop'),
        software_version = request.POST.get('software_version'),
        software_path = request.POST.get('software_path'),
        modification = request.POST.get('modification'),
        plan_release_date = request.POST.get('plan_release_date'),
        actual_release_date = request.POST.get('actual_release_date'),
        release_delay_reason = request.POST.get('release_delay_reason'),
        self_test_result = request.POST.get('self_test_result'),
        self_test_fail_reason = request.POST.get('self_test_fail_reason'),
        val_verify_result = request.POST.get('val_verify_result'),
        val_verify_fail_reason = request.POST.get('val_verify_fail_reason'),
        create_time = request.POST.get('create_time'),
        status = request.POST.get('status'),
        compiler=request.POST.get('compiler'),
        verifier = request.POST.get('verifier'),
        vpm = request.POST.get('vpm')
    )
    print("project_name:" + project_name)
    print("submit_items")
    ver_list = ReleaseVersion.objects.all()
    return render(request, 'index.html', {"ver_lists": ver_list})