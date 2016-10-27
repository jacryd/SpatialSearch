# -*- coding: utf-8 -*-
import json
import csv
import models
from urllib import unquote
from flask import Blueprint, current_app, jsonify, render_template, request
import sqlite3

api = Blueprint('api', __name__)


def data_path(filename):
    data_path = current_app.config['DATA_PATH']
    return u"%s/%s" % (data_path, filename)


@api.route('/search', methods=['GET'])
def search():
	pref = searchQueryToDictionary(request)
	products = models.getProductsCrude(pref)
	jdata = json.dumps(products)
	return jdata
	

@api.route('/products', methods=['GET'])	
def products():
	products = models.getShops()
	return json.dumps(products[:10])
	
def searchQueryToDictionary(request):
	# surely there is some better way of doing this with automapping just like in c# 
	# but at least we get to feel some sort of nostalgia (written from notepad)
	rad = float(request.args.get('radius'))
	count = int(request.args.get('count'))
	lat = float(request.args.get('lat'))
	lng = float(request.args.get('lng'))
	tags = request.args.getlist('tags')
	pref = {'count':count,'radius':rad,'position':{'lat':lat,'lng':lng},'tags':tags}
	return pref
	
