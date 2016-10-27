# -*- coding: utf-8 -*-

import csv,pandas,api,sqlite3,math
import pandas as pd
import numpy as np

def dbContext():
	conn = sqlite3.connect('search.s3db')
	db = conn.cursor()
	return db

def getProductsCrude(pref):
	table = dbQueryProducts(pref)
	products = []
	for row in table: 
		product = {'dist':row[12],'title':row[2],'popularity':row[3],'shop':{'lat':row[7],'lng':row[8]}}
		products.append(product)
	return products

def coordToeuclideanpoints(cords):
	print cords
	R = 6371
	alpha = math.radians(cords['lat'])
	beta = math.radians(cords['lng'])
	x = R * math.cos(alpha) * math.cos(beta)
	y = R * math.cos(alpha) * math.sin(beta)
	z = R * math.sin(alpha)
	return [x,y,z]
	
def dbQueryProducts(pref):
	d = (pref['radius'] / 1000) * (pref['radius'] / 1000) # This is because sqlite3 does not support sqrt operation needed for euc. norm
	eCoord = coordToeuclideanpoints(pref['position'])
	filter = getTagsFilter(pref)
	db = dbContext()
	# db inject - yes please.
	query = """ SELECT *
	FROM products as p
	JOIN shops AS s ON  s.id = p.shop_id
	JOIN taggings AS ta ON ta.shop_id = s.id
	JOIN tags AS t ON t.id = ta.tag_id
	WHERE 
	{3} 
	((s.xPos-{0}) * (s.xPos-{0}) +
	(s.yPos-{1}) * (s.yPos-{1}) +
	(s.zPos-{2}) * (s.zPos-{2})) < {4}
	ORDER BY p.popularity desc
	LIMIT 10 """.format(eCoord[0],eCoord[1],eCoord[2],filter,d)
	print query
	db.execute(query)
	return db.fetchall()
	
def getTagsFilter(pref):
	tags = pref['tags']
	if not tags: 
		return ""
	filter = "t.tag IN ({0}) AND".format(', '.join(['"{}"'.format(value) for value in tags]))
	return filter
		
	
		
