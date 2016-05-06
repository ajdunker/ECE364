#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-02-29 18:23:54 -0500 (Mon, 29 Feb 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab07/points.py $
# $Revision: 89049 $


import math


class PointND:

    def __init__(self, *args):
        self.t = tuple(args)
        self.n = len(args)
        for item in args:
            if type(item) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")

    def __str__(self):
        rstr = '({:.2f},'.format(self.t[0])
        for i in range(1, self.n - 1):
            rstr += ' {:.2f},'.format(self.t[i])
        rstr += ' {:.2f})'.format(self.t[self.n-1])
        return str(rstr)

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        dist = 0
        for i in range(self.n):
            dist += (self.t[i] - other.t[i]) ** 2
        return math.sqrt(dist)

    def nearestPoint(self, points):
        dist = None
        cPoint = None
        if not points:
            raise ValueError("Input cannot be empty.")
        for item in points:
            if cPoint is None:
                dist = self.distanceFrom(item)
                cPoint = item
            else:
                if self.distanceFrom(item) < dist:
                    dist = self.distanceFrom(item)
                    cPoint = item
        return cPoint

    def clone(self):
        new = PointND(*self.t)
        return new

    def __add__(self, x):
        if isinstance(x, self.__class__) or isinstance(x, PointND):
            if x.n != self.n:
                raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
            else:
                vals = list(self.t)
                for i in range(self.n):
                    vals[i] += x.t[i]
                return PointND(*vals)
        elif isinstance(x,  float):
            vals = list(self.t)
            for i in range(self.n):
                vals[i] += x
            return PointND(*vals)

    def __radd__(self, x):
        if isinstance(x, self.__class__) or isinstance(x, PointND):
            if x.n != self.n:
                raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
            else:
                vals = list(self.t)
                for i in range(self.n):
                    vals[i] += x.t[i]
                return PointND(*vals)
        elif isinstance(x,  float):
            vals = list(self.t)
            for i in range(self.n):
                vals[i] += x
            return PointND(*vals)

    def __sub__(self, x):
        if isinstance(x, self.__class__) or isinstance(x, PointND):
            if x.n != self.n:
                raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
            else:
                vals = list(self.t)
                for i in range(self.n):
                    vals[i] -= x.t[i]
                return PointND(*vals)
        elif isinstance(x,  float):
            vals = list(self.t)
            for i in range(self.n):
                vals[i] -= x
            return PointND(*vals)

    def __mul__(self, x):
        if isinstance(x,  float):
            vals = list(self.t)
            for i in range(self.n):
                vals[i] *= x
            return PointND(*vals)

    def __rmul__(self, x):
        if isinstance(x,  float):
            vals = list(self.t)
            for i in range(self.n):
                vals[i] *= x
            return PointND(*vals)

    def __truediv__(self, x):
        if isinstance(x,  float):
            vals = list(self.t)
            for i in range(self.n):
                vals[i] /= x
            return PointND(*vals)

    def __neg__(self):
        vals = list(self.t)
        for i in range(self.n):
            vals[i] = -vals[i]
        return PointND(*vals)

    def __getitem__(self, k):
        return self.t[k]

    def __eq__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        for i in range(self.n):
            if self.t[i] != other.t[i]:
                return False
        return True

    def __ne__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        return not self.__eq__(other)

    def __gt__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        zeroes = [0.0] * self.n
        origin = PointND(*zeroes)
        if self.distanceFrom(origin) > other.distanceFrom(origin):
            return True
        else:
            return False

    def __ge__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        zeroes = [0.0] * self.n
        origin = PointND(*zeroes)
        if self.distanceFrom(origin) >= other.distanceFrom(origin):
            return True
        else:
            return False

    def __lt__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        zeroes = [0.0] * self.n
        origin = PointND(*zeroes)
        if self.distanceFrom(origin) < other.distanceFrom(origin):
            return True
        else:
            return False

    def __le__(self, other):
        if other.n != self.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        zeroes = [0.0] * self.n
        origin = PointND(*zeroes)
        if self.distanceFrom(origin) <= other.distanceFrom(origin):
            return True
        else:
            return False


class Point3D(PointND):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        PointND.__init__(self, x, y, z)


class PointSet:

    def __init__(self, **kwargs):
        if len(kwargs) < 1:
            self.n = 0
            points = set()
        else:
            if 'pointList' in kwargs:
                if len(kwargs['pointList']) < 1:
                    raise ValueError("'pointList' input parameter cannot be empty.")
                else:
                    self.n = kwargs['pointList'][0].n
                    for point in kwargs['pointList']:
                        if point.n != self.n:
                            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
                    self.points = set(kwargs['pointList'])
            else:
                raise KeyError("'pointList' input parameter not found.")

    def addPoint(self, p):
        if p.n == self.n:
            self.points.add(p)
        else:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))

    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        maxes = []
        mins = []
        pList = [[] for _ in range(self.n)]
        for point in self.points:
            for i, dim in enumerate(point.t):
                pList[i].append(dim)
        for i, item in enumerate(pList):
            maxes.append(max(pList[i]))
            mins.append(min(pList[i]))
        rtup = PointND(*mins), PointND(*maxes)
        return rtup

    def computeNearestNeighbors(self, otherPointSet):
        closest = []
        for point in self.points:
            nearest = point.nearestPoint(otherPointSet.points)
            closest.append(tuple([point, nearest]))
        return closest

    def __add__(self, other):
        if other.n == self.n:
            self.addPoint(other)
            return self
        else:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))

    def __sub__(self, other):
        if self.__contains__(other):
            self.points.remove(other)
            return self
        else:
            return self

    def __contains__(self, item):
        for point in self.points:
            if point == item:
                return True
        return False

def main():
    pass

if __name__ == "__main__":
    main()
