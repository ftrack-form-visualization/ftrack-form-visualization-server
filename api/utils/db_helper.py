# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/09/19 22:24 
"""
from mongo import Mongo


class Form(object):
    db = Mongo('FtrackFormVisualization', 'Info')

    @classmethod
    def get_forms(cls):
        return cls.db.query({}).all(True)

    @classmethod
    def del_form(cls, form_id):
        return cls.db.delete({'id': form_id})
