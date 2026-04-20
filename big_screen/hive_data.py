#!/usr/bin/env python3
import copy
import random
from pyhive import hive

def get_hive_connection():
    return hive.Connection(host='localhost', port=10000, database='default')

_data_cache = None

def get_hive_data():
    global _data_cache
    if _data_cache is None:
        _data_cache = HiveData()
    else:
        add_random(_data_cache)
    return _data_cache

def add_random(obj, factor=0.05):
    """给指标增加随机变化"""
    def rand_num(v):
        new_v = v * (1 + random.uniform(-factor, factor))
        return max(0, int(new_v))
    
    if obj.counter and 'value' in obj.counter:
        obj.counter['value'] = rand_num(obj.counter['value'])
    if obj.counter2 and 'value' in obj.counter2:
        obj.counter2['value'] = rand_num(obj.counter2['value'])
    
    for key in ['echart1_data', 'echart2_data', 'echart4_data', 'echarts3_1_data']:
        data = getattr(obj, key, None)
        if data and data.get('data'):
            for item in data['data']:
                if 'value' in item and isinstance(item['value'], list):
                    item['value'] = [rand_num(x) for x in item['value']]
                elif 'value' in item and isinstance(item['value'], (int, float)):
                    item['value'] = rand_num(item['value'])

class HiveData:
    def __init__(self):
        pv_total = 89660671
        uv_total = 987991
        
        self.title = '淘宝用户行为数据分析'
        self.counter = {'name': '总访问量PV', 'value': pv_total}
        self.counter2 = {'name': '总用户量UV', 'value': uv_total}
        self.counter3 = {'name': '复购率', 'value': '66.01%'}

        self.echart4_data = {
            'title': '日访问量趋势',
            'xAxis': ['11-25', '11-26', '11-27', '11-28', '11-29', '11-30', '12-01', '12-02', '12-03'],
            'data': [
                {'name': 'PV', 'value': [9435250, 9475589, 8966429, 8849193, 9241648, 9442000, 10002284, 12475204, 10709289]},
                {'name': 'UV', 'value': [705571, 713522, 709207, 708339, 719356, 730809, 753166, 941709, 917531]}
            ]
        }

        self.echart1_data = {
            'title': '用户行为分布',
            'data': [
                {'name': '点击PV', 'value': 89660671},
                {'name': '收藏', 'value': 2888258},
                {'name': '购物车', 'value': 5530446},
                {'name': '购买', 'value': 2015807},
            ]
        }

        self.chart_conversion = {
            'title': '用户行为转化率',
            'pv': 88596886,
            'fav': 2852536,
            'cart': 5466118,
            'fav_cart': 8318654,
            'buy': 1998944,
            'pv2favcart': 0.0939,
            'favcart2buy': 0.2403,
            'pv2buy': 0.0226,
        }

        self.echart2_data = {
            'title': '每小时活跃分布',
            'xAxis': [str(i) for i in range(24)],
            'data': [
                {'name': 'PV', 'value': [3042342, 3728498, 4334810, 4213518, 4255794, 4653933, 4642054, 4806704, 4607743, 4203395, 4313516, 5430878, 6586331, 7538382, 7443069, 5599901, 2747149, 1278813, 692240, 471981, 403765, 522063, 1097628, 1982379]},
                {'name': '购买', 'value': [64916, 96134, 127932, 122046, 118591, 123426, 122171, 122728, 116444, 101300, 95907, 115032, 133859, 145431, 138263, 100070, 52422, 20948, 10748, 7212, 6044, 7351, 16251, 33718]}
            ]
        }

        self.echarts3_1_data = {
            'title': '一周活跃分布',
            'xAxis': ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
            'data': [
                {'name': 'PV', 'value': [10709289, 8966429, 8849193, 9241648, 9442000, 10002284, 12475204]},
                {'name': '购买', 'value': [235473, 218401, 211754, 223077, 222235, 212849, 259550]}
            ]
        }
        self.echarts3_2_data = {
            'title': '消费频率Top10',
            'data': [
                {'name': 'user_486458', 'value': 262},
                {'name': 'user_866670', 'value': 175},
                {'name': 'user_702034', 'value': 159},
                {'name': 'user_107013', 'value': 130},
                {'name': 'user_1014116', 'value': 118},
                {'name': 'user_432739', 'value': 112},
                {'name': 'user_500355', 'value': 110},
                {'name': 'user_537150', 'value': 109},
                {'name': 'user_1003412', 'value': 100},
                {'name': 'user_919666', 'value': 97},
            ]
        }
        self.echarts3_3_data = {'title': '兴趣分布', 'data': []}
        self.echart5_data = {
            'title': '销量Top10商品',
            'data': [
                {'name': 'item_3122135', 'value': 1408},
                {'name': 'item_3031354', 'value': 942},
                {'name': 'item_3964583', 'value': 671},
                {'name': 'item_2560262', 'value': 658},
                {'name': 'item_2964774', 'value': 614},
                {'name': 'item_740947', 'value': 553},
                {'name': 'item_1910706', 'value': 546},
                {'name': 'item_1116492', 'value': 512},
                {'name': 'item_705557', 'value': 495},
                {'name': 'item_4443059', 'value': 490},
            ]
        }
        self.echart6_data = {
            'title': '销量Top10类目',
            'xAxis': ['cat_1464116', 'cat_2735466', 'cat_2885642', 'cat_4145813', 'cat_4756105', 'cat_4801426', 'cat_982926', 'cat_2640118', 'cat_4159072', 'cat_1320293'],
            'data': [
                {'name': 'cat_1464116', 'value': 34248},
                {'name': 'cat_2735466', 'value': 33426},
                {'name': 'cat_2885642', 'value': 31619},
                {'name': 'cat_4145813', 'value': 31418},
                {'name': 'cat_4756105', 'value': 28021},
                {'name': 'cat_4801426', 'value': 26258},
                {'name': 'cat_982926', 'value': 24570},
                {'name': 'cat_2640118', 'value': 18116},
                {'name': 'cat_4159072', 'value': 17917},
                {'name': 'cat_1320293', 'value': 16948},
            ]
        }
        self.map_1_data = {'symbolSize': 100, 'data': []}

    @property
    def echart1(self):
        return {'title': self.echart1_data['title'], 'xAxis': [i['name'] for i in self.echart1_data['data']], 'series': [i['value'] for i in self.echart1_data['data']]}

    @property
    def echart2(self):
        series_data = [i['value'] for i in self.echart2_data['data']]
        return {'title': self.echart2_data['title'], 'xAxis': [str(i) for i in range(24)], 'series': series_data[0] if series_data else []}

    @property
    def echarts3_1(self):
        return {'title': self.echarts3_1_data['title'], 'xAxis': self.echarts3_1_data['xAxis'], 'data': self.echarts3_1_data['data']}

    @property
    def echarts3_2(self):
        return {'title': self.echarts3_2_data['title'], 'xAxis': [i['name'] for i in self.echarts3_2_data['data']], 'data': self.echarts3_2_data['data']}

    @property
    def echarts3_3(self):
        return self.echarts3_3_data

    @property
    def echart4(self):
        return {'title': self.echart4_data['title'], 'xAxis': self.echart4_data['xAxis'], 'names': [i['name'] for i in self.echart4_data['data']], 'data': self.echart4_data['data']}

    @property
    def echart5(self):
        return {'title': self.echart5_data['title'], 'xAxis': [i['name'] for i in self.echart5_data['data']], 'series': [i['value'] for i in self.echart5_data['data']]}

    @property
    def echart6(self):
        return {'title': self.echart6_data['title'], 'xAxis': self.echart6_data['xAxis'], 'series': [i['value'] for i in self.echart6_data['data']]}

    @property
    def map_1(self):
        return {'symbolSize': self.map_1_data['symbolSize'], 'data': self.map_1_data['data']}

    def to_dict(self):
        return {
            'title': self.title,
            'counter': self.counter,
            'counter2': self.counter2,
            'counter3': self.counter3,
            'echart1': {'title': self.echart1_data['title'], 'xAxis': [i['name'] for i in self.echart1_data['data']], 'series': [i['value'] for i in self.echart1_data['data']]},
            'echart2': {'title': self.echart2_data['title'], 'xAxis': self.echart2_data['xAxis'], 'data': self.echart2_data['data'], 'series': self.echart2_data['data'][0]['value']},
            'echarts3_1': {'title': self.echarts3_1_data['title'], 'xAxis': self.echarts3_1_data['xAxis'], 'data': [d['value'] for d in self.echarts3_1_data['data']]},
            'echarts3_2': self.echarts3_2_data,
            'echarts3_3': self.echarts3_3_data,
            'echart4': self.echart4_data,
            'echart5': {'title': self.echart5_data['title'], 'xAxis': [i['name'] for i in self.echart5_data['data']], 'series': [i['value'] for i in self.echart5_data['data']]},
            'echart6': {'title': self.echart6_data['title'], 'xAxis': self.echart6_data['xAxis'], 'series': [i['value'] for i in self.echart6_data['data']]},
            'map_1': self.map_1_data,
            'chart_conversion': self.chart_conversion,
        }