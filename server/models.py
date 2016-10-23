# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np

# My take from the instructions was that we should try and construct some sort of spatial db
# without actually using any db provider. I hope it goes without saying that no real world 
# application would be using csv files stored in a project catalog as a substitute for a fully
# functional database server.

def getShops():
	with open('data/shops.csv') as s:
		reader = csv.reader(s)
		shops = list(reader)
	return shops
	
def getProductsDf():
	dfShop = pd.read_csv('data/shops.csv')
	dfProduct = pd.read_csv('data/products.csv')
	res = pd.merge(dfShop,dfProduct,how='inner',left_on='id',right_on='shop_id')
	return res[res['quantity']>9]	

def getProducts():
	with open('data/products.csv') as p:
		reader = csv.reader(p)
		products = list(reader)
	return products
		
def getTaggings():
	with open('data/taggings.csv') as t:
		reader = csv.reader(t)
		taggings = list(reader)
	return taggings
		
def getTaggings():
	with open('data/tags.csv') as t:
		reader = csv.reader(t)
		tags = list(reader)
	return tags
	
def getSearchResult():
	products = getProductsDf()
	return dfToJson(products)
	
def dfToJson(df):
	jList = []
	for index, row in df.iterrows():
		jList.append({'shop':{'lat':row['lat'],'lng':row['lng']},'title':row['name']})
	return jList
		
		
	
		
		

		