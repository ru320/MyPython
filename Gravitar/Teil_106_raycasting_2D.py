#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Imports
import pygame as pg, random as rnd
import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Variablen
ANZ_Wände = 5
ANZ_Rays = 5



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Defs
def get_intersect(a, b, c, d):
  ab, cd, ac = a - b, c - d, a - c
  if not (nenner := ab.x * cd.y - ab.y * cd.x): return
  t = (ac.x * cd.y - ac.y * cd.x) / nenner
  u = -(ab.x * ac.y - ab.y * ac.x) / nenner
  if 0 <= t <= 1 and 0 <= u <= 1: return a.lerp(b, t)


def ray_casting(wände):
  c = V2(pg.mouse.get_pos())
  for ray in rays:
    d = c + ray
    entfernungen = [(c.distance_to(k), k) for a, b in wände if (k := get_intersect(a, b, c, d))]
    if not entfernungen: 
        pg.draw.line(fenster, 'red', c, d)
    else:
        pg.draw.line(fenster, 'green', c, min(entfernungen)[1], 1)

def Check_Anz_Rays(ANZ_Rays):
  if ANZ_Rays > 360:
    ANZ_Rays = 360
  if ANZ_Rays < 0:
    ANZ_Rays = 0
  return ANZ_Rays

def Wandentfernen():
  wände.pop()

def Wandhinzufuegen():
  neue_wand = (V2(rnd.randrange(breite), rnd.randrange(höhe)), V2(rnd.randrange(breite), rnd.randrange(höhe)))
  wände.append(neue_wand) 
  
  


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main
pg.init()
größe = breite, höhe = 1920, 1080
fenster = pg.display.set_mode(größe)

clock = pg.time.Clock()
FPS = 40

ANZ_Rays = Check_Anz_Rays(ANZ_Rays)

V2 = pg.Vector2
wände = [tuple(V2(rnd.randrange(breite), rnd.randrange(höhe)) for _ in range(2)) for _ in range(ANZ_Wände)]
# rays = [V2(3000, 0).rotate(w) for w in range(0, 360, 360 // ANZ_Rays)]

while True:
  clock.tick(FPS)
  fenster.fill('black')

  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT: quit()
    if ereignis.type == pg.KEYDOWN:
       match ereignis.key:
        case pg.K_ESCAPE: quit()
        case pg.K_KP_PLUS: ANZ_Rays += 1
        case pg.K_KP_MINUS: ANZ_Rays -= 1
        case pg.K_z: ANZ_Rays += 10
        case pg.K_t: ANZ_Rays -= 10
        case pg.K_e: Wandentfernen()
        case pg.K_w: Wandhinzufuegen()
        
  ANZ_Rays = Check_Anz_Rays(ANZ_Rays)
  # rays = [V2(3000, 0).rotate(w) for w in range(0, 360, 360 / ANZ_Rays)]
  angles = np.linspace(0, 360, ANZ_Rays, endpoint=False)
  rays = [V2(3000, 0).rotate(w) for w in angles]
  

  ray_casting(wände)

  for a, b in wände:
    pg.draw.line(fenster, 'white', a, b, 3)

  pg.display.flip()