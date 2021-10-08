#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 11:43
# @Author  : lichong
# @File    : wx_test.py
# @Software: PyCharm
# @Content : 文件说明

import calendar
import time
import datetime

import jsonpath
import requests

# 服务器地址
base_url = "https://saas.fat.supermonkey.com.cn"
# 登录的URL
login_url = "/api/saas/v1/auth/saasUser/login"
# 获取token的URL
token_url = "/api/saas/v1/auth/login/withTenant"
# 新增排课的URL
create_schedule_url = '/api/saas/v1/scheduleConfig/coachView/create'
# 获取指定日期的课表
schedule_list_url = '/api/saas/v1/scheduleConfig/classSchedule/queryList'
# 将排课进行上线
schedule_id_online = '/api/saas/v1/scheduleConfig/classSchedule/onlineAndDisplay'
# 课程id
class_id = None
# 教练id
coach_id = None
# 教室id
box_id = None
# 租户id
tenant_id = None
# 时间
days = None
# 是否对当前时间的下一周进行排课
isTrue = None


def login(name, pwd):
    """
    登录
    :param name:
    :param pwd:
    :return:
    """
    data = {
        "account": name,
        "password": pwd
    }
    res = requests.post(url=base_url + login_url, json=data).json()
    # return res['data']['token']
    return res.get("data").get("token")
    # print(res)

def get_token(tenant_id, name, pwd):
    """
    根据租户id进行获取最后的token
    :param tenant_id:
    :param name:
    :param pwd:
    :return:
    """
    data = {
        "tenantId": tenant_id
    }
    headers = {
        "Authorization": login(name, pwd)
    }
    res = requests.post(url=base_url + token_url, json=data, headers=headers).json()
    print(res)

    return  res['data']['token']

