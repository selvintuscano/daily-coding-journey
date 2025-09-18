# You are given the speed of a vehicle and the time it has traveled. Your task is to compute and return the distance traveled by the vehicle.
# Two floating-point numbers:

#speed: The speed of the vehicle.
#time: The time it has been traveling.

def calculate_distance(speed, time):
    return speed * time


result = calculate_distance(20, 4)
print(result)