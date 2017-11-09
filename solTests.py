import unittest
from Sol import Point, Triangle, Polygon, solve

class PointTests(unittest.TestCase):

	def setUp(self):
		pass
	def test_color1(self):
		p  = Point(1,True, 'b')
		self.assertEqual(p.showColor(),'b')

	def test_color2(self):
		p  = Point(1,True, 'r')
		self.assertEqual(p.showColor(),'r')

	def test_color3(self):
		p  = Point(1,True, 'y')
		self.assertEqual(p.showColor(),'y')

	def test_color4(self):
		p  = Point(1,False)
		self.assertEqual(p.showColor(),None)

	def test_color_chang1(self):
		p = Point(1,False)
		p.changeColor('r')
		self.assertEqual(p.showColor(),'r')

	def test_color_change2(self):
		p = Point(1,False)
		p.changeColor('y')
		self.assertEqual(p.showColor(),'y')

	def test_color_change3(self):
		p = Point(1,False)
		p.changeColor('b')
		self.assertEqual(p.showColor(),'b')

	def test_color_change4(self):
		p = Point(1,True, 'b')
		p.changeColor('r')
		self.assertEqual(p.showColor(),'b')

	def test_edgePoint1(self):
		p = Point(1,True, 'b')
		self.assertTrue(p.isEdgePoint())

	def test_edgePoint2(self):
		p = Point(1,False)
		self.assertFalse(p.isEdgePoint())

class TriangleTests(unittest.TestCase):

	def setUp(self):
		pass

	def test_showPoints(self):
		p1 = Point(1,True, 'b')
		p2 = Point(2,True, 'b')
		p3 = Point(3,True, 'b')
		t = Triangle(p1,p2,p3)
		self.assertEqual(t.showPoints(), {1:'b',2:'b',3:'b'})

	def test_showPoints1(self):
		p1 = Point(1,False)
		p2 = Point(2,True, 'b')
		p3 = Point(3,True, 'b')
		t = Triangle(p1,p2,p3)
		self.assertEqual(t.showPoints(), {1:None,2:'b',3:'b'})

	def test_showPoints2(self):
		p1 = Point(1,False)
		p2 = Point(2,False)
		p3 = Point(3,False)
		t = Triangle(p1,p2,p3)
		p1.changeColor('r')
		p2.changeColor('y')
		p3.changeColor('b')
		self.assertEqual(t.showPoints(), {1:'r',2:'y',3:'b'})

	def test_getStatus1(self):
		p1 = Point(1,False)
		p2 = Point(2,False)
		p3 = Point(3,False)
		t = Triangle(p1,p2,p3)
		p1.changeColor('r')
		p2.changeColor('y')
		p3.changeColor('b')
		self.assertTrue(t.getStatus())
	
	def test_getStatus2(self):
		p1 = Point(1,False)
		p2 = Point(2,False)
		p3 = Point(3,False)
		t = Triangle(p1,p2,p3)
		p1.changeColor('r')
		p2.changeColor('y')
		p3.changeColor('r')
		self.assertFalse(t.getStatus())
	
	def test_getStatus3(self):
		p1 = Point(1,False)
		p2 = Point(2,False)
		p3 = Point(3,False)
		t = Triangle(p1,p2,p3)
		p2.changeColor('y')
		p3.changeColor('r')
		self.assertFalse(t.getStatus())

	def test_getStatus4(self):
		p1 = Point(1,True, 'r')
		p2 = Point(2,True, 'b')
		p3 = Point(3,True, 'y')
		t = Triangle(p1,p2,p3)
		self.assertTrue(t.getStatus())

	def test_getStatus5(self):
		p1 = Point(1,True, 'r')
		p2 = Point(2,True, 'b')
		p3 = Point(3,True, 'r')
		t = Triangle(p1,p2,p3)
		self.assertFalse(t.getStatus())