def create_schedule(class_id, coach_id, box_id, tenant_id, days=None, isTrue=True, name=13049376577, pwd=376577,now=None):
    """
    排课功能
    :param class_id: 课程id
    :param coach_id: 教练id，为一个列表
    :param box_id: 教室id
    :param tenant_id: 租户id
    :param name: 用户名
    :param pwd: 密码
    :param days: 日期，例如：2021-05-27
    :param isTrue: 如果为True，则针对所传递日期进行排课，否则则对日期的下周一到周日进行排课
    :return:
    """
    times = [("06:00:00", "06:50:00"),
             ("07:00:00", "07:50:00"),
             ("08:00:00", "08:50:00"),
             ("09:00:00", "09:50:00"),
             ("10:00:00", "10:50:00"),
             ("11:00:00", "11:50:00"),
             ("12:00:00", "12:50:00"),
             ("13:00:00", "13:50:00"),
             ("14:00:00", "14:50:00"),
             ("15:00:00", "15:50:00"),
             ("16:00:00", "16:50:00"),
             ("17:00:00", "17:50:00"),
             ("18:00:00", "18:50:00"),
             ("19:00:00", "19:50:00"),
             ("20:00:00", "20:50:00"),
             ("21:00:00", "21:50:00"),
             ("22:00:00", "22:50:00"),
             ("23:00:00", "23:50:00")]
    #只排当前时间:
    start_time=(datetime.datetime.now() + datetime.timedelta(minutes=0)).strftime('%H:%M:%S')
    end_time=(datetime.datetime.now() + datetime.timedelta(minutes=50)).strftime('%H:%M:%S')
    now_time=[(str(start_time),str(end_time))]
    # now_time=[("15:00:00", "15:50:00")]
    # # times=[("15:00:00", "15:50:00")]
    days=(datetime.datetime.now() + datetime.timedelta(minutes=0)).strftime('%Y-%m-%d')

    headers = {
        "Authorization": get_token(tenant_id, name, pwd)
    }
    if isTrue == True:
        if now:
            for i in now_time:
                s_time = int(time.mktime(time.strptime("{} {}".format(days, i[0]), "%Y-%m-%d %H:%M:%S")) * 1000)
                e_time = int(time.mktime(time.strptime("{} {}".format(days, i[1]), "%Y-%m-%d %H:%M:%S")) * 1000)
                data = {
                    "classId": class_id,
                    "mainCoachId": coach_id,
                    "extraTuitionFee": 0,
                    "fullNumber": 30,
                    "scheduleRange": {
                        "startTimestamp": s_time,
                        "endTimestamp": e_time
                    },
                    "boxId": box_id,
                    "confirmAgain": False,
                    "schedulePrice": 532000
                }
                try:
                    print(data)
                    res = requests.post(url=base_url + create_schedule_url, json=data, headers=headers).json()
                    # print(res)
                    # print("{}-{}时间段排课成功".format(days + " " + i[0], days + " " + i[1]))
                    print(res)
                except:
                    raise ("{}-{}时间段排课失败".format(days + " " + i[0], days + " " + i[1]))
            data = days
            _data = datetime.datetime.strptime(data, "%Y-%m-%d")
            oneday = datetime.timedelta(days=1)
            e_data = _data + oneday
            startTimestamp = int(time.mktime(time.strptime(str(_data), "%Y-%m-%d %H:%M:%S")) * 1000)
            endTimestamp = int(time.mktime(time.strptime(str(e_data), "%Y-%m-%d %H:%M:%S")) * 1000)
            schedule_list_ids = []
            schedule_online(startTimestamp, endTimestamp, headers,schedule_list_ids)

        else:
            for i in times:
                s_time = int(time.mktime(time.strptime("{} {}".format(days, i[0]), "%Y-%m-%d %H:%M:%S")) * 1000)
                e_time = int(time.mktime(time.strptime("{} {}".format(days, i[1]), "%Y-%m-%d %H:%M:%S")) * 1000)
                data = {
                    "classId": class_id,
                    "mainCoachId": coach_id,
                    "extraTuitionFee": 0,
                    "fullNumber": 12,
                    "scheduleRange": {
                        "startTimestamp": s_time,
                        "endTimestamp": e_time
                    },
                    "boxId": box_id,
                    "confirmAgain": False,
                    "schedulePrice": 5300
                }
                try:
                    # print("12344")
                    print(data)
                    res = requests.post(url=base_url + create_schedule_url, json=data, headers=headers).json()
                    print(res)
                    # print("{}-{}时间段排课成功".format(days + " " + i[0], days + " " + i[1]))
                except:
                    raise ("{}-{}时间段排课失败".format(days + " " + i[0], days + " " + i[1]))
            data = days
            _data = datetime.datetime.strptime(data, "%Y-%m-%d")
            oneday = datetime.timedelta(days=1)
            e_data = _data + oneday
            startTimestamp = int(time.mktime(time.strptime(str(_data), "%Y-%m-%d %H:%M:%S")) * 1000)
            endTimestamp = int(time.mktime(time.strptime(str(e_data), "%Y-%m-%d %H:%M:%S")) * 1000)
            schedule_list_ids = []
            schedule_online(startTimestamp, endTimestamp, headers,schedule_list_ids)

    else:
        __time = _get_time(days)
        for m in __time:
            for n in times:
                s_time = int(time.mktime(time.strptime("{} {}".format(m, n[0]), "%Y-%m-%d %H:%M:%S")) * 1000)
                e_time = int(time.mktime(time.strptime("{} {}".format(m, n[1]), "%Y-%m-%d %H:%M:%S")) * 1000)
                data = {
                    "classId": class_id,
                    "mainCoachId": coach_id,
                    "extraTuitionFee": 0,
                    "fullNumber": 12,
                    "scheduleRange": {
                        "startTimestamp": s_time,
                        "endTimestamp": e_time
                    },
                    "boxId": box_id,
                    "confirmAgain": False,
                    "schedulePrice": 5300
                }
                try:
                    res=requests.post(url=base_url + create_schedule_url, json=data, headers=headers).json()
                    # print("78787997")
                    # print("{}-{}时间段排课成功".format(m + " " + n[0], m + " " + n[1]))
                    print(res)
                except:
                    raise "{}-{}时间段排课失败".format(m + " " + n[0], m + " " + n[1])
        oneday = datetime.timedelta(days=1)
        schedule_list_ids = []
        for i in __time:
            s_data = datetime.datetime.strptime(i, "%Y-%m-%d")
            e_data = s_data + oneday
            startTimestamp = int(time.mktime(time.strptime(str(s_data), "%Y-%m-%d %H:%M:%S")) * 1000)
            endTimestamp = int(time.mktime(time.strptime(str(e_data), "%Y-%m-%d %H:%M:%S")) * 1000)
            schedule_online(startTimestamp, endTimestamp, headers, schedule_list_ids)


def schedule_online(startTimestamp, endTimestamp, headers, schedule_list_ids):
    """
    将未生效的课表改为上线并展示
    :param startTimestamp: 开始时间
    :param endTimestamp: 结束时间
    :param headers: 请求头信息
    :param schedule_list_ids: 未生效的课表id，列表
    :return: None
    """
    data_list = {"filters":
                     {"attendClassTimestampRange":
                          {"startTimestamp": startTimestamp,
                           "endTimestamp": endTimestamp
                           },
                      "classScheduleStatus": []
                      },
                 "sorter": {},
                 "pagination":
                     {"pageSize": 100,
                      "pageNo": 1}}
    schedule_list = requests.post(url=base_url + schedule_list_url, json=data_list, headers=headers).json()
    date = schedule_list.get("data").get("list")
    for n in date:
        schedule_list_ids.append(n.get("classScheduleId"))
    res=requests.post(url=base_url + schedule_id_online, json={"idList": schedule_list_ids}, headers=headers)
    print(res.json())


