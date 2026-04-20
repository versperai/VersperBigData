#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

from flask import Flask, render_template, jsonify
from data import SourceData, CorpData, JobData
from data_fake import get_accumulated_data
from hive_data import HiveData

app = Flask(__name__)


@app.route('/')
def index():
    data = HiveData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/corp')
def corp():
    data = CorpData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/job')
def job():
    data = JobData()
    return render_template('index.html', form=data, title=data.title)


@app.route('/api/data')
def api_data():
    """
    返回 HiveData 的 JSON 数据
    """
    data = HiveData()
    return jsonify(data.to_dict())

@app.route('/api/corp')
def api_corp():
    """
    返回 CorpData 的 JSON 数据
    """
    # data = CorpData()
    data = get_accumulated_data('corp', CorpData)  # 模拟实时数据增长
    return jsonify(data.to_dict())


@app.route('/api/job')
def api_job():
    """
    返回 JobData 的 JSON 数据
    """
    # data = JobData()
    data = get_accumulated_data('job', JobData)  # 模拟实时数据增长
    return jsonify(data.to_dict())


@app.route('/api/hive')
def api_hive():
    return jsonify(HiveData().to_dict())

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
