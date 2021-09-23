# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/09/19 22:19 
"""
from flask import jsonify, request
import shortuuid

from redprint import RedPrint
from .utils.db_helper import Form

forms_rp = RedPrint('forms')


@forms_rp.route('/get_forms')
def get_forms():
    return jsonify({'status': 'success', 'data': Form.get_forms()})


@forms_rp.route('/get_form', methods=['POST'])
def get_form():
    form_id = request.json['id']
    return jsonify({'status': 'success', 'data': Form.get_form(form_id)})


@forms_rp.route('/del_form', methods=['POST'])
def delete_form():
    form_id = request.json['id']
    Form.del_form(form_id)
    return jsonify({'status': 'success', 'data': Form.get_forms()})


@forms_rp.route('/edit_form', methods=['POST'])
def edit_form():
    form_id = request.json['id']
    if not form_id:
        form_id = shortuuid.uuid()

    Form.edit_form(form_id, request.json['formName'], request.json['templates'])
    return jsonify({'status': 'success', 'data': form_id})
