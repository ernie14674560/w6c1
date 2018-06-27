#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0
    try:
        with pd.read_json(file,orient='value') as df:
            times = len(df[df[user_id]==5348].index)
            minutes = sum(df[df[user_id]==5348].minutes)
            return times, minutes
    except:
        return times, minutes


