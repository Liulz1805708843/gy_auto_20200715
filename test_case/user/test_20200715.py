import random

import allure

from config.conf import API_URL
import requests

@allure.feature("用户管理")
@allure.story("模块")

@allure.title("扣款接口")
def test_charg(db):
    with allure.step("第一步、执行sql语句"):
        res = db.select_execute("SELECT account_name FROM t_cst_account WHERE t_cst_account.status = 0 AND account_name IS NOT NULL")
    with allure.step("第二步、随机选择账号，并选取下标为1的数据"):
        accountName = random.choice(res)[0]
    with allure.step("第三步、输入数据"):
        json_data =  {
            "accountName": accountName,
            "changeMoney": 9000
        }
    with allure.step("第四步、发送请求"):
        r = requests.request("POST",API_URL +"/acc/charge",json = json_data)
    with allure.step("第五步、查看请求"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求正文",allure.attachment_type.TEXT)
    with allure.step("第五步、查看响应"):
        allure.attach(str(r.status_code),"响应状态吗",allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响应头",allure.attachment_type.TEXT)
        allure.attach(r.text,"响应正文",allure.attachment_type.TEXT)
    with allure.step("第六步、断言"):
        allure.attach(r.text,"实际结果",allure.attachment_type.TEXT)
        allure.attach("账户余额不足","预期结果",allure.attachment_type.TEXT)
        assert "账户余额不足" in r.text
    pass