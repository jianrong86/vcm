from django.shortcuts import render, get_object_or_404

# Create your views here.
from vcmapp.models import ReleaseVersion
from datetime import datetime
from django.views.generic.base import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import json

data_list = [
    'id',
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
    'create_time',
    'status'
]

class SoftwareView(View):
    def get(self, request):
        software_list = ReleaseVersion.objects.all()
        return render(request, "index.html", {"ver_lists": software_list})

class SoftwareList(View):
    def get(self, request):
        print("software list")
        fields = ['id', 'weekly','project_name', 'customer_name', 'customer_id', 'software_version', 'plan_release_date', 'status']
        filters = dict()
        ret = dict(data=list(ReleaseVersion.objects.filter(**filters).values(*fields).order_by('-id')))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class SoftwareCreate(View):
    def get(self,request):
        status_list = []
        test_result_list = []
        build_type_list = []
        release_type_list = []
        for status_type in ReleaseVersion.status_choice:
            status_dict = dict(item=status_type[0], value=status_type[1])
            status_list.append(status_dict)
        for test_result_type in ReleaseVersion.result_choice:
            test_result_dict = dict(item=test_result_type[0], value=test_result_type[1])
            test_result_list.append(test_result_dict)
        for build_type in ReleaseVersion.build_type_choice:
            build_type_dict = dict(item=build_type[0], value=build_type[1])
            build_type_list.append(build_type_dict)
        for release_type in ReleaseVersion.release_type_choice:
            release_type_dict = dict(item=release_type[0], value=release_type[1])
            release_type_list.append(release_type_dict)

        ret = {
            "status_list":status_list,
            "test_result_list":test_result_list,
            "build_type_list":build_type_list,
            "release_type_list":release_type_list
        }
        return render(request, "software_create.html", ret)

    # @csrf_exempt
    def post(self,request):
        ret = dict()
        if request.is_ajax():
            plan_date = request.POST.get('plan_release_date')
            if not plan_date:
                plan_date = None

            actual_date = request.POST.get('actual_release_date')
            if not actual_date:
                actual_date = None

            ReleaseVersion.objects.create(
                project_name=request.POST.get('project_name'),
                customer_name=request.POST.get('customer_name'),
                customer_id=request.POST.get('customer_id'),
                firmware_develop=request.POST.get('firmware_develop'),
                webui_develop=request.POST.get('webui_develop'),
                software_version=request.POST.get('software_version'),
                software_path=request.POST.get('software_path'),
                modification=request.POST.get('modification'),
                plan_release_date=plan_date,
                actual_release_date=actual_date,
                release_delay_reason=request.POST.get('release_delay_reason'),
                self_test_result=request.POST.get('self_test_result'),
                self_test_fail_reason=request.POST.get('self_test_fail_reason'),
                val_verify_result=request.POST.get('val_verify_result'),
                val_verify_fail_reason=request.POST.get('val_verify_fail_reason'),
                create_time=request.POST.get('create_time'),
                status=request.POST.get('status'),
                compiler=request.POST.get('compiler'),
                verifier=request.POST.get('verifier'),
                vpm=request.POST.get('vpm'),
                weekly=request.POST.get('weekly'),
                build_type=request.POST.get('build_type'),
                rebuild_reason=request.POST.get('rebuild_reason'),
                release_type=request.POST.get('release_type'),
                re_release_reason=request.POST.get('re_release_reason')
            )
            ret['status'] = "success"
        else:
            ret['status'] = "fail"
        print(ret)
        return HttpResponse(json.dumps(ret), content_type='application/json')
        # return render(request, 'index.html', {"ver_lists": ver_list})
# @login_required
# def release_ver_manage(request):
#     ver_list = ReleaseVersion.objects.all()
#     return render(request, "index.html", {"ver_lists": ver_list})

class SoftwareUpdate(View):
    def get(self, request):
        status_list = []
        test_result_list = []
        build_type_list = []
        release_type_list = []
        for status_type in ReleaseVersion.status_choice:
            status_dict = dict(item=status_type[0], value=status_type[1])
            status_list.append(status_dict)
        for test_result_type in ReleaseVersion.result_choice:
            test_result_dict = dict(item=test_result_type[0], value=test_result_type[1])
            test_result_list.append(test_result_dict)
        for build_type in ReleaseVersion.build_type_choice:
            build_type_dict = dict(item=build_type[0], value=build_type[1])
            build_type_list.append(build_type_dict)
        for release_type in ReleaseVersion.release_type_choice:
            release_type_dict = dict(item=release_type[0], value=release_type[1])
            release_type_list.append(release_type_dict)
        ver = ReleaseVersion.objects.get(id=request.GET['id'])
        ret = {
            "ver": ver,
            'status_list':status_list,
            'test_result_list':test_result_list,
            "build_type_list": build_type_list,
            "release_type_list": release_type_list
        }
        return render(request, "software_update.html", ret)

    def post(self, request):
        res = dict()
        res['status'] = 'success'
        ver = ReleaseVersion.objects.get(id=request.POST.get('sw_id'))

        if not ver:
            res['status'] = 'fail'

        try:
            ver.project_name = request.POST.get('project_name')
            ver.customer_name = request.POST.get('customer_name')
            ver.customer_id = request.POST.get('customer_id')
            ver.firmware_develop = request.POST.get('firmware_develop')
            ver.webui_develop = request.POST.get('webui_develop')
            ver.software_version = request.POST.get('software_version')
            ver.software_path = request.POST.get('software_path')
            ver.modification = request.POST.get('modification')
            ver.plan_release_date = request.POST.get('plan_release_date')
            ver.actual_release_date = request.POST.get('actual_release_date')
            ver.release_delay_reason = request.POST.get('release_delay_reason')
            ver.self_test_result = request.POST.get('self_test_result')
            ver.self_test_fail_reason = request.POST.get('self_test_fail_reason')
            ver.val_verify_result = request.POST.get('val_verify_result')
            ver.val_verify_fail_reason = request.POST.get('val_verify_fail_reason')
            ver.create_time = request.POST.get('create_time')
            ver.status = request.POST.get('status')
            ver.compiler = request.POST.get('compiler')
            ver.verifier = request.POST.get('verifier')
            ver.vpm = request.POST.get('vpm')
            ver.weekly = request.POST.get('weekly')
            ver.build_type = request.POST.get('build_type')
            ver.rebuild_reason = request.POST.get('rebuild_reason')
            ver.release_type = request.POST.get('release_type')
            ver.re_release_reason = request.POST.get('re_release_reason')
            ver.save()
        except BaseException as e:
            res['status'] = str(e)

        return HttpResponse(json.dumps(res), content_type='application/json')


def new_items(request):
    # ver_list = ReleaseVersion.objects.all()
    return render(request, "new_items.html")

def edit_items(request, id):
    ver = ReleaseVersion.objects.get(id=id)
    return render(request, "software_update.html", {"ver": ver})

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

    return render(request, "software_update.html", {"ver": ver})


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