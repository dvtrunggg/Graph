import networkx as nx
import matplotlib.pyplot as plt
import json_lines
import json
import re
import math
import sys
import numpy as np
import pandas as pd

#{"Myanmar,South Sudan": "9 hours, 25 minutes"}

def file(fileName):
	G = nx.Graph()
	with open(fileName, 'rb') as f:		
		for line in json_lines.reader(f):	
			for key in line:
				countries = key.split(',')		
				times = line[key].split(',')		
				stringTimes = ''.join(times)	
				t = stringTimes.split()	
				timeTotal = countTime(t)	
				G.add_edge(countries[0], countries[1], weight = timeTotal)
	return G

# hàm dùng để hỗ trợ check giờ với định dạng list = ["9", "hours", "25", "minutes"]
def countTime(list):
	min = 0
	h = 0 
	if 'hours' not in list:		#["25", "minutes"]
		h = 0
		min = int(list[0])
	elif 'minutes' not in list:	#["9", "hours"]
		min = 0 
		h = int(list[0])
	else:		#["9", "hours", "25", "minutes"]
		h = int(list[0])
		min = int(list[2])

	timeTotal = h * 60 + min
	return timeTotal

def makeG3():
	G1 = file('g1.jl')
	G2 = file('g2.jl')
	G3 = nx.Graph()
	#list các quốc gia trong graph ( là các đỉnh)
	for a in list(G1):
		for b in list(G2):
			data1 = 0
			data2 = 0
			#has_edge: ktra có tồn tại cạnh giữa 2 đỉnh a, b
			if G1.has_edge(a, b) and G2.has_edge(a, b) == False:

				data1 = G1.get_edge_data(a, b)['weight']
				G3.add_edge(a, b, weight = data1)

			if G2.has_edge(a, b) and G1.has_edge(a, b) == False:
				data2 = G2.get_edge_data(a, b)['weight']
				G3.add_edge(a, b, weight = data2)

			if G2.has_edge(a, b) and G1.has_edge(a, b):
				data3 = min(G1.get_edge_data(a, b)['weight'], G2.get_edge_data(a, b)['weight'])
				G3.add_edge(a, b, weight = data3)

	return G3
# chuyển và lưu vào file luôn 
def convert_adjacencyMatrix_andSave(Graph, fileOut):
	matrix = nx.to_numpy_matrix(Graph, Graph.nodes, int)	#có sẵn trong nx python
	np.savetxt(fileOut, matrix, fmt = '%.0f') 

def BFS_Traversal(Graph):
	print('Quoc gia bat dau: ')
	start = input()

	l = list(Graph)
	if start not in l:
		print('Khong co quoc gia nay trong danh sach hoac ban da nhap sai ten.')
	else:
		print('\nDuyet BFS tu: ', start, ': ')
		a = list(nx.bfs_tree(Graph, start))
		print(a)

def topDeath():
	df = pd.read_csv('Info.csv')

	dataSort = df.sort_values(by= ['Deaths'], ascending = False)	

	
	countries = dataSort['Country'].tolist()	
	top_20Countries = countries[:20]	
	
	G = nx.Graph()
	G3 = makeG3()
	for country1 in top_20Countries:
		for country2 in top_20Countries:
			if G3.has_edge(country1, country2) == True:
				data = G3.get_edge_data(country1, country2)['weight']
				G.add_edge(country1, country2, weight = data)
	return G

def topRecoveredRate():
	df = pd.read_csv('Info.csv')
	
	data = df.values		 

	Recovered = df['Recovered']
	Cases = df['Cases']
	rate = Recovered/Cases
	for i in range(len(rate)):
		if math.isnan(rate[i]) == True:
			rate[i] = 0

	df['Rate'] = rate		
	dataSort = df.sort_values(by= ['Rate'], ascending = False)	

	
	countries = dataSort['Country'].tolist()	
	top_20Countries = countries[:20]	
	G = nx.Graph()
	G3 = makeG3()
	for country1 in top_20Countries:
		for country2 in top_20Countries:
			if G3.has_edge(country1, country2) == True:
				data = G3.get_edge_data(country1, country2)['weight']
				G.add_edge(country1, country2, weight = data)

	return G

