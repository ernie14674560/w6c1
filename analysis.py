#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import pandas as pd


def analysis(file, user_id):
    times = 0
    minutes = 0
    try:
        pd.read_json(file, orient='value') as df:
        times = len(df[df['user_id'] == user_id].index)
        minutes = sum(df[df['user_id'] == user_id].minutes)
        return times, minutes
    except ValueError:
        return times, minutes
