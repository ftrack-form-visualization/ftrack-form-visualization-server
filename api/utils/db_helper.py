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
        return cls.db.query({}, {'_id': 0}).all(True)

    @classmethod
    def get_form(cls, form_id):
        return cls.db.query_one({'id': form_id}, {'_id': 0}) or {}

    @classmethod
    def del_form(cls, form_id):
        return cls.db.delete({'id': form_id})

    @classmethod
    def edit_form(cls, form_id, name, templates):
        return cls.db.update({'name': name, 'templates': templates},
                             {'id': form_id}, True)
