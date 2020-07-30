# 3D-Polygon-area
## Used to calculate the area of any polygon in 3D space

Calculating the area of an arbitrary polygon is very simple in the case of 2D. It can be solved by dividing the triangle and the Helen formula, but in the case of 3D, this problem becomes tricky.

The method here is to solve the polygon area by using the Stokes formula. The specific mathematical derivation process is in the pdf file of the project.

This script realizes that by inputting the vertices of any polygon in 3D space, you can get its area. Compared with the previous 2D situation, the 3D model realized by this script is more universal, and the 2D situation is a special one. Happening.

You can directly open the 3D polygon area.py file for use, just modify the polygon variable to the vertex set of your polygon.

### But it should be noted that when inputting the vertices of the polygon, you must follow the flow input order of the ring, starting at any point clockwise or counterclockwise, but you cannot input the vertices out of order, otherwise the final result will be 0.
