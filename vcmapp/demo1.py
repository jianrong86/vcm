
file_list = [
'apps_proc/oem/app/core-app/src/jrd_main/jrd_oem_json_web.c',
'apps_proc/oem/app/core-app/src/jrd_main/jrd_oem_tn_web.c',
'apps_proc/oem/app/core-app/src/jrd_modules/celllock/jrd_cell_lock.c',
'apps_proc/oem/app/core-app/src/jrd_modules/celllock/jrd_cell_lock.h',
'apps_proc/oem/app/core-app/src/jrd_modules/led/jrd_led_indication.c',
'apps_proc/oem/app/core-app/src/jrd_modules/network/jrd_network_ext.c',
'apps_proc/oem/app/core-app/src/jrd_modules/sms/jrd_sms_core.c',
'apps_proc/oem/app/core-app/src/jrd_modules/sms/jrd_sms_ext.c',
'apps_proc/oem/app/core-app/src/jrd_modules/system/jrd_sys_al.c',
'apps_proc/oem/app/core-app/src/jrd_modules/system/jrd_sys_backup.c',
'apps_proc/oem/app/core-app/src/jrd_modules/usim/jrd_usim.c',
'apps_proc/oem/app/core-app/src/jrd_modules/usim/jrd_usim.h',
'apps_proc/oem/app/core-app/src/jrd_modules/usim/jrd_usim_al.c',
'apps_proc/oem/app/core-app/src/jrd_modules/voice/jrd_voice.c',
'apps_proc/oem/app/core-app/src/jrd_modules/voice/jrd_voice_core.c',
'apps_proc/oem/app/core-app/src/jrd_qmi/client/jrdcom_system_client_v01.h',
'apps_proc/oem/app/core-app/src/jrd_qmi/jrd_qmi_voice.c',
'jrd_oem/efs2_dir/hh40_generic/image_for_read_nv_files/NON-HLOS.ubi',
'jrd_oem/efs2_dir/hh41_claro_colombia/efs_4g2g/Note.txt',
'jrd_oem/efs2_dir/hh41_claro_colombia/efs_4g2g/efs.mbn',
'jrd_oem/efs2_dir/hh41_claro_colombia/efs_4g2g/efs_453_1.mbn',
'jrd_oem/efs2_dir/hh41_claro_colombia/efs_4g2g/efs_bak2/Note.txt',
'jrd_oem/efs2_dir/hh41_claro_colombia/efs_4g2g/efs_bak2/efs.mbn',
'jrd_oem/efs2_dir/hh41_claro_colombia/efs_4g2g/efs_bak2/efs_453_1.mbn',
'jrd_oem/efs2_dir/hh41_generic/image_for_read_nv_files/NON-HLOS.ubi',
'jrd_oem/jrd_resource_dir/jrd_resource_oem_prj/hh41_iu_rc/jrd-resource/resource/jrdcfg/efs/nv/item_files/ims/qp_ims_reg_config_db',
'jrd_oem/jrd_resource_dir/jrd_resource_oem_prj/hh41_iu_rc/jrd-resource/resource/jrdcfg/json_req_config_file',
'jrd_oem/jrd_resource_dir/jrd_resource_oem_prj/hh41_my_rc/jrd-resource/resource/profile/profile_operate',
'jrd_oem/recovery_files.xlsx',
'apps_proc/oem/app-framework/sqlite3-db',
        ]

cmd_list = {
'apps_proc/oem/app/core-app': "core-app",
'apps_proc/oem/app/webs':'webs',
'apps_proc/oem/app/slic_mgr':'slic-mgr',
'apps_proc/oem/app/cwmp':'easycwmp',
'apps_proc/oem/app-framework/sqlite3-db':'sqlite3-db',
'apps_proc/oem/app-framework/timer':'timer',
'apps_proc/oem/app-framework/sock-client':'sock-client',
'apps_proc/oem/app-framework/fota':'fota',
'apps_proc/data':'data',
'apps_proc/qmi':'qmi',
'apps_proc/mm-audio/audcal':'audcal',
'apps_proc/kernel':'linux-quic',
}
cmd_set = set()
for file in file_list:
    for key in cmd_list:
        if file.__contains__(key):
            cmd_set.add(cmd_list[key])

print(cmd_set)
