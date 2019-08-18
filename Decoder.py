class Decoder:
	def __init__(self, a, b, c, steps = 5):
		self.a = a[0]
		self.b = b[0]
		self.c = c[0]
		self.add = [a[1], b[1], c[1]]
		self.steps = steps
	
	def dec(self):
		import math as m
		import time as t
		
		a = int(self.a)
		b = int(self.b)
		c = int(self.c)
		
		numbers = input("What is the set you wish to decode my lord?: ")
		
		to_be_decoded = list(numbers.split(" "))
		
		def do_over(steps, x, do_a, do_b, do_c):
			memory = x
			step = 1
			while step <= steps:
				memory = int((-do_b + m.sqrt((do_b ** 2) - (4 * do_a * (do_c - memory)))) / (2 * do_a))
				step += 1
			
			return memory
		
		export_list = []
		start = t.time()
		for num in to_be_decoded:
			out = do_over(self.steps, int(num), a, b, c)
			
			a += self.add[0]
			b += self.add[1]
			c += self.add[2]
			
			export_list.append(chr(out))
		for letter in export_list:
			print(letter, end = "")
		end = t.time()
		print("Total time:", end - start, "seconds")