def _get_time(_time):
    """
    获取指定日期的下周一到周日
    :param _time: 例如：2021-05-27
    :return:
    """
    e_time_week = datetime.datetime.strptime(_time, "%Y-%m-%d")
    week = datetime.datetime.weekday(e_time_week)
    oneday = datetime.timedelta(days=1)
    m1 = calendar.MONDAY
    while week != m1:
        e_time_week += oneday
        week = datetime.datetime.weekday(e_time_week)
    day_week = []
    for i in range(7):
        __time = (str(e_time_week).split(" ")[0])
        day_week.append(__time)
        e_time_week += oneday
    print(day_week)
    return day_week


def classSchedule_deleteList():
    url='https://saas-web.fat.supermonkey.com.cn/api/saas/v1/scheduleConfig/classSchedule/deleteList'
    cookie=''
    requests.request(method='post',headers='',)



class AutomaticCourseScheduling():

    #登录url
    saasUser_login_url="https://saas.fat.supermonkey.com.cn/api/saas/v1/auth/saasUser/login"
    # 获取token的URL
    token_url = "https://saas.fat.supermonkey.com.cn/api/saas/v1/auth/login/withTenant"
    # 新增排课的URL
    create_schedule_url = 'https://saas.fat.supermonkey.com.cn/api/saas/v1/scheduleConfig/coachView/create'
    # 获取指定日期的课表
    schedule_list_url = 'https://saas.fat.supermonkey.com.cn/api/saas/v1/scheduleConfig/classSchedule/queryList'
    # 将排课进行上线
    schedule_id_online = 'https://saas.fat.supermonkey.com.cn/api/saas/v1/scheduleConfig/classSchedule/onlineAndDisplay'

    def cms_login(self,name=13049376577,pwd=376577):
        """saas登录"""
        data={
        "account": name,
        "password": pwd
    }
        res=requests.request('post',url=self.saasUser_login,json=data).json()
        return jsonpath.jsonpath(res,'$..token')

    def get_token(self,tenant_id=26257):
        """获取租户token"""
        data = {
            "tenantId": tenant_id
        }
        headers = eval(self.cms_login()[0])
        res = requests.post(url=self.token_url, json=data, headers=headers).json()
        return res['data']['token']

    def create_schedule(self):
        pass


if __name__ == "__main__":
    pass
    # print(login(name=13049376577, pwd=376577))
    # print(get_token(tenant_id=26257, name=13049376577, pwd=376577))
    # print('11111',AutomaticCourseScheduling().cms_login())
    # print(AutomaticCourseScheduling().get_token())
    # create_schedule(class_id=5020, coach_id=[3216262], box_id=2375, tenant_id=26257, isTrue=True,now=True)
    # res=login(name=18318051036, pwd="051036")
    # print(res)
    # res.get

    # start_time = datetime.datetime.now().strftime('%H:%M:%S')
    # end_time = (datetime.datetime.now() + datetime.timedelta(minutes=50)).strftime('%H:%M:%S')
    # print(start_time,end_time)

    # datetime.datetime.now().strftime('%H:%M:%S')

    # def time_diff(timestamp):
    #     onlineTime = datetime.datetime.fromtimestamp(timestamp)
    #     localTime = datetime.datetime.now()
    #     result = localTime - onlineTime
    #     hours = int(result.seconds / 3600)
    #     minutes = int(result.seconds % 3600 / 60)
    #     seconds = result.seconds % 3600 % 60
    #     print("当前网络时间：{0}".format(localTime))
    #     print("上次在线时间：{0}".format(onlineTime))
    #     print("{0}天{1}时{2}分{3}秒前在线".format(result.days, hours, minutes, seconds))
    #
    #
    # times = int(time.time()) - 80
    # time_diff(times)

    # start=(datetime.datetime.now() + datetime.timedelta(minutes=0)).strftime('%H:%M:%S')
    # end=start+((datetime.timedelta(minutes=50)).strftime('%H:%M:%S'))
    # print(end)
    # start=(datetime.datetime.now() + datetime.timedelta(minutes=0)).strftime('%Y-%m-%d')
    # print(start)
    # login(name=13049376577, pwd="376577")