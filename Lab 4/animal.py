import random
class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
	 	self.sound=sound
	 	self.name=name
	 	self.age=age
	 	self.favorite_color=favorite_color
	def eat(self,food):
		print("Yummy!! "+self.name+" is eating "+food)
	def description(self):
		print(self.name+" is "+self.age+" years old and loves the color "+self.favorite_color)
	def make_sound(self,times):
		print(self.sound+" ! ")*times
d= Animal("woof","Dog","5","red")
d.eat("Apple")
d.description()
d.make_sound(3)

class Person(object):
	def __init__ (self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eat_breakfast(self,favorite_breakfast):
		print(self.name+", let's have "+favorite_breakfast+ " for breakfast.")
	def city_living (self,years):
		print(self.name+" has lived in "+ self.city+ " for "+ years+ " years.")
		pass

h= Person("Harry", 16, "Jerusalem", "male")
h.eat_breakfast("waffles")
h.city_living("4")


class Song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
	def random_lyrics(self,lyrics):
		num=[]
		for i  in lyrics:
			n=random.randint(0,2)
			if n not in num:
				print(lyrics[n])
			num.append(n)



	def sing (self):
		print(self.lyrics)

flower_song = Song(["Roses are red,",
			"voilets are blue,",
			"I wrote a poem for you"])
flower_song.random_lyrics(["Roses are red,",
			"voilets are blue,",
			"I wrote a poem for you"])

