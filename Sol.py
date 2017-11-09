import itertools

#Point class 
class Point:
	#Function intializes point class
	def  __init__(self, idVal, edgePoint,  color = None):
		#points can only be 4 variants red, blue yellow and uncolored (None)
		self.colors =  ['r', 'b', 'y', None]
		self.id = idVal
		self.edgePoint = edgePoint

		#trying to detect if a color is valid or invalid
		if color in self.colors:
			self.color =  color
		else:
			print "invalid color set to None"
			self.color = None
	
	#Function takes in a color and if valid changes it to the user entered color
	def changeColor(self, color):
		#checking if a colour is valid or invalid switches color if valid
		if self.edgePoint != True and color in self.colors:
			self.color = color  

		else:
			print "invalid color not changed"
	#Function returns whether the point is part of the outside edge of the polygon or not
	def isEdgePoint(self):
		return self.edgePoint

	#Function returns the curent set color of the polygon
	def showColor(self):
		return self.color

#Triangle class
class Triangle:
	#Intializing teh triangle class
	def __init__(self, point1, point2, point3):

		self.complete = False
		self.point1 = point1 
		self.point2 = point2
		self.point3 = point3
		self.colors =  set([self.point1.showColor(), self.point2.showColor(), self.point3.showColor()])

		#Determining whether the Triangle is complete or not
		if len(self.colors) == 3 and None not in self.colors:
			self.complete =  True

	#Function returns whether a triangle is determined to be complete (r,b,y)
	def getStatus(self):
		self.colors =  set([self.point1.showColor(), self.point2.showColor(), self.point3.showColor()])
		if len(self.colors) == 3 and None not in self.colors:
			self.complete =  True
		else:
			self.complete = False

		return self.complete

	#Function returns the colour and Id of the points that comprise the triangle
	def showPoints(self):
		return {self.point1.id : self.point1.color, self.point2.id : self.point2.color, self.point3.id : self.point3.color}

#Polygon class comprised of points and triangles
class Polygon:
	#Constructor that intializes the Polygon
	def __init__(self, triangles):
		self.triangles  = triangles
		self.variantPoints = []
		self.variantDict = {}

	#Function sets the list of points within the polygon that are mutable 
	def setVariants(self, newPoints):
		self.variantPoints =  newPoints
	#Function returns a list of the points that a mutable within the polygon
	def showVariants(self):
		return self.variantPoints
	#Function determines whether there is 2 complete traingles within the polygon
	def hasTwo(self):
		index = 0
		completeCount = 0
		for triangle in self.triangles:
			if triangle.getStatus() == True:
				completeCount += 1 
			if completeCount > 2:
				return False
			index += 1
		
		if completeCount != 2:
			return False
		else:
			return True 
	#Function add the dictionary containing each triangle that has that variant point
	#when you change the color of one point it affects several triangles
	def addVariantDict(self, newDict):
		self.variantDict = newDict

	# Function checks if any of the triangles that a specific point are 
	# a part of are complete if more than 2 return
	def checkVariantTriangles(self, pointID):
		count =  0
		for angleRef in self.variantDict[pointID]:

			if self.triangles[angleRef].getStatus() == True:
				count += 1
			if count > 2:
				break
		return count

#Recursive back tracking solver for the problem returns true if there is a solution false otherwise
def solve(poly, polyVariants, completeTriangles = 0): 
	#if more than 2 triangles return false
	if completeTriangles > 2:
		return False
	colors  =  ['r', 'b', 'y']
	#Whenenever the list is empty and at its final point and all triangles are
	#set then check if there is two complete triangles
	if len(polyVariants) == 0:
		if poly.hasTwo():
			return True
	else:
		#Iterate over colors to see if it is part of the solution
		for color in colors:
			polyVariants[0].changeColor(color)
			compTriCount = completeTriangles +  poly.checkVariantTriangles(poly.variantPoints[0].id)
			if compTriCount > 2:
				# if this partial solution has more than 2 complete triangles skip over
				# and move on to the next color
				continue
			#reursive call
			if solve(poly, polyVariants[1:], compTriCount):
				return True
	return False








def main():
	print "Is there a solution to the polygon?"

	#Intializing the individual points that the polygone and points
	#is composed of
	p1 = Point(1,True,'r')
	p2 = Point(2,True,'r')
	p3 = Point(3,True,'y')
	p4 = Point(4,True,'b')
	p5 = Point(5,True,'b')
	p6 = Point(6,False)
	p7 = Point(7,False)
	p8 = Point(8,False)
	p9 = Point(9,False)
	p10 = Point(10,True, 'y')
	p11 = Point(11,False)
	p12 = Point(12,False)
	p13 = Point(13,False)
	p14 = Point(14,True, 'r')
	p15 = Point(15,False)
	p16 = Point(16,False)
	p17 = Point(17,False)
	p18 = Point(18,False)
	p19 = Point(19,True, 'y')
	p20 = Point(20,True, 'r')
	p21 = Point(10,True, 'r')
	p22 = Point(22,True, 'b')

	#Intializing the triangles that the shape is composed of
	t0 = Triangle(p1,p5,p6)
	t1 = Triangle(p1,p2,p6)
	t2 = Triangle(p2,p6,p7)
	t3 = Triangle(p2,p3,p7)
	t4 = Triangle(p3,p7,p8)
	t5 = Triangle(p3,p4,p8)
	t6 = Triangle(p4,p8,p14)
	t7 = Triangle(p5,p6,p9)
	t8 = Triangle(p6,p7,p9)
	t9 = Triangle(p7,p8,p13)
	t10 = Triangle(p8,p13,p14)
	t11 = Triangle(p5,p9,p10)
	t12 = Triangle(p7,p9,p12)
	t13 = Triangle(p7,p12,p13)
	t14 = Triangle(p9,p10,p11)
	t15 = Triangle(p9,p11,p12)
	t16 = Triangle(p10,p11,p15)
	t17 = Triangle(p11,p12,p15)
	t18 = Triangle(p12,p15,p16)
	t19 = Triangle(p12,p13,p16)
	t20 = Triangle(p13,p16,p17)
	t21 = Triangle(p13,p17,p18)
	t22 = Triangle(p17,p18,p19)
	t23 = Triangle(p14,p18,p19)
	t24 = Triangle(p10,p15,p20)
	t25 = Triangle(p15,p16,p20)
	t26 = Triangle(p16,p20,p21)
	t27 = Triangle(p16,p17,p21)
	t28 = Triangle(p17,p21,p22)
	t29 = Triangle(p17,p19,p22)
	t30 = Triangle(p13,p14,p18)

	#Intializing the polygon
	shape = Polygon([t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, 
		t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, 
		t24, t25, t26, t27, t28, t29,t30])
	#Adding a list of variant adjustable points
	shape.setVariants([p6,p7,p8,p9,p11,p12,p13,p15,p16,p17,p18])
	#adding a dictionary of vaiant points and the different triangles that they are a part of
	shape.addVariantDict({ 6 : [0,1,7,8], 7:[2,8,9,12,13], 8: [4,5,6,9], 9: [7,8,11,12,14,15], 
	11: [14,15,16,17], 12: [12,13,14,15,17,18,19], 13: [9,10,13,19,20,21,30], 15:[16,17,18,24,25],
	16: [18,19,20,25,26,27], 17: [20,21,22,27,28,29], 18: [21,22,23,30]})

	
	#print solve(shape, shape.variantPoints)
	if solve(shape, shape.variantPoints):
		print "YES"
	else:
		print "NO"


if __name__ == "__main__":
    main()