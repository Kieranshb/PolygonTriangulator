# PolygonTriangulator
This repo contains the code to solve the "Triangulating Polygons" challenge  

### My Solution:  
When constructing my solution, I first tried to approach the problem from the theoretical angle about triangulation. Theory’s such as Fisk’s Theorem proved positive in helping me gain some insight into Triangulation problems and their rules.

Unable to find a pattern or a “hard” math solution I decide to test the multiple permutations and combinations that would exist for this problem. First, I created 3 classes to build the polygon I the challenge:

**Point:**  
* Has variable color  
* 3 colors red (r), yellow (y), blue (b)  

**Triangle:**  
* Composed of 3 points of varying colors
* Triangles have a status of complete (a combination of r,b,y)
* A dictionary of points and their colors can be returned as well. 

**Polygon:**    
Constructed of a list of Triangles, a list of points that have mutable colours, and a dictionary containing the mutable points and triangles in which they are a part of
The polygon is capable of checking if exactly 2 triangles exist within the solution
Whenever a point is changed you can check the triangles in which that point is a part of

Finally, I have a function that I use as a “solver” for the problem. It starts by recursively iterating through the list of existing mutable points and then cycling through their colors. To reduce runtime, I check to see if a point puts the current solution over the threshold of two Complete Triangles. If this is the case my program iterates over tot the next color instead of further exploring an incorrect solution.
My solution tries this until there are no more colors in which to set the points and there is no solution and returns false. My program as it runs right now currently determines that there is no solution to the polygon as described in the challenge. 


### Resources:  
http://mathworld.wolfram.com/MinimumVertexColoring.html  
https://en.wikipedia.org/wiki/Graph_coloring  
https://people.csail.mit.edu/indyk/6.838-old/handouts/lec4.pdf  
https://www.cs.ucsb.edu/~suri/cs235/Triangulation.pdf  
http://www.cs.uu.nl/docs/vakken/ga/slides3.pdf  

### Time Breakdown:  
Research: 1-2 hrs  
Design & Implementation: ~ 3 - 4 hrs  
Testing & Refactoring: 2 hrs  
Documentation: 1 hr  
Total: ~ 9 hrs    
### Improvements:  
* Increase the constraints to further crop recursion
* Runtime on some Windows machines takes a lot longer compared to when I test it on other machines (Mac OSX)
* I would pursue a mathematical angle instead of searching of the semi-brute force method that I used
* I would maybe consider using a language other than python for performance reasons  
#### Installation:  
git clone https://github.com/Kieran92/PolygonTriangulator.git  
#### To Run:  
 python Sol.py  
#### To Run Tests:  
python solTests.py  
