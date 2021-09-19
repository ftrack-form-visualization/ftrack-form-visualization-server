# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/09/19 22:19 
"""
from flask import jsonify, request

from redprint import RedPrint
from .utils.db_helper import Form

forms_rp = RedPrint('forms')


@forms_rp.route('/get_forms')
def get_forms():
    return jsonify({'status': 'success', 'data': Form.get_forms()})


@forms_rp.route('/del_form', methods=['POST'])
def delete_form():
    form_id = request.json['id']
    Form.del_form(form_id)
    return jsonify({'status': 'success', 'data': Form.get_forms()})
