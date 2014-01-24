#!/bin/python

import math, cProfile 
from scene import *

def render(scene):
  aspect_ratio = scene.width / scene.height
  view_len = scene.height / math.tan(math.radians(scene.fov) / 2.0) / 2.0 
  hor = [0, 0, 0]
  top_pixel = [0, 0, 0]
  tmp = [0, 0, 0]
  
  cross(hor, scene.view, scene.up)
  normalize(hor)
  normalize(scene.up)

  scale(tmp, scene.view, view_len)
  add(top_pixel, scene.camera, tmp)
  scale(tmp, hor, -(scene.width / 2.0))
  add(top_pixel, top_pixel, tmp)
  scale(tmp, scene.up, scene.height / 2.0)
  add(top_pixel, top_pixel, tmp)

  pixel = [0, 0, 0]
  ray = [0, 0, 0]
  col = Colour([])

  print "P3\n", scene.width, scene.height, "\n255"

  for i in xrange(0, scene.height):
    print("\n")
    for j in xrange(0, scene.width):
      scale(tmp, hor, aspect_ratio * j);
      add(pixel, top_pixel, tmp)
      scale(tmp, up, -i)
      add(pixel, pixel, tmp)
      sub(ray, pixel, scene.camera)
      col = trace(ray, scene.camera, scene)
      print col.c[0], col.c[1], col.c[2]


#Vector Operations
def add(v, u, w):
  for i in xrange(0, 3):
    v[i] = u[i] + w[i]
    
def sub(v, u, w):
  for i in xrange(0, 3):
    v[i] = u[i] - w[i]

def scale(v, u, scalar):
  for i in xrange(0, 3):
    v[i] = u[i] * scalar 

def normalize(u):
  det = math.sqrt(u[0]*u[0] + u[1]*u[1] + u[2]*u[2])
  for i in xrange(0, 3):
    u[i] = u[i] / det


def dot(a, u, v):
  for i in xrange(0,3):
    a += (u[i] * v[i])
  return a

def cross(v, u, w):
  v[0] = (u[1] * w[2]) - (u[2] * w[1])
  v[1] = (u[2] * w[0]) - (u[0] * w[2])
  v[2] = (u[0] * w[1]) - (u[1] * w[0])
  return v

def quad(a, b, c, roots):
  if(a == 0):
    roots[0] = (-c / b)
    return 1
  else:
    d = (b * b) - (4 * a * c)
    if(d > 0):
      dd = math.sqrt(d)
      roots[0] = (-b + dd) / (2 * a)
      roots[1] = (-b - dd) / (2 * a)
      return 2
  return 0
#------------------------------#

def ray_epsilon_check(r, ray, line, raylen, normal):
  if(r > 0.00001):
    raylen = r
    tmp = [0, 0, 0]
    scale(tmp, ray, r)
    sub(normal, tmp, line)
    return 1
  return 0

def intersect_sphere(ray, origin, node, raylen, normal):
  line = [0, 0, 0]
  sub(line, node.pos, origin)
  roots = [0, 0, 0]
  a, b, c = 0, 0, 0
  a = dot(a, ray, ray)
  b = dot(b, ray, line)
  c = dot(c, line, line)
  numroots = quad(a, -2*b, c - node.radius * node.radius, roots) 
  if (numroots == 0):
    pass
  elif(numroots == 1):
    return ray_epsilon_check(roots[0], ray, line, raylen, normal)
  elif(numroots == 2):
    if(roots[0] < roots[1]):
      return ray_epsilon_check(roots[0], ray, line, raylen, normal)
    else:
      return ray_epsilon_check(roots[1], ray, line, raylen, normal)
  return 0

def trace(ray, origin, scene):
  raylen = 0
  normal = [0, 0, 0]
  draw = False
  for i in xrange(0, 5):
    if intersect_sphere(ray, origin, Spheres[i], raylen, normal):
      draw = True
      break
  if(draw):
    return Colour([255, 255, 255])
  else:
    return Colour([0, 0, 0])

def main():
  render(refscene) 

