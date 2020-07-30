import math

def compute_3D_polygon_area(points):
    '''
    points为任意多边形的点集合
    注意输入时要按环的流动输入，不能乱序输入
    此方法是3D空间的，相较于2D更具有普适性
    '''
    if (len(points) < 3): return 0.0
    P1X,P1Y,P1Z = points[0][0],points[0][1],points[0][2]
    P2X,P2Y,P2Z = points[1][0],points[1][1],points[1][2]
    P3X,P3Y,P3Z = points[2][0],points[2][1],points[2][2]
    a = pow(((P2Y-P1Y)*(P3Z-P1Z)-(P3Y-P1Y)*(P2Z-P1Z)),2) + pow(((P3X-P1X)*(P2Z-P1Z)-(P2X-P1X)*(P3Z-P1Z)),2) + pow(((P2X-P1X)*(P3Y-P1Y)-(P3X-P1X)*(P2Y-P1Y)),2)
    cosnx = ((P2Y-P1Y)*(P3Z-P1Z)-(P3Y-P1Y)*(P2Z-P1Z))/(pow(a,1/2))
    cosny = ((P3X-P1X)*(P2Z-P1Z)-(P2X-P1X)*(P3Z-P1Z))/(pow(a,1/2))
    cosnz = ((P2X-P1X)*(P3Y-P1Y)-(P3X-P1X)*(P2Y-P1Y))/(pow(a,1/2))
    s = cosnz*((points[-1][0])*(P1Y)-(P1X)*(points[-1][1])) + cosnx*((points[-1][1])*(P1Z)-(P1Y)*(points[-1][2])) + cosny*((points[-1][2])*(P1X)-(P1Z)*(points[-1][0]))
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        ss = cosnz*((p1[0])*(p2[1])-(p2[0])*(p1[1])) + cosnx*((p1[1])*(p2[2])-(p2[1])*(p1[2])) + cosny*((p1[2])*(p2[0])-(p2[2])*(p1[0]))
        s += ss 

    s = abs(s/2.0)

    return s

#polygon输入多边形的顶点集合
polygon = [[0,0,0],[0,1,0],[1,1,1],[1,0,1]]

result = compute_3D_polygon_area(polygon)


