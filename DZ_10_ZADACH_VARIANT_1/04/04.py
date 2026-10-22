from math import sqrt
def closest_point(points,x0,y0):
    if len(points)==0:
        return None,None
    best_point=points[0]
    min_distance=(best_point[0]-x0)**2+(best_point[1]-y0)**2
    for point in points:
        distance=(point[0]-x0)**2+(point[1]-y0)**2
        if distance<min_distance:
            min_distance=distance
            best_point=point
    return best_point,sqrt(min_distance)
points=[(1,2),(4,5),(2,3),(7,1)]
point,distance=closest_point(points,3,3)
print("Ближайшая точка:",point)
print("Расстояние:",distance)
