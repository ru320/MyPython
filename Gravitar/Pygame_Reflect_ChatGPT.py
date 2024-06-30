import pygame

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
            pygame.draw.line(screen, color, start, end, width)

# Beispielverwendung
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Beispiel-Linien
line1 = ((100, 100), (300, 200))  # Strahl
line2 = ((200, 150), (400, 150))  # Spiegel

# Berechne die reflektierte Linie
reflected_line = reflect_line(line1, line2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Zeichne die ursprünglichen Linien
    pygame.draw.line(screen, (0, 0, 0), line1[0], line1[1], 2)
    pygame.draw.line(screen, (0, 0, 255), line2[0], line2[1], 2)

    if reflected_line:
        # Zeichne den ursprünglichen Strahl bis zum Schnittpunkt
        pygame.draw.line(screen, (0, 0, 0), line1[0], calculate_intersection(line1, line2), 2)
        # Zeichne die reflektierte Linie gestrichelt
        draw_dashed_line(screen, (255, 0, 0), reflected_line[0], reflected_line[1], 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
