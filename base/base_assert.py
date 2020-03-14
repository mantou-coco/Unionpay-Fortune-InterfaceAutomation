import json
from base import base_excel


#断言结果与预期结果是否符合
def assert_res(em, res):
    if em.expect_way == 'json':
        assert res.json() == json.loads(em.expect_res)
    elif em.expect_way == 'status_code':
        assert res.status_code == int(em.expect_res)
    elif em.expect_way == 'contain_data':
        assert em.expect_res in res.text

# 将data插入Excel“数据”中
def write_data(case_id, data):
    return base_excel.excel_write_data(base_excel.get_rows_number_with_case_id(case_id), 7, data)

# 将text插入Excel“结果数据”中
def write_result_data(case_id, res):
    return base_excel.excel_write_data(base_excel.get_rows_number_with_case_id(case_id), 14, res.text)


