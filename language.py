
# -*- coding: UTF-8 -*-


language_map = {"Chinese" : 0, "English" : 1, "Hindi" : 2, "Spanish" : 3, "Arabic" : 4, "Malay" : 5, "Russian" : 6, "Bengali" : 7, "Portuguese" : 8, "French" : 9, "Hausa" : 10, "Punjabi" : 11, "Japanese" : 12, "German" : 13, "Persian" : 14 }

num2lan = {0: 'Chinese', 1: 'English', 2: 'Hindi', 3: 'Spanish', 4: 'Arabic', 5: 'Malay', 6: 'Russian', 7: 'Bengali', 8: 'Portuguese', 9: 'French', 10: 'Hausa', 11: 'Punjabi', 12: 'Japanese', 13: 'German', 14: 'Persian'}

class language(object):

	language_pop = [0 for x in range(15)] #人口总数


	def mix(self, lan):
		self._population += lan._population
	def __init__(self, name, population):
		self.name = name
		self._population = population #地区人口数
		language.language_pop[language_map[self.name]] = language.language_pop[language_map[self.name]] + population
	@property
	def population(self):
		return self._population

	@population.setter
	def population(self, population):
		language.language_pop[language_map[self.name]] = language.language_pop[language_map[self.name]] + population - self._population
		self._population = population


class English(language):
	def __init__(self, population):
		super(English, self).__init__("English", population)
	def get_pop():
		return language.language_pop[language_map["English"]]

class Chinese(language):
	def __init__(self, population):
		super(Chinese, self).__init__("Chinese", population)
	def get_pop():
		return language.language_pop[language_map["Chinese"]]


class Hindi(language):
	def __init__(self, population):
		super(Hindi, self).__init__("Hindi", population)
	def get_pop():
		return language.language_pop[language_map["Hindi"]]

class Spanish(language):
	def __init__(self, population):
		super(Spanish, self).__init__("Spanish", population)
	def get_pop():
		return language.language_pop[language_map["Spanish"]]

class Arabic(language):
	def __init__(self, population):
		super(Arabic, self).__init__("Arabic", population)
	def get_pop():
		return language.language_pop[language_map["Arabic"]]



class Malay(language):
	def __init__(self, population):
		super(Malay, self).__init__("Malay", population)
	def get_pop():
		return language.language_pop[language_map["Malay"]]



class Russian(language):
	def __init__(self, population):
		super(Russian, self).__init__("Russian", population)
	def get_pop():
		return language.language_pop[language_map["Russian"]]



class Bengali(language):
	def __init__(self, population):
		super(Bengali, self).__init__("Bengali", population)
	def get_pop():
		return language.language_pop[language_map["Bengali"]]



class Portuguese(language):
	def __init__(self, population):
		super(Portuguese, self).__init__("Portuguese", population)
	def get_pop():
		return language.language_pop[language_map["Portuguese"]]



class French(language):
	def __init__(self, population):
		super(French, self).__init__("French", population)
	def get_pop():
		return language.language_pop[language_map["French"]]



class Hausa(language):
	def __init__(self, population):
		super(Hausa, self).__init__("Hausa", population)
	def get_pop():
		return language.language_pop[language_map["Hausa"]]



class Punjabi(language):
	def __init__(self, population):
		super(Punjabi, self).__init__("Punjabi", population)
	def get_pop():
		return language.language_pop[language_map["Punjabi"]]



class Japanese(language):
	def __init__(self, population):
		super(Japanese, self).__init__("Japanese", population)
	def get_pop():
		return language.language_pop[language_map["Japanese"]]



class German(language):
	def __init__(self, population):
		super(German, self).__init__("German", population)
	def get_pop():
		return language.language_pop[language_map["German"]]



class Persian(language):
	def __init__(self, population):
		super(Persian, self).__init__("Persian", population)
	def get_pop():
		return language.language_pop[language_map["Persian"]]

def get_lan(language, num):
	if language == 0 : return Chinese(num)
	elif language == 1 : return English(num)
	elif language == 2 : return Hindi(num)
	elif language == 3 : return Spanish(num)
	elif language == 4 : return Arabic(num)
	elif language == 5 : return Malay(num)
	elif language == 6 : return Russian(num)
	elif language == 7 : return Bengali(num)
	elif language == 8 : return Portuguese(num)
	elif language == 9 : return French(num)
	elif language == 10 : return Hausa(num)
	elif language == 11 : return Punjabi(num)
	elif language == 12 : return Japanese(num)
	elif language == 13 : return German(num)
	else : return Persian(num)

