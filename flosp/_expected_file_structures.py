import numpy as np
possible_pkls_list = ['ED.pkl','NOTAPICKLE.pkl']

dataRAW_expected_dtypes = {
'dept_patid':[np.float,np.int,np.int64,np.str],
'hosp_patid':[np.float,np.int,np.int64,np.str],
'age':[np.int,np.int64],
'gender':[np.object],
'site':[np.object],
'arrive_date':[np.object],
'arrive_time':[np.object],
'arrive_datetime':[np.dtype('datetime64[ns]')],
'arrive_mode':[np.object],
'arrive_hour':[np.float,np.int,np.int64],
'arrive_dayofweek':[np.float,np.int,np.int64],
'arrive_week':[np.float,np.int,np.int64],
'arrive_month':[np.float,np.int,np.int64],
'arrive_year':[np.float,np.int,np.int64],
'arrive_dayofweek_name':[np.object],
'arrive_flag_wkend':[np.int],
'first_triage_time':[np.object],
'first_triage_datetime':[np.dtype('datetime64[ns]')],
'first_dr_time':[np.object],
'first_dr_datetime':[np.dtype('datetime64[ns]')],
'first_adm_request_time':[np.object],
'first_adm_request_datetime':[np.dtype('datetime64[ns]')],
'adm_referral_loc':[np.object],
'depart_time':[np.object],
'depart_date':[np.object],
'depart_datetime':[np.dtype('datetime64[ns]')],
'depart_method':[np.object],
'depart_hour':[np.float,np.int,np.int64],
'depart_dayofweek':[np.float,np.int,np.int64],
'depart_week':[np.float,np.int,np.int64],
'depart_month':[np.float,np.int,np.int64],
'depart_year':[np.float,np.int,np.int64],
'depart_dayofweek_name':[np.str],
'depart_flag_wkend':[np.int],
'waiting_time':[np.float],
'breach_flag':[np.int],
'adm_flag':[np.int],
'stream':[np.float,np.int,np.int64,np.str],
'minutes_today':[np.int],
'minutes_tomo':[np.int],
'breach_datetime':[np.dtype('datetime64[ns]')],
'arr_triage_wait':[np.float,np.float64],
'first_adm_request_datetime':[np.dtype('datetime64[ns]')],
'arr_triage_wait':[np.float,np.float64],
'arr_dr_wait':[np.float,np.float64],
'arr_adm_req_wait':[np.float,np.float64],
'adm_req_dep_wait':[np.float,np.float64],
'dr_adm_req_wait':[np.float,np.float64],
'dr_dep_wait':[np.float,np.float64]
}

dataRAW_expected_cols = {
'hosp_patid':'',
'age':'check column name',
'gender':'',
'arrive_datetime':'use ',
'arrive_mode':'',
'arrive_hour':'make_callender_columns',
'arrive_dayofweek':'make_callender_columns',
'arrive_month':'make_callender_columns',
'arrive_dayofweek_name':'make_callender_columns',
'arrive_date':'make_callender_columns',
'arrive_week':'make_callender_columns',
'first_triage_datetime':'create_datetime_from_time',
'first_dr_datetime':'create_datetime_from_time',
'first_adm_request_datetime':'create_datetime_from_time',
'adm_referral_loc':'',
'depart_datetime':'',
'depart_method':'',
'depart_hour':'make_callender_columns',
'depart_dayofweek':'make_callender_columns',
'depart_week':'make_callender_columns',
'depart_month':'make_callender_columns',
'depart_dayofweek_name':'make_callender_columns',
'depart_date':'make_callender_columns',
'waiting_time':'',
'breach_flag':'',
'adm_flag':'',
'stream':'',
'minutes_today':'',
'minutes_tomo':'',
'breach_datetime':'',
'arr_triage_wait':'',
'arr_dr_wait':'',
'arr_adm_req_wait':'',
'adm_req_dep_wait':'',
'dr_adm_req_wait':'',
'dr_dep_wait':''

}
