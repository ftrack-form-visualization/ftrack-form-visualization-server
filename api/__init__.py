# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/09/19 22:17 
"""
from flask import Blueprint

from .forms import forms_rp

api = Blueprint('api', __name__)
forms_rp.register(api)