# cau 2.3.1
def Travel(k):
	df = pd.read_csv('Info.csv')
	Deaths = df['Deaths']
	Cases = df['Cases']
	rate = Deaths/Cases
	for i in range(len(rate)):
		if math.isnan(rate[i]) == True:	
			rate[i] = 0
	df['Rate'] = rate


	Asia = df[df['Area'] == 'Asia'].sort_values(by= ['Rate'], ascending = False)	# filter theo 'Asia ' rồi sort
	America = df[df['Area'] == 'America'].sort_values(by= ['Rate'], ascending = False)
	Europe = df[df['Area'] == 'Europe'].sort_values(by= ['Rate'], ascending = False)
	Oceania = df[df['Area'] == 'Oceania'].sort_values(by= ['Rate'], ascending = False)
	Africa = df[df['Area'] == 'Africa'].sort_values(by= ['Rate'], ascending = False)

	asia_Countries = Asia['Country'].tolist()
	america_Countries = America['Country'].tolist()
	europe_Countries = Europe['Country'].tolist()
	oceania_Countries = Oceania['Country'].tolist()
	africa_Countries = Africa['Country'].tolist()
	
	top_Asia = asia_Countries[:k]		# k quốc gia 
	top_America = america_Countries[:k]
	top_Europe = europe_Countries[:k]
	top_Oceania = oceania_Countries[:k]
	top_Africa = africa_Countries[:k]

	top_Countries = top_Asia + top_America + top_Europe + top_Oceania + top_Africa	# nối các list lại vào 1 list duy nhất 

	
	G = nx.Graph()
	G3 = makeG3()
	for country1 in top_Countries:
		for country2 in top_Countries:
			if G3.has_edge(country1, country2) == True:
				data = G3.get_edge_data(country1, country2)['weight']
				G.add_edge(country1, country2, weight = data)
	G_result = nx.Graph()
	G_result = nx.minimum_spanning_tree(G)		# cây khung tối thiểu 
	return G_result

def lets_Flight():
	G3 = makeG3()
	G2 = file('g2.jl')
	with open('Travel.txt') as f:
		list2 = []
		list3 = []
		countries = f.read().split(',')
		for i in range(len(countries)-1):
			list_Temp3 = nx.shortest_path(G3, countries[i], countries[i+1])		# tìm đường đi ngắn nhất giữa các quốc gia trong G3
			list3 = list3 + list_Temp3	# list_Temp3 là các mảng nx.shortest_path(...) nên cần phải gộp vào 1 list 
			
			list_Temp2 = nx.shortest_path(G2, countries[i], countries[i+1])		# tìm đường đi ngắn nhất giữa các quốc gia trong G2
			list2 = list2 + list_Temp2
		
		if list2 is list3:
			print('Kha thi')
		else:
			print('ko kha thi')
			print('Duong di moi la:')

		# list2:['Germany', 'Vietnam', 'Vietnam', 'Mozambique', 'Mozambique', 'Poland', 'Saint Lucia']
		list_Result = list(dict.fromkeys(list2))	# xóa các quốc gia trùng nhau

		print(list_Result)
		for i in range(0,len(list_Result)-1):
			 print(list_Result[i], '->',list_Result[i+1],': ',G2.get_edge_data(list_Result[i], list_Result[i+1])['weight'])

if __name__ == '__main__':
	G1 = file('g1.jl')
	G2 = file('g2.jl')
	G3 = makeG3()
	convert_adjacencyMatrix_andSave(G1, 'G1.txt')
	convert_adjacencyMatrix_andSave(G2, 'G2.txt')
	convert_adjacencyMatrix_andSave(G3, 'G3.txt')
	BFS_Traversal(G3)
	
	nx.draw(topDeath(), with_labels=True) 
	plt.show()

	nx.draw(topRecoveredRate(), with_labels=True) 
	plt.show()

	nx.draw(Travel(1), with_labels=True) 
	plt.show()
	lets_Flight()