class PolygonTests(unittest.TestCase):
	def setUp(self):
		pass
	def test_VariantPoints(self):
		p1  =  Point(1, True, 'y')
		p2  =  Point(2, True, 'y')
		p3  =  Point(3, True, 'y')
		p4  =  Point(4, True, 'r')
		p5  =  Point(5, False)
		t0  =  Triangle(p1,p2, p5) 
		t1  =  Triangle(p2,p3, p5) 
		t2  =  Triangle(p1,p4, p5) 
		t3  =  Triangle(p3,p4, p5) 
		shape = Polygon([t0,t1,t2,t3])
		shape.setVariants([p5])
		shape.addVariantDict({5:[0,1,2,3]})
		self.assertEqual(shape.showVariants(),[p5])

	def test_VariantPoints1(self):
		p1  =  Point(1, True, 'r')
		p2  =  Point(2, True, 'b')
		p3  =  Point(3, True, 'y')
		p4  =  Point(4, True, 'r')
		p5  =  Point(5, False)
		p6  =  Point(6, False)
		t0  =  Triangle(p1,p2,p5) 
		t1  =  Triangle(p1,p3,p5) 
		t2  =  Triangle(p2,p5,p6) 
		t3  =  Triangle(p2,p4,p6) 
		t4  =  Triangle(p3,p5,p6) 
		t5  =  Triangle(p3,p4,p6) 
		shape = Polygon([t0,t1,t2,t3,t4,t5])
		shape.setVariants([p5,p6])
		shape.addVariantDict({5:[0,1,2,4], 6:[2,4,3,5]})
		self.assertEqual(shape.showVariants(),[p5,p6])
	
	def test_hasTwo1(self):
		p1  =  Point(1, True, 'r')
		p2  =  Point(2, True, 'b')
		p3  =  Point(3, True, 'y')
		p4  =  Point(4, True, 'r')
		p5  =  Point(5, False)
		p6  =  Point(6, False)
		t0  =  Triangle(p1,p2,p5) 
		t1  =  Triangle(p1,p3,p5) 
		t2  =  Triangle(p2,p5,p6) 
		t3  =  Triangle(p2,p4,p6) 
		t4  =  Triangle(p3,p5,p6) 
		t5  =  Triangle(p3,p4,p6) 
		shape = Polygon([t0,t1,t2,t3,t4,t5])
		shape.setVariants([p5,p6])
		shape.addVariantDict({5:[0,1,2,4], 6:[2,4,3,5]})
		self.assertFalse(shape.hasTwo())

	def test_hasTwo2(self):
		p1  =  Point(1, True, 'y')
		p2  =  Point(2, True, 'y')
		p3  =  Point(3, True, 'y')
		p4  =  Point(4, True, 'r')
		p5  =  Point(5, False)
		t0  =  Triangle(p1,p2, p5) 
		t1  =  Triangle(p2,p3, p5) 
		t2  =  Triangle(p1,p4, p5) 
		t3  =  Triangle(p3,p4, p5) 
		shape = Polygon([t0,t1,t2,t3])
		shape.setVariants([p5])
		shape.addVariantDict({5:[0,1,2,3]})
		self.assertFalse(shape.hasTwo())

	def test_hasTwo3(self):
		p1  =  Point(1, True, 'r')
		p2  =  Point(2, True, 'b')
		p3  =  Point(3, True, 'y')
		p4  =  Point(4, True, 'r')
		p5  =  Point(5, False)
		p6  =  Point(6, False)
		t0  =  Triangle(p1,p2,p5) 
		t1  =  Triangle(p1,p3,p5) 
		t2  =  Triangle(p2,p5,p6) 
		t3  =  Triangle(p2,p4,p6) 
		t4  =  Triangle(p3,p5,p6) 
		t5  =  Triangle(p3,p4,p6) 
		shape = Polygon([t0,t1,t2,t3,t4,t5])
		shape.setVariants([p5,p6])
		shape.showVariants()[0].changeColor('r')
		shape.showVariants()[1].changeColor('b')
		shape.addVariantDict({5:[0,1,2,4], 6:[2,4,3,5]})
		self.assertTrue(shape.hasTwo())

	def test_hasTwo4(self):
		p1  =  Point(1, True, 'b')
		p2  =  Point(2, True, 'y')
		p3  =  Point(3, True, 'b')
		p4  =  Point(4, True, 'b')
		p5  =  Point(5, False)
		t0  =  Triangle(p1,p2, p5) 
		t1  =  Triangle(p2,p3, p5) 
		t2  =  Triangle(p1,p4, p5) 
		t3  =  Triangle(p3,p4, p5) 
		shape = Polygon([t0,t1,t2,t3])
		shape.setVariants([p5])
		shape.showVariants()[0].changeColor('r')
		shape.addVariantDict({5:[0,1,2,3]})
		self.assertTrue(shape.hasTwo())

	#need to test the checkVariant triangles portion of my program
	def test_checkVariantTriangles(self):
		p1  =  Point(1, True, 'b')
		p2  =  Point(2, True, 'y')
		p3  =  Point(3, True, 'b')
		p4  =  Point(4, True, 'b')
		p5  =  Point(5, False)
		t0  =  Triangle(p1,p2, p5) 
		t1  =  Triangle(p2,p3, p5) 
		t2  =  Triangle(p1,p4, p5) 
		t3  =  Triangle(p3,p4, p5) 
		shape = Polygon([t0,t1,t2,t3])
		shape.setVariants([p5])
		shape.showVariants()[0].changeColor('r')
		shape.addVariantDict({5:[0,1,2,3]})
		self.assertEqual(shape.checkVariantTriangles(5), 2)

	def test_checkVariantTriangles2(self):
		p1  =  Point(1, True, 'b')
		p2  =  Point(2, True, 'y')
		p3  =  Point(3, True, 'b')
		p4  =  Point(4, True, 'b')
		p5  =  Point(5, False)
		t0  =  Triangle(p1,p2, p5) 
		t1  =  Triangle(p2,p3, p5) 
		t2  =  Triangle(p1,p4, p5) 
		t3  =  Triangle(p3,p4, p5) 
		shape = Polygon([t0,t1,t2,t3])
		shape.setVariants([p5])
		shape.addVariantDict({5:[0,1,2,3]})
		self.assertEqual(shape.checkVariantTriangles(5), 0)


