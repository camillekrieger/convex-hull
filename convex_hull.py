def determine_point_location(left, right, new):
    return (right[0] - left[0]) * (new[1] - left[1]) - (right[1] - left[1]) * (new[0] - left[0])

def FindUpperTangent(L, R):
    #find rightmost point in L and leftmost point in R
    n = len(L)
    m = len(R)
    p_index = 0
    for i in range(len(L)):
        if L[i][0] > L[p_index][0]:
            p_index = i
    q_index = 0
    for j in range(len(R)):
        if R[j][0] < R[q_index][0]:
            q_index = j
    # temp = draw_line(L[p_index], R[q_index])
    done = False
    while not done:
        done = True
        while determine_point_location(L[p_index], R[q_index], L[(p_index - 1) % n]) > 0:
            # r = L[(p_index - 1) % n] #counterclockwise neighbor
            # temp = draw_line(r, R[q_index])
            p_index = (p_index - 1) % n
            done = False
        while determine_point_location(L[p_index], R[q_index], R[(q_index + 1) % m]) > 0:
            # r = R[(q_index + 1) % m] #clockwise neighbor
            # temp = draw_line(L[p_index], r)
            q_index = (q_index + 1) % m
            done = False
    return L[p_index], R[q_index]

def FindLowerTangent(L, R):
    #find rightmost point in L and leftmost point in R
    n = len(L)
    m = len(R)
    p_index = 0
    for i in range(len(L)):
        if L[i][0] > L[p_index][0]:
            p_index = i
    q_index = 0
    for j in range(len(R)):
        if R[j][0] < R[q_index][0]:
            q_index = j
    # temp = draw_line(L[p_index], R[q_index])
    done = False
    while not done:
        done = True
        while determine_point_location(L[p_index], R[q_index], L[(p_index + 1) % n]) < 0:
            # r = L[(p_index + 1) % n] #clockwise neighbor
            # temp = draw_line(r, R[q_index])
            p_index = (p_index + 1) % n
            done = False
        while determine_point_location(L[p_index], R[q_index], R[(q_index - 1) % m]) < 0:
            # r = R[(q_index - 1) % m] #counterclockwise neighbor
            # temp = draw_line(L[p_index], r)
            q_index = (q_index - 1) % m
            done = False
    return L[p_index], R[q_index]

def connect_hulls(left, right):
    merged_points = left + right
    merged_points = list(set(merged_points))
    merged_points.sort()

    def build_half(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and determine_point_location(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull

    lower_hull = build_half(merged_points)
    upper_hull = build_half(reversed(merged_points))
    return lower_hull[:-1] + upper_hull[:-1]


def compute_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Return the subset of provided points that define the convex hull"""
    if len(points) <= 1:
        return points
    points.sort()
    L = points[:len(points)//2]
    R = points[len(points)//2:]
    left_hull = compute_hull(L)
    right_hull = compute_hull(R)
    FindUpperTangent(left_hull, right_hull)
    FindLowerTangent(left_hull, right_hull)
    points = connect_hulls(left_hull, right_hull)
    return points