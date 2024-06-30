#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Imports
import pygame as pg, random as rnd
import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Variablen
ANZ_Wände   = 5
ANZ_Rays    = 5
Do_Rays     = True
Do_Inf      = True
Do_Refl     = True
Dashed      = False
Do_Text     = True

text = """+ / - | Anzahl der Strahlen +-1
z / t | Anzahl der Strahlen +-10
e | Wand entfernen
w | Wand hinzufügen
r | Strahlen ein- / ausschalten
m | Refelktionen ein- / ausschalten
i | Offene Strahlen ein- / ausschalten
d | Wände als Elemente umschalten
h | WHilfetext ein- / ausschalten
Esc | Beenden"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Defs
def get_intersect(a, b, c, d):
    ab, cd, ac = a - b, c - d, a - c
    if not (nenner := ab.x * cd.y - ab.y * cd.x): return
    t = (ac.x * cd.y - ac.y * cd.x) / nenner
    u = -(ab.x * ac.y - ab.y * ac.x) / nenner
    if 0 <= t <= 1 and 0 <= u <= 1: return a.lerp(b, t)


def ray_casting(wände):
    global Do_Refl, Do_Rays, Do_Inf
    c = V2(pg.mouse.get_pos())
    for ray in rays:
        d = c + ray
        entfernungen = [(c.distance_to(k), k,a,b) for a, b in wände if (k := get_intersect(a, b, c, d))]
        if not entfernungen: 
            if Do_Inf:
                pg.draw.line(fenster, 'red', c, d)
        else:
            if Do_Rays:
                pg.draw.line(fenster, 'green', c, min(entfernungen)[1], 1)
            # Reflektion
            line1 = tuple([c,d])
            line2 = tuple([min(entfernungen)[2],min(entfernungen)[3]])
            reflected_line = reflect_line(line1, line2)
            if Do_Refl:
                draw_dashed_line(fenster, 'blue', reflected_line[0], reflected_line[1], 2)


def draw_dashed_line(screen, color, start_pos, end_pos, width=1, dash_length=10):
    # Berechne den Unterschied zwischen den Endpunkten
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = (dx**2 + dy**2) ** 0.5

    # Berechne die Anzahl der Striche
    num_dashes = int(distance // dash_length)

    for i in range(num_dashes):
        if i % 2 == 0:  # Zeichne nur jeden zweiten Strich
            start = (
                start_pos[0] + (dx * i / num_dashes),
                start_pos[1] + (dy * i / num_dashes)
            )
            end = (
                start_pos[0] + (dx * (i + 1) / num_dashes),
                start_pos[1] + (dy * (i + 1) / num_dashes)
            )
            pg.draw.line(screen, color, start, end, width)


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


def calculate_intersection(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None  # Linien sind parallel oder identisch

    intersect_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    intersect_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

    return (intersect_x, intersect_y)

def reflect_line(line1, line2):
    # Berechne den Schnittpunkt
    intersection = calculate_intersection(line1, line2)
    if intersection is None:
        return None  # Kein Schnittpunkt

    # Extrahiere die Punkte
    (x1, y1), _ = line1
    (x3, y3), (x4, y4) = line2
    intersect_x, intersect_y = intersection

    # Berechne den Richtungsvektor der Linie 1
    dx1 = intersect_x - x1
    dy1 = intersect_y - y1

    # Berechne den Normalvektor der Linie 2
    dx2 = x4 - x3
    dy2 = y4 - y3
    norm_x = -dy2
    norm_y = dx2

    # Normalisieren des Normalvektors
    norm_length = (norm_x**2 + norm_y**2) ** 0.5
    norm_x /= norm_length
    norm_y /= norm_length

    # Berechne das Skalarprodukt
    dot_product = dx1 * norm_x + dy1 * norm_y

    # Berechne den reflektierten Vektor
    rx = dx1 - 2 * dot_product * norm_x
    ry = dy1 - 2 * dot_product * norm_y

    # Die reflektierte Linie startet am Schnittpunkt
    reflected_line = ((intersect_x, intersect_y), (intersect_x + rx, intersect_y + ry))

    return reflected_line

def SwitchRay():
    global Do_Rays
    if Do_Rays:
        Do_Rays = False
    else:
       Do_Rays = True

def SwitchRefl():
    global Do_Refl
    if Do_Refl:
        Do_Refl = False
    else:
       Do_Refl = True
      
def SwitchInf():
    global Do_Inf
    if Do_Inf:
        Do_Inf = False
    else:
       Do_Inf = True

def SwitchDashed():
    global Dashed
    if Dashed:
        Dashed = False
    else:
       Dashed = True   

def SwitchText():
    global Do_Text
    if Do_Text:
        Do_Text = False
    else:
       Do_Text = True   


def blit_text(surface, text, pos, font, color=pg.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main
pg.init()
größe = breite, höhe = 1920, 1080
fenster = pg.display.set_mode(größe)
font = pg.font.SysFont('DejaVu Sans', 24)


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
                case pg.K_r: SwitchRay()
                case pg.K_m: SwitchRefl()
                case pg.K_i: SwitchInf()
                case pg.K_d: SwitchDashed()
                case pg.K_h: SwitchText()
        
    ANZ_Rays = Check_Anz_Rays(ANZ_Rays)
    # rays = [V2(3000, 0).rotate(w) for w in range(0, 360, 360 / ANZ_Rays)]
    angles = np.linspace(0, 360, ANZ_Rays, endpoint=False)
    rays = [V2(3000, 0).rotate(w) for w in angles]
  

    ray_casting(wände)

    for a, b in wände:
        if Dashed:
            draw_dashed_line(fenster, 'white', a, b, 3)
        else:
            pg.draw.line(fenster, 'white', a, b, 3)

    if Do_Text:
        blit_text(fenster, text, (50, 20), font)

    pg.display.flip()