# -*- coding: utf-8 -*-
import json
import csv
import models
from urllib import unquote
from flask import Blueprint, current_app, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

api = Blueprint('api', __name__)


def data_path(filename):
    data_path = current_app.config['DATA_PATH']
    return u"%s/%s" % (data_path, filename)


@api.route('/search', methods=['GET'])
def search():
	mock = [
	{'shop':{'lat':59.33265973,'lng':18.06061238},'title':'MockShop'},
	{'shop':{'lat':59.33829867,'lng':18.11972390},'title':'HM'},
	]
	jdata = json.dumps(mock)
	return products()
	
@api.route('/test', methods=['GET'])
def test():
	return render_template('test.html')

	
@api.route('/products', methods=['GET'])	
def products():
	products = models.getSearchResult()
	return json.dumps(products[:10])
	
@api.route('/getter')	
def getter():
	print "RESP"
	count  = request.args.get('count')
	print count
	radius  = request.args.get('radius')
	print radius
	lat  = request.args.get('lat')
	print lat
	lng  = request.args.get('lng')
	print lng
	tags = request.args.get('tags')
	print tags
	print "END"	
	return "miip"
	
@api.route('/geturl')	
def geturl():
	print "START"
	jdata = json.loads(unquote(request.query_string.partition('&')[0]))
	print "REQUEST BELOW!!!!"
	print jdata['tags'][0]
	print "END"	
	return "miip"
		
	
	
	
