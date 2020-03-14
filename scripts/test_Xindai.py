import json
import requests
import pytest
import jsonpath
import allure
from base import base_excel
from base import base_assert
from base.base_fixture import deal_fixture
from base.base_allure import get_description


#处理用例编号
def get_case_id(prefix, count):
    lis = list()
    for i in range(count):
        lis.append('%s_%03d' % (prefix, i + 1))
    return lis


#处理cookies
def get_cookies(em):
    if em.cookies is not None:
        return eval(em.cookies)

#处理传参数据
def get_data(em):
    if em.data is not None:
        return em.data.encode('utf-8')




class TestFinancial(object):
    Base_url = 'https://unionpay.ylzcf.com/finance'

    #初始化订单获取orderNo并用于下个接口传参
    def Initialize_order(self, fixture_case_id,  behind_case_id):
        fix_em = base_excel.get_item_with_case_id(fixture_case_id)
        fix_res = requests.get(self.Base_url + fix_em.url, data=get_data(fix_em), headers=json.loads(fix_em.headers),
                           cookies=get_cookies(fix_em))
        base_assert.assert_res(fix_em, fix_res)
        result = json.loads(fix_res.text)
        order = str(jsonpath.jsonpath(result, "$..orderNo"))[2:27]
        data = {
            "token": "915mPAYKlUGATok79dDNlOS7hMNHPPrfGdl1Ln6F2TI9uo/PpVtHLBhdBggHMNMU-1500289aa5f37422b01fcde3d6cc4b300",
            "orderNo": order
        }
        base_assert.write_data(behind_case_id, json.dumps(data))


    #@pytest.mark.skip
    @pytest.mark.parametrize("case_id", get_case_id('fixture', 2))
    def test_post_fixture(self, case_id):
        em = base_excel.get_item_with_case_id(case_id)
        allure.dynamic.title(em.title)
        res = requests.post(self.Base_url + em.url, data=get_data(em), headers=json.loads(em.headers),
                            cookies=get_cookies(em))
        base_assert.assert_res(em, res)
        base_assert.write_result_data(case_id, res)
        allure.dynamic.description_html(get_description(em))



    #@pytest.mark.skip
    #@pytest.mark.parametrize("case_id", ["post_007"])
    @pytest.mark.parametrize("case_id", get_case_id('post', 8))
    def test_post(self, case_id):
        em = base_excel.get_item_with_case_id(case_id)
        allure.dynamic.title(em.title)
        deal_fixture(self, em, case_id)
        res = requests.post(self.Base_url + em.url, data=get_data(em),  headers=json.loads(em.headers),
                            cookies=get_cookies(em))
        base_assert.assert_res(em, res)
        base_assert.write_result_data(case_id, res)
        allure.dynamic.description_html(get_description(em))




    @pytest.mark.skip
    @pytest.mark.parametrize("case_id", get_case_id('get', 3))
    def test_get(self, case_id):
        em = base_excel.get_item_with_case_id(case_id)
        allure.dynamic.title(em.title)
        res = requests.get(em.url, data=get_data(em), headers=json.loads(em.headers),
                           cookies=get_cookies(em))
        base_assert.assert_res(em, res)
        base_assert.write_result_data(case_id, res)
        allure.dynamic.description_html(get_description(em))










