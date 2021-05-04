from math import radians, cos, sin, asin, sqrt, pi

EARTH_RADIUS = 6371
ROOM_OFFSET_KM = 0.01 # Room witdh/2 converted to km

def example1():
    engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude':34.069140, 'longitude': -118.442689 }
    geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude':-118.441878 }
    psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude':-118.441312 }
    music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
    humanities_classroom = { 'name': 'Art Hitory', 'latitude': 34.071528, 'longitude': -118.441211 }
    john_student = { 'name': 'John Wilson', 'latitude': 34.069149, 'longitude': -118.442639 } #engineering
    jane_student = { 'name': 'Jane Graham', 'latitude': 34.069601, 'longitude': -118.441862 } #geology
    pam_student = { 'name': 'Pam Bam', 'latitude': 34.071513, 'longitude': -118.441181 } #humanities
    student_list = [john_student,jane_student,pam_student]
    classroom_list =[geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]  
    return (student_list, classroom_list)


def example2():
    engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude':34.069140, 'longitude': -118.442689 }
    geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude':-118.441878 }
    psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude':-118.441312 }
    music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
    humanities_classroom = { 'name': 'Art Hitory', 'latitude': 34.071528, 'longitude': -118.441211 }
    john_student = { 'name': 'John Wilson', 'latitude': 34.069849, 'longitude': -118.443539 } #engineering
    jane_student = { 'name': 'Jane Graham', 'latitude': 34.069901, 'longitude': -118.441562 } #geology
    pam_student = { 'name': 'Pam Bam', 'latitude': 34.071523, 'longitude': -118.441171 } #humanities
    classroom_list =[geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]
    student_list = [john_student,jane_student,pam_student]
    return (student_list, classroom_list)

def example3():
    engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude':34.069140, 'longitude': -118.442689 }
    geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude':-118.441878 }
    psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude':-118.441312 }
    music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
    humanities_classroom = { 'name': 'Art Hitory', 'latitude': 34.071528, 'longitude': -118.441211 }
    john_student = { 'name': 'John Wilson', 'latitude': 35.071523, 'longitude': -118.441171 } #humanities
    jane_student = { 'name': 'Jane Graham', 'latitude': 36.071523, 'longitude': -118.441171 } #humanities
    pam_student = { 'name': 'Pam Bam', 'latitude': 34.071523, 'longitude': -118.441171 } #humanities
    classroom_list =[geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]
    student_list = [john_student,jane_student,pam_student]
    return (student_list, classroom_list)

def example4():
    engineering_classroom = { 'name': 'Principles of computational geo-location analysis', 'latitude':34.069140, 'longitude': -118.442689 }
    geology_classroom = { 'name': 'Sedimentary Petrology', 'latitude': 34.069585, 'longitude':-118.441878 }
    psychology_classroom = { 'name': 'Introductory Psychobiology', 'latitude': 34.069742, 'longitude':-118.441312 }
    music_classroom = { 'name': 'Art of Listening', 'latitude': 34.070223, 'longitude': -118.440193 }
    humanities_classroom = { 'name': 'Art Hitory', 'latitude': 34.071528, 'longitude': -118.441211 }
    john_student = { 'name': 'John Wilson', 'latitude': 34.071523, 'longitude': -118.441171 } #humanities
    jane_student = { 'name': 'Jane Graham', 'latitude': 36.071523, 'longitude': -118.441171 } #humanities
    pam_student = { 'name': 'Pam Bam', 'latitude': 34.071523, 'longitude': -118.441171 } #humanities
    classroom_list =[geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]
    student_list = [john_student,jane_student,pam_student]
    return (student_list, classroom_list)    

# Using haversine formula to calculate the distance between two points
# source: https://stackoverflow.com/a/4913653/3670530
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = EARTH_RADIUS 
    return c * r

# Move the latitude to a new point using the distance
# Source: https://stackoverflow.com/a/7478827/3670530
def move_latitude(latitude, distance):
    return latitude  + (distance / EARTH_RADIUS) * (180 / pi);

# Move the longitude to a new point using the distance
# Source: https://stackoverflow.com/a/7478827/3670530
def move_longitude(latitude, longitude, distance):
    return longitude + (distance / EARTH_RADIUS) * (180 / pi) / cos(latitude * pi/180);

def calculate_rectangle(center_point, distance):
    latitude = center_point['latitude']
    longitude = center_point['longitude']
    top_left_corner = {'latitude':move_latitude(latitude, distance), 'longitude':move_longitude(latitude, longitude, distance*-1) }
    # Don't needed the other two corners of the rectangle
    #top_rigth_corner = {'latitude':move_latitude(latitude, distance), 'longitude':move_longitude(latitude, longitude, distance) }
    #left_botton_corner = {'latitude':move_latitude(latitude, distance*-1), 'longitude':move_longitude(latitude, longitude, distance*-1) }
    right_botton_corner = {'latitude':move_latitude(latitude,  distance*-1), 'longitude':move_longitude(latitude, longitude, distance)}
    return (top_left_corner, right_botton_corner)

def is_point_within_rectangle(point, rectangle):
    top_left_corner, right_botton_corner = rectangle
    is_y = top_left_corner['latitude'] >= point['latitude'] and point['latitude'] >= right_botton_corner['latitude']
    is_x = top_left_corner['longitude'] <= point['longitude'] and point['longitude'] <= right_botton_corner['longitude']
    return is_x and is_y

# It will fail if the student is located in the area near the corners because using the distance as a criterion, at the end 
# means check if the student is between a circle
def students_in_classes_haversine_distance(students, classrooms):
    result = []
    for room in classrooms:
        for student in students:
            distance = haversine(room['longitude'], room['latitude'], student['longitude'], student['latitude'])
            if distance < ROOM_OFFSET_KM:
                result.append(student)
                students.remove(student)
                break
    return result

# It should work accurately because in this case, the classroom area is small, it might fail if the area is quite bigger and 
# the student is at the edge of the rectangle
def students_in_classes_within_rectangle(students, classrooms):
    result = []
    for room in classrooms:
        room_rectangle = calculate_rectangle(room, ROOM_OFFSET_KM)
        for student in students:
            if is_point_within_rectangle(student, room_rectangle):
                result.append(student)
                students.remove(student)
                break
    return result    

def students_cluster_in_classes(students, classrooms):
    students_in_room = {}
    for room in classrooms:
        students_in_room[room['name']] = []
        room_rectangle = calculate_rectangle(room, ROOM_OFFSET_KM)
        for student in students:
            if is_point_within_rectangle(student, room_rectangle):
                students_in_room[room['name']].append(student)
                #students.remove(student)
    newDict = dict(filter(lambda elem: len(elem[1]) > 1, students_in_room.items()))
    students_cluser = list(newDict.values())
    return [item for sublist in students_cluser for item in sublist]

print("Example 1 - Distance")
print(students_in_classes_haversine_distance(*example1()))
print("Example 1 - Rectangle")
print(students_in_classes_haversine_distance(*example1()))
print("Example 2 - Distance")
print(students_in_classes_within_rectangle(*example2()))
print("Example 2 - Rectangle")
print(students_in_classes_within_rectangle(*example2()))
print("Students in clustur 1")
print(students_cluster_in_classes(*example3()))
print("Students in clustur 2")
print(students_cluster_in_classes(*example4()))