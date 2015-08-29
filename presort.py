class service():
def __init__(self,name,wt,d1,d2,d3):
	self.cartonid =  name,
	self.weight = wt,
	self.measure1 = d1,
	self.measure2 = d2,
	self.measure3 = d3

length = max (d1,d2,d3)
height = min (d1,d2,d3)
width = sum(d1,d2,d3)-(length+height)
