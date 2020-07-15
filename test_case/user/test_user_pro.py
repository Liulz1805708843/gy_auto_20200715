from idlelib.multicall import r

import pytest
from pinyin.pinyin import f

from tools.api import request_tool
from tools.data import excel_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

@pytest.mark.lock
@pytest.mark.rellname
#注册接口
def test_post_signup(pub_data):
    pub_data["username"] = "自动生成 字符串 3 数字 liuzl"
    pub_data["phone"] = "自动生成 手机号"
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户注册'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
           {
  "phone": "${phone}",
  "pwd": "asd123456",
  "rePwd": "asd123456",
  "userName": "${username}"
}
            '''
    status_code = 200  # 响应状态码
    expect = "注册成功"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"cstId": '$.data.cstId'}]
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title,json_path = json_path)


@pytest.mark.lock
@pytest.mark.rellname
#登录
def test_post_json(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "asd123456",
  "userName": "${username}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


@pytest.mark.rellname
#实名认证
def test_post_realname(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '实名认证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/realname2"  # 接口地址
    header = {"token":pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "cstId": "${cstId}",
  "customerInfo": {
    "birthday": "2020-1-1",
    "certno": "自动生成 身份证号",
    "city": "上海市",
    "cstName": "自动生成 姓名",
    "email": "自动生成 邮箱",
    "province": "上海",
    "sex": 1
  }
}
'''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers=header,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


#修改密码
def test_post_changepwd(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/changepwd"  # 接口地址
    header = {"token":pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "newPwd": "qwe123456",
  "oldPwd": "asd123456",
  "reNewPwd": "qwe123456",
  "userName": "${username}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers = header,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


@pytest.mark.lock
#冻结用户
def test_post_luck(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '锁定用户'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/user/lock"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"userName":'${username}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


@pytest.mark.lock
#解冻用户
def test_post_unluck(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '解冻用户'  # allure报告中二级分类
    title = "解冻用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/user/unLock"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"userName":'${username}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)



#查询单个账户
def test_get_allInfo(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"accountName":'${username}'}
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    #json_path = [{"accountName": '$.data.accountName'}]
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"accountName": '$.data.accountName'}]
    request_tool.request(json_path= json_path,method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)



#查询账户所有信息
def test_get_geaALLACC(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum=1,pageSize=3)  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


#账户解冻
def test_post_accUnLock(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '账户解冻'  # allure报告中二级分类
    title = "账户解冻_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accUnLock"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {
        "accountName":"${accountName}"
    }
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "9999"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


#修改金额
def test_post_json(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值金额'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "accountName": "${username}",
  "changeMoney": 9999
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
