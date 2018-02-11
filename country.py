# -*- coding: UTF-8 -*-
import language, math

class position(object):
	def __init__(self, x, y):
		#经度
		self.longitude = x
		#纬度
		self.latitude = y
	def dis(self, other):
		pass

def getdistance(orgin, destination):
	return 0.02 * math.sqrt(orgin.longitude * destination.longitude + destination.latitude * orgin.latitude) 


class country(object):
	k = 0.8  #人口迁移数据
	def __init__(self, name, gdp, nr, position, ml, *sl):
		#language
		self.name = name
		self.gdp = gdp
		self.natrual_rate = nr
		self.position = position
		self.major_lan = ml
		self.second_lan = list(sl)
		self.population = self.major_lan.population
		for i in  self.second_lan:
			self.population += i.population

	def grow(self):
		t = natrual_rate * self.population
		self.major_lan.population += t
		self.population += t

	def flow_in(self, language):
		self.population += language.population
		if language.name == self.major_lan.name:
			self.major_lan.mix(language)
		else:
			for i in self.second_lan:
				if i.name == language.name :
					i.mix(language)
					return
			self.second_lan.append(language)

	def Garavity(self, destination):
		return country.k * self.population * destination.gdp / (destination.population * self.gdp * getdistance(self.position, destination.position)) 

	def flow(self, other):
		number = math.floor(self.Garavity(other))
		#print(number)
		self.population -= number
		self.major_lan.population -= number
		other.flow_in(language.get_lan(language.language_map[self.major_lan.name], number))



def show(country):
	print(country.major_lan.name, country.major_lan.population);

	for i in country.second_lan:
		print(i.name, i.population);



if __name__ == '__main__':
	n = language.English(10000000)
	m = language.Hindi(132)
	amer_sp = language.Spanish(12333)
	China_C = language.Chinese(12999993)
	China_e = language.English(1223244)
	China_M = language.Malay(12342)
	american = country("USA", 10000000, 0.5, position(5,23), n, m, amer_sp)
	China = country("China", 20000000, 0.2, position(-2,24), China_C, China_e, China_M)
	print("China:")
	show(China)
	print("american:")
	show(american)
	print(language.Chinese.get_pop(),language.English.get_pop())
	China.flow(american)
	print(language.Chinese.get_pop(),language.English.get_pop())
	american.flow(China)
	print("after:")
	print("China:")
	show(China)
	print("american:")
	show(american)
	print(language.Chinese.get_pop(),language.English.get_pop())

	
