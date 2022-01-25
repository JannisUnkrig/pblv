import random
import math


if __name__ == '__main__':

    sensors = [
        [0, 0, 0],
        [0, random.random(), random.random()],
        [0, random.random(), random.random()],
        [0, random.random(), random.random()],
        [random.random(), 0, random.random()],
        [random.random(), 0, random.random()],
        [random.random(), 0, random.random()],
        [random.random(), random.random(), 0],
        [random.random(), random.random(), 0],
        [random.random(), random.random(), 0]
        ]

    print("Sensor Positionen:\n", sensors)

    noOfExamples = int(input("Größe der Traingsmenge eingeben: "))
    objects = []
    distances = []

    for i in range(noOfExamples):

        obj = [random.random(), random.random(), random.random()]
        objects.append(obj)

        dist = [math.sqrt((obj[0] - s[0]) ** 2 + (obj[1] - s[1]) ** 2 + (obj[2] - s[2]) ** 2) for s in sensors]
        distances.append(dist)

        print("Objekt:", obj, " |  Distanzen:", dist)
