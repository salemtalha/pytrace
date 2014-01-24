#!/bin/python

from collections import namedtuple

Colour = namedtuple("Colour", "c")
Light = namedtuple("Light", "pos colour")
Material = namedtuple("Material", "diffuse specular shininess mirror")
Sphere = namedtuple("Sphere", "pos radius Material")
Scene = namedtuple("Scene", "Lights Spheres numlights numspheres numboxes nummeshes camera view up ambient fov width height")
Box = namedtuple("Box", "pos size Material")
Mesh = namedtuple("Mesh", "verts faces m Material")

Lights = [Light([-100, 150.0, 400.0], [0.7, 0.7, 0.7]), 
          Light([400.0, 100.0, 150.0], [0.7, 0.0, 0.7])]

MAT1 = [[0.7, 1.0, 0.7], [0.5, 0.7, 0.5], 25.0, 0.3]
MAT2 = [[0.5, 0.5, 0.5], [0.5, 0.7, 0.5], 25.0, 0.3]
MAT3 = [[1.0, 0.6, 0.1], [0.5, 0.7, 0.5], 25.0, 0.3]
MAT4 = [[0.7, 0.6, 1.0], [0.5, 0.4, 0.8], 25.0, 0.3]

Spheres = [ Sphere([0.0, 0.0, -400.0], 100.0, MAT1),
            Sphere([200.0, 50.0, -100.0], 150.0, MAT1),
            Sphere([0.0, -1200.0, -500.0], 1000.0, MAT2),
            Sphere([-100.0, 25.0, -300.0], 50.0, MAT3),
            Sphere([0.0, 100.0, -250.0], 25.0, MAT1) ]

Boxes = [Box([-200, -125.0, 0.0], 100.0, MAT4)]

camera  = [0.0, 0.0, 800.0]
view    = [0.0, 0.0, -1.0]
up      = [0.0, 1.0, 0.0]
ambient = [0.3, 0.3, 0.3]

fov    = 50.0
width  = 500
height = 500

refscene = Scene(Lights, Spheres, 
                 2, 5, 1, 1, 
                 [0.0, 0.0, 800.0], 
                 [0.0, 0.0, -1.0], 
                 [0.0, 1.0, 0.0], 
                 [0.3, 0.3, 0.3],
                 50.0, 512, 512)