class testSolve(unittest.TestCase):
	def setUp(self):
		pass
	def testSolve1(self):
		p1  =  Point(1, True, 'b')
		p2  =  Point(2, True, 'y')
		p3  =  Point(3, True, 'b')
		p4  =  Point(4, True, 'b')
		p5  =  Point(5, False)
		t0  =  Triangle(p1,p2, p5) 
		t1  =  Triangle(p2,p3, p5) 
		t2  =  Triangle(p1,p4, p5) 
		t3  =  Triangle(p3,p4, p5) 
		shape = Polygon([t0,t1,t2,t3])
		shape.setVariants([p5])
		shape.addVariantDict({5:[0,1,2,3]})
		self.assertTrue(solve(shape, shape.variantPoints))

	def testSolve2(self):
		p1  =  Point(1, True, 'b')
		p2  =  Point(2, True, 'b')
		p3  =  Point(3, True, 'b')
		p4  =  Point(4, True, 'b')
		p5  =  Point(5, False)
		t0  =  Triangle(p1,p2, p5) 
		t1  =  Triangle(p2,p3, p5) 
		t2  =  Triangle(p1,p4, p5) 
		t3  =  Triangle(p3,p4, p5) 
		shape = Polygon([t0,t1,t2,t3])
		shape.setVariants([p5])
		shape.addVariantDict({5:[0,1,2,3]})
		self.assertFalse(solve(shape, shape.variantPoints))	

	def testSolve3(self):
		p1  =  Point(1, True, 'r')
		p2  =  Point(2, True, 'b')
		p3  =  Point(3, True, 'y')
		p4  =  Point(4, True, 'r')
		p5  =  Point(5, False)
		p6  =  Point(6, False)
		t0  =  Triangle(p1,p2,p5) 
		t1  =  Triangle(p1,p3,p5) 
		t2  =  Triangle(p2,p5,p6) 
		t3  =  Triangle(p2,p4,p6) 
		t4  =  Triangle(p3,p5,p6) 
		t5  =  Triangle(p3,p4,p6) 
		shape = Polygon([t0,t1,t2,t3,t4,t5])
		shape.setVariants([p5,p6])
		shape.addVariantDict({5:[0,1,2,4], 6:[2,4,3,5]})
		self.assertTrue(solve(shape, shape.variantPoints))	
	
	def testSolve4(self):
		p1  =  Point(1, True, 'r')
		p2  =  Point(2, True, 'r')
		p3  =  Point(3, True, 'r')
		p4  =  Point(4, True, 'r')
		p5  =  Point(5, False)
		p6  =  Point(6, False)
		t0  =  Triangle(p1,p2,p5) 
		t1  =  Triangle(p1,p3,p5) 
		t2  =  Triangle(p2,p5,p6) 
		t3  =  Triangle(p2,p4,p6) 
		t4  =  Triangle(p3,p5,p6) 
		t5  =  Triangle(p3,p4,p6) 
		shape = Polygon([t0,t1,t2,t3,t4,t5])
		shape.setVariants([p5,p6])
		shape.addVariantDict({5:[0,1,2,4], 6:[2,4,3,5]})
		self.assertTrue(solve(shape, shape.variantPoints))	

if __name__ == '__main__':
	unittest.main()


