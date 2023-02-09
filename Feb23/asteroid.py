# Task: Determine if cylinder intersects with line segment
# Strategy: Check if distance between line segment and axis of cylinder is less than the cylinder radius.
# Compare at endpoint of line segment, cylinder, and shortest line (if extending the ray and line segment)
from collections import deque

# Defining functions for vector arithmetic
# cross product
def cross(a, b):
    (ax, ay, az) = a
    (bx, by, bz) = b
    x = (ay * bz) - (az * by)
    y = (az * bx) - (ax * bz)
    z = (ax * by) - (ay * bx)
    return (x, y, z)

# dot product
def dot(a, b):
    (ax, ay, az) = a
    (bx, by, bz) = b
    return ((ax*bx) + (ay*by) + (az*bz))

# distance between points
def distance(a, b):
    (ax, ay, az) = a
    (bx, by, bz) = b
    return ((ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2) ** 0.5

# find point on vector from parametric equations
# a is origin, b is direction, t is parameter
def param(a, b, t):
    (ax, ay, az) = a
    (bx, by, bz) = b
    return ((ax + bx * t), (ay + by * t), (az + bz * t))

# Compute direction vector from a to b
def between(a, b):
    (ax, ay, az) = a
    (bx, by, bz) = b
    return ((bx - ax), (by - ay), (bz - az))

# Compute projection of b onto vector a
def project(a, a_dir, b):
    b_t = dot(between(a, b), a_dir) / dot(a_dir, a_dir)
    b_proj = param(a, a_dir, b_t)
    return(b_t, b_proj)

sx, sy, sz, bx, by, bz, a = [float(x) for x in input().split()]
a = int(a)
dbx = bx - sx
dby = by - sy
dbz = bz - sz

s_point = (sx, sy, sz)
s_dir = (dbx, dby, dbz)

b_point = (bx, by, bz)

asteroids = deque([])

# Calculate center, direction, and radius for each asteroid
for _ in range(a):
    px, py, pz, dx, dy, dz, m = [float(x) for x in input().split()]
    m = int(m)
    v = deque([float(x) for x in input().split()])
    r = 0
    for _ in range(m):
        tx = v.popleft()
        ty = v.popleft()
        tz = v.popleft()
        
        tr = distance((px, py, pz), (tx, ty, tz))
        r = max(r, tr)
    asteroids.append(((px, py, pz), (dx, dy, dz), r))

for (a_point, a_dir, r) in asteroids:
    n = cross(s_dir, a_dir)

    (px, py, pz) = a_point
    t = ((px - sx), (py - sy), (pz - sz))

    d_short = float("inf")
    
    # if not parallel, check the closest point between lines defined by vector
    if n != (0,0,0):
        s_par = dot(cross(a_dir, n), t) / dot(n, n)
        a_par = dot(cross(s_dir, n), t) / dot(n, n)

        # Ensure that all points are on line segment or cylinder axis
        s_par = max(min(s_par, 1), 0)
        a_par = max(a_par, 0)

        a_short = param(a_point, a_dir, a_par)
        s_short = param(s_point, s_dir, s_par)

        d_short = distance(a_short, s_short)

    d_ship = float("inf")
    d_ast = float("inf")

    d_start = distance(a_point, s_point)

    # Calculate distance between ship and projection of ship onto asteroid vector
    # and vice versa
    (ship_t, proj_ship_ast) = project(a_point, a_dir, s_point)
    (ast_t, proj_ast_ship) = project(s_point, s_dir, a_point)

    # Ignore projection points behind starting point
    if ship_t >= 0:
        d_ship = distance(proj_ship_ast, s_point)

    if ast_t >= 0 and ast_t <= 1:
        d_ast = distance(proj_ast_ship, a_point)

    if min(d_short, d_ship, d_ast, d_start) > r:
        continue

    print("Surrender")
    break
else:
    print("Go")
    
