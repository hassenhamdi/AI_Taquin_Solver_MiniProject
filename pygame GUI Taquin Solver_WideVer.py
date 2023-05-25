"""
NOTE : CHATGPT WAS NOT USED IN THE PROCESS OF CREATION OF THESE FILE AND THE ASSOCIATED FILES ,
                 IN THE CONTAINING PACKAGE NOR ANY OTHER REFERENCES FROM INTERNET NOR BEEN TAKEN FROM ANY OTHER PERSON
                 WORK , ONLY THE OFFICIAL PYTHON DOCUMENTATION BEEN USED AS A REFERENCE .
                 PLEASE DON'T DISTRIBUTE THE CODE FOR THIS TERMINAL MINI-SOFTWARE ON THE INTERNET NOR TO ANYONE
                 WITHOUT PERMISSION .
                 MY REGARDS .
                 AUTHOR : "HASSEN HAMDI" .
"""

from pathlib import Path
import pygame
import SolveTaquin_cp as Tsolver
from BoardTaquinV3 import Taquin

tiles_position = [(12, 12), (140, 12), (268, 12), (12, 140), (140, 140), (268, 140), (12, 268), (140, 268), (268, 268)]
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Taquin GUI Solver")
image_path = Path("assets\\Tiles\\icon.png")
icon = pygame.image.load(image_path)
pygame.display.set_icon(icon)
fpsClock = pygame.time.Clock()

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_1 = (245, 245, 245)
WHITE_2 = (200, 200, 200)
WHITE_3 = (155, 155, 155)
RED = (200, 0, 0)
C2 = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (0, 255, 255)
CC2 = (255, 0, 255)
YELLOW = (255, 255, 0)
GREY = (133, 133, 133)

window.fill(GREY)
taquin_bg = pygame.draw.rect(window, WHITE_1, (10, 10, 386, 386), border_radius=10)

pygame.display.update()
font = pygame.font.SysFont(None, 48)
init = font.render("Initialize", True, BLACK)
init_r = init.get_rect()

start = font.render("Start Solving", True, BLACK)
start_r = start.get_rect()

dfs_rect = pygame.draw.rect(window, WHITE_2, (500, 340, 80, 40), border_radius=3)
dfsfont = font.render("DFS", True, BLACK)
window.blit(dfsfont, (505, 345, 80, 40))

bfs_rect = pygame.draw.rect(window, WHITE_2, (590, 340, 80, 40), border_radius=3)
bfsfont = font.render("BFS", True, BLACK)
window.blit(bfsfont, (595, 345, 40, 40))

A_rect = pygame.draw.rect(window, WHITE_2, (680, 340, 70, 40), border_radius=3)
Afont = font.render("A*", True, BLACK)
window.blit(Afont, (700, 345, 40, 40))

bg = pygame.image.load('assets/img30.jpg')
pygame.transform.scale(bg, (800, 600))
window.blit(bg, (0, 0), window.get_rect())

#  load image assets
t1 = pygame.image.load('assets/Tiles/1.png')
t2 = pygame.image.load('assets/Tiles/2.png')
t3 = pygame.image.load('assets/Tiles/3.png')
t4 = pygame.image.load('assets/Tiles/4.png')
t5 = pygame.image.load('assets/Tiles/5.png')
t6 = pygame.image.load('assets/Tiles/6.png')
t7 = pygame.image.load('assets/Tiles/7.png')
t8 = pygame.image.load('assets/Tiles/8.png')

tile1 = pygame.transform.scale(t1, (126, 126))
tile2 = pygame.transform.scale(t2, (126, 126))
tile3 = pygame.transform.scale(t3, (126, 126))
tile4 = pygame.transform.scale(t4, (126, 126))
tile5 = pygame.transform.scale(t5, (126, 126))
tile6 = pygame.transform.scale(t6, (126, 126))
tile7 = pygame.transform.scale(t7, (126, 126))
tile8 = pygame.transform.scale(t8, (126, 126))

t1r = tile1.get_rect()
t2r = tile2.get_rect()
t3r = tile3.get_rect()
t4r = tile4.get_rect()
t5r = tile5.get_rect()
t6r = tile6.get_rect()
t7r = tile7.get_rect()
t8r = tile8.get_rect()

tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8]
tileRects = [t1r, t2r, t3r, t4r, t5r, t6r, t7r, t8r]

root = Taquin(board=[1, 2, 3, 8, 6, 0, 7, 5, 4])
solver = Tsolver.SolveTaquin(root)
GenerateNode = root.generated_nodes_number
solver.recursive_dfs(root)
solver.solution_path_saver()
depth = solver.searchTreeDepth
solver.heuristic_search(root)
solver.step_to_solution_counter = 0
solver.bfs()
bfsExploredNodeNumber = solver.step_to_solution_counter
nodes = solver.explored_nodes_list

rect_b = pygame.draw.rect(window, BLACK, taquin_bg, 3, 10)

initial = pygame.draw.rect(window, WHITE_3, (540, 50, 220, 75), border_radius=3)
startBgRect = pygame.draw.rect(window, WHITE_3, (540, 150, 220, 75), border_radius=3)

window.blit(init, (579, 73, 220, 105))
window.blit(start, (545, 173, 220, 105))

running = True
count = None
loop = True
pause = False
speed = [1, 2, 4, 8, 16]
speedindex = 1
speedlistlen = len(speed)
stats = None
initializeClicked = False
plus_rect = None
minus_rect = None
bfs_selected = False
dfs_selected = False
A_selected = False
dfs_set : set = set()


def initialize():
    global startBgRect, initial, plus_rect, minus_rect, dfs_rect
    pygame.image.load('assets/img30.jpg')
    pygame.transform.scale(bg, (800, 600))
    window.blit(bg, (0, 0), window.get_rect())

    initial = pygame.draw.rect(window, WHITE_3, (540, 50, 220, 75), border_radius=3)
    startBgRect = pygame.draw.rect(window, WHITE_3, (540, 150, 220, 75), border_radius=3)

    plus_rect = pygame.draw.rect(window, WHITE_3, (540, 260, 40, 55), border_radius=7)
    plus = font.render("+", True, BLACK)
    window.blit(plus, (550, 270, 40, 75))

    pygame.draw.rect(window, WHITE_2, (587, 259, 125, 55), border_radius=7)
    pygame.draw.rect(window, BLACK, (587, 259, 125, 55), width=2, border_radius=7)
    spindex = font.render(f"{speedindex}", True, BLACK)
    window.blit(spindex, (641, 270, 100, 55))

    minus_rect = pygame.draw.rect(window, WHITE_3, (720, 260, 40, 55), border_radius=7)
    minus = font.render("-", True, BLACK)
    window.blit(minus, (735, 270, 40, 75))

    window.blit(init, (579, 73, 220, 105))
    window.blit(start, (545, 173, 220, 105))

    pygame.draw.rect(window, WHITE_1, (10, 10, 386, 386), border_radius=10)

    dfs_rect = pygame.draw.rect(window, WHITE_2, (500, 340, 80, 40), border_radius=3)
    dfsfont = font.render("DFS", True, BLACK)
    window.blit(dfsfont, (505, 345, 80, 40))

    bfs_rect = pygame.draw.rect(window, WHITE_2, (590, 340, 80, 40), border_radius=3)
    bfsfont = font.render("BFS", True, BLACK)
    window.blit(bfsfont, (595, 345, 40, 40))

    A_rect = pygame.draw.rect(window, WHITE_2, (680, 340, 70, 40), border_radius=3)
    Afont = font.render("A*", True, BLACK)
    window.blit(Afont, (700, 345, 40, 40))

    window.blit(tiles[0], tiles_position[0])
    window.blit(tiles[1], tiles_position[1])
    window.blit(tiles[2], tiles_position[2])
    window.blit(tiles[3], tiles_position[8])
    window.blit(tiles[4], tiles_position[7])
    window.blit(tiles[5], tiles_position[4])
    window.blit(tiles[6], tiles_position[6])
    window.blit(tiles[7], tiles_position[3])

    pygame.display.update()


initialize()
pygame.display.update()

def posindex():
    global p1, p2, p3, p4, p5, p6, p7, p8, leng, count
    if count == leng:
        return
    if bfs_selected:
        p1 = nodes[count].index(1)
        p2 = nodes[count].index(2)
        p3 = nodes[count].index(3)
        p4 = nodes[count].index(4)
        p5 = nodes[count].index(5)
        p6 = nodes[count].index(6)
        p7 = nodes[count].index(7)
        p8 = nodes[count].index(8)
    else:
        p1 = nodes[count].current.index(1)
        p2 = nodes[count].current.index(2)
        p3 = nodes[count].current.index(3)
        p4 = nodes[count].current.index(4)
        p5 = nodes[count].current.index(5)
        p6 = nodes[count].current.index(6)
        p7 = nodes[count].current.index(7)
        p8 = nodes[count].current.index(8)

def update_tile_position():
    global count, tiles_position, nodes, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, t1r, t2r, t3r, t4r, \
        t5r, t6r, t7r, t8r, loop, initial, initializeClicked, bfs_selected, dfs_selected, A_selected, dfs_set

    posindex()

    oldp1 = tiles_position[p1]
    oldp2 = tiles_position[p2]
    oldp3 = tiles_position[p3]
    oldp4 = tiles_position[p4]
    oldp5 = tiles_position[p5]
    oldp6 = tiles_position[p6]
    oldp7 = tiles_position[p7]
    oldp8 = tiles_position[p8]

    oldp = [oldp1, oldp2, oldp3, oldp4, oldp5, oldp6, oldp7, oldp8]

    count += 1

    posindex()

    newp1 = tiles_position[p1]
    newp2 = tiles_position[p2]
    newp3 = tiles_position[p3]
    newp4 = tiles_position[p4]
    newp5 = tiles_position[p5]
    newp6 = tiles_position[p6]
    newp7 = tiles_position[p7]
    newp8 = tiles_position[p8]

    newp = [newp1, newp2, newp3, newp4, newp5, newp6, newp7, newp8]

    tr1 = [newp1[0] - oldp1[0], newp1[1] - oldp1[1]]
    tr2 = [newp2[0] - oldp2[0], newp2[1] - oldp2[1]]
    tr3 = [newp3[0] - oldp3[0], newp3[1] - oldp3[1]]
    tr4 = [newp4[0] - oldp4[0], newp4[1] - oldp4[1]]
    tr5 = [newp5[0] - oldp5[0], newp5[1] - oldp5[1]]
    tr6 = [newp6[0] - oldp6[0], newp6[1] - oldp6[1]]
    tr7 = [newp7[0] - oldp7[0], newp7[1] - oldp7[1]]
    tr8 = [newp8[0] - oldp8[0], newp8[1] - oldp8[1]]

    transitions = [tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8]

    x = None
    y = None
    tdistance = None
    pos = 0
    for t in transitions:
        if t[0] or t[1]:
            tdistance = t
            break
        pos += 1

    x = tdistance[0]
    y = tdistance[1]
    imagex = oldp[pos][0]
    imagey = oldp[pos][1]

    if not dfs_selected and not bfs_selected and not A_selected:
        counterfont = font.render(" Counter ", True, WHITE, BLACK)
        window.blit(counterfont, (500, 405, 70, 40))
        pygame.draw.rect(window, WHITE_1, (670, 400, 80, 40), border_radius=3)
        pygame.draw.rect(window, BLACK, (670, 400, 80, 40), 1, border_radius=3)
        countfont = font.render(" 1 ", True, BLACK)
        window.blit(countfont, (690, 405, 80, 40))
        dfs_set.clear()
        dfs_selected = True

    while (dfs_selected or A_selected) and (oldp[pos][0]-128 < imagex < oldp[pos][0]+128 or oldp[pos][1]-128 < imagey < oldp[pos][1]+128):
        fpsClock.tick(60)
        event_listener()

        if not loop or imagex > oldp[pos][0]+128 or imagex < oldp[pos][0]-128 or imagey > oldp[pos][1]+128 or imagey < oldp[pos][1]-128:
            break

        pygame.draw.rect(window, WHITE_3, (10, 10, 386, 386), border_radius=10)
        for t in range(len(tiles)):
            if t != pos:
                window.blit(tiles[t], oldp[t])
        window.blit(tiles[pos], (imagex, imagey))
        pygame.display.update()
        if x:
            if x > 0:
                imagex += speed[speedindex]
            else:
                imagex -= speed[speedindex]
        if y:
            if y > 0:
                imagey += speed[speedindex]
            else:
                imagey -= speed[speedindex]

    pygame.draw.rect(window, WHITE_3, (10, 10, 386, 386), border_radius=10)

    if not initializeClicked:
        for i in range(len(newp)):
            pygame.draw.rect(window, WHITE_1, (670, 400, 80, 40), border_radius=3)
            pygame.draw.rect(window, BLACK, (670, 400, 80, 40), 1, border_radius=3)
            if dfs_selected:
                dfs_set.add(nodes[count])
                countfont = font.render(f" {len(dfs_set)+1}", True, BLACK, WHITE)
            else:
                countfont = font.render(f" {count + 1}", True, BLACK, WHITE)

            window.blit(tiles[i], newp[i])
            window.blit(countfont, (690, 405, 80, 40))
        pygame.display.update()
        if bfs_selected:
            pygame.time.wait(1500//speedindex)
        pygame.time.wait(250)
    else:
        initialize()


def event_listener():
    global running, count, loop, startBgRect, initial, start, init, stats, initializeClicked, speedindex, plus_rect, \
        minus_rect, dfs_rect, bfs_rect, A_rect, nodes, leng, dfs_selected, bfs_selected, A_selected, dfs_set
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if startBgRect.collidepoint(event.pos):
                pygame.draw.rect(window, WHITE_3, (540, 150, 220, 75), border_radius=3)
                window.blit(start, (545, 173, 220, 105))
                count = 0
                loop = True
                initializeClicked = False
                dfs_selected = False

            if initial.collidepoint(event.pos):
                initial = pygame.draw.rect(window, WHITE_3, (540, 50, 220, 75), border_radius=3)
                window.blit(init, (579, 73, 220, 105))
                loop = False
                stats = None
                count = None
                initializeClicked = True
                pygame.display.update()
                initialize()

                dfs_selected = True
                bfs_selected = False
                A_selected = False
                nodes = solver.explored_nodes_list
                leng = len(nodes)



            elif dfs_rect.collidepoint(event.pos):
                dfs_rect = pygame.draw.rect(window, WHITE_1, (500, 340, 80, 40), border_radius=3)
                dfsfont = font.render("DFS", True, BLACK)
                window.blit(dfsfont, (505, 345, 80, 40))


                counterfont = font.render(" Counter ", True, WHITE, BLACK)
                window.blit(counterfont, (500, 405, 70, 40))
                pygame.draw.rect(window, WHITE_1, (670, 400, 80, 40), border_radius=3)
                pygame.draw.rect(window, BLACK, (670, 400, 80, 40), 1, border_radius=3)
                countfont = font.render(" 1", True, BLACK)
                window.blit(countfont, (690, 405, 80, 40))

                bfs_rect = pygame.draw.rect(window, WHITE_2, (590, 340, 80, 40), border_radius=3)
                bfsfont = font.render("BFS", True, BLACK)
                window.blit(bfsfont, (595, 345, 40, 40))
                A_rect = pygame.draw.rect(window, WHITE_2, (680, 340, 70, 40), border_radius=3)
                Afont = font.render("A*", True, BLACK)
                window.blit(Afont, (700, 345, 40, 40))
                dfs_set = set()
                nodes = solver.explored_nodes_list
                leng = len(nodes)
                dfs_selected = True
                bfs_selected = False
                A_selected = False
                initializeClicked = True
                count = None

            elif bfs_rect.collidepoint(event.pos):
                dfs_rect = pygame.draw.rect(window, WHITE_2, (500, 340, 80, 40), border_radius=3)
                dfsfont = font.render("DFS", True, BLACK)
                window.blit(dfsfont, (505, 345, 80, 40))
                bfs_rect = pygame.draw.rect(window, WHITE_1, (590, 340, 80, 40), border_radius=3)
                bfsfont = font.render("BFS", True, BLACK)
                window.blit(bfsfont, (595, 345, 40, 40))
                A_rect = pygame.draw.rect(window, WHITE_2, (680, 340, 70, 40), border_radius=3)
                Afont = font.render("A*", True, BLACK)
                window.blit(Afont, (700, 345, 40, 40))

                counterfont = font.render(" Counter ", True, WHITE, BLACK)
                window.blit(counterfont, (500, 405, 70, 40))
                pygame.draw.rect(window, WHITE_1, (670, 400, 80, 40), border_radius=3)
                pygame.draw.rect(window, BLACK, (670, 400, 80, 40), 1, border_radius=3)
                countfont = font.render(" 1", True, BLACK)
                window.blit(countfont, (690, 405, 80, 40))

                end = solver.exploring_space.index(solver.solution_node.current)
                nodes = solver.exploring_space[:end+1]
                leng = len(nodes)
                dfs_selected = False
                bfs_selected = True
                A_selected = False
                initializeClicked = True
                count = None

            elif A_rect.collidepoint(event.pos):
                dfs_rect = pygame.draw.rect(window, WHITE_2, (500, 340, 80, 40), border_radius=3)
                dfsfont = font.render("DFS", True, BLACK)
                window.blit(dfsfont, (505, 345, 80, 40))
                bfs_rect = pygame.draw.rect(window, WHITE_2, (590, 340, 80, 40), border_radius=3)
                bfsfont = font.render("BFS", True, BLACK)
                window.blit(bfsfont, (595, 345, 40, 40))
                A_rect = pygame.draw.rect(window, WHITE_1, (680, 340, 70, 40), border_radius=3)
                Afont = font.render("A*", True, BLACK)
                window.blit(Afont, (700, 345, 40, 40))

                counterfont = font.render(" Counter ", True, WHITE, BLACK)
                window.blit(counterfont, (500, 405, 70, 40))
                pygame.draw.rect(window, WHITE_1, (670, 400, 80, 40), border_radius=3)
                pygame.draw.rect(window, BLACK, (670, 400, 80, 40), 1, border_radius=3)
                countfont = font.render(" 1 ", True, BLACK)
                window.blit(countfont, (690, 405, 80, 40))

                nodes = solver.path
                leng = len(nodes)
                A_selected = True
                bfs_selected = False
                dfs_selected = False
                initializeClicked = True
                count = None


            elif plus_rect.collidepoint(event.pos) and speedindex < speedlistlen-1:
                plus_rect = pygame.draw.rect(window, WHITE_1, (540, 260, 40, 55), border_radius=7)
                plus = font.render("+", True, BLACK)
                window.blit(plus, (550, 270, 40, 75))
                speedindex += 1
                pygame.draw.rect(window, WHITE_2, (587, 259, 125, 55), border_radius=7)
                spindex = font.render(f"{speedindex}", True, BLACK)
                window.blit(spindex, (641, 270, 100, 55))

            elif minus_rect.collidepoint(event.pos) and speedindex > 0:
                minus_rect = pygame.draw.rect(window, WHITE_1, (720, 260, 40, 55), border_radius=7)
                minus = font.render("-", True, BLACK)
                window.blit(minus, (735, 270, 40, 75))
                speedindex -= 1
                pygame.draw.rect(window, WHITE_2, (587, 259, 125, 55), border_radius=7)
                spindex = font.render(f"{speedindex}", True, BLACK)
                window.blit(spindex, (641, 270, 100, 55))

        if event.type != pygame.MOUSEBUTTONDOWN and startBgRect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, WHITE_2, (540, 150, 220, 75), border_radius=3)
            window.blit(start, (545, 173, 220, 105))

        elif event.type != pygame.MOUSEBUTTONDOWN and not startBgRect.collidepoint(pygame.mouse.get_pos()):
            startBgRect = pygame.draw.rect(window, WHITE_3, (540, 150, 220, 75), border_radius=3)
            window.blit(start, (545, 173, 220, 105))

        if event.type != pygame.MOUSEBUTTONDOWN and initial.collidepoint(pygame.mouse.get_pos()):
            initial = pygame.draw.rect(window, WHITE_2, (540, 50, 220, 75), border_radius=3)
            window.blit(init, (579, 73, 220, 105))
        elif event.type != pygame.MOUSEBUTTONDOWN and not startBgRect.collidepoint(pygame.mouse.get_pos()):
            initial = pygame.draw.rect(window, WHITE_3, (540, 50, 220, 75), border_radius=3)
            window.blit(init, (579, 73, 220, 105))

        if event.type != pygame.MOUSEBUTTONDOWN and plus_rect.collidepoint(pygame.mouse.get_pos()) and speedindex < speedlistlen-1:
            plus_rect = pygame.draw.rect(window, WHITE_2, (540, 260, 40, 55), border_radius=7)
            plus = font.render("+", True, BLACK)
            window.blit(plus, (550, 270, 40, 75))
        elif event.type != pygame.MOUSEBUTTONDOWN and not plus_rect.collidepoint(pygame.mouse.get_pos()):
            plus_rect = pygame.draw.rect(window, WHITE_3, (540, 260, 40, 55), border_radius=7)
            plus = font.render("+", True, BLACK)
            window.blit(plus, (550, 270, 40, 75))

        if event.type != pygame.MOUSEBUTTONDOWN and minus_rect.collidepoint(pygame.mouse.get_pos()) and speedindex>0:
            minus_rect = pygame.draw.rect(window, WHITE_2, (720, 260, 40, 55), border_radius=7)
            minus = font.render("-", True, BLACK)
            window.blit(minus, (735, 270, 40, 75))

        elif event.type != pygame.MOUSEBUTTONDOWN and not minus_rect.collidepoint(pygame.mouse.get_pos()):
            minus_rect = pygame.draw.rect(window, WHITE_3, (720, 260, 40, 55), border_radius=7)
            minus = font.render("-", True, BLACK)
            window.blit(minus, (735, 270, 40, 75))

        pygame.display.update()


leng = len(nodes)

while running:
    event_listener()
    if count is not None and count < leng - 1:
        update_tile_position()
    else:
        if stats:
            stats_font = pygame.font.SysFont("Segoe Print", 32, True)
            stats_font.set_underline(True)
            stats = stats_font.render("Stats", True, RED)
            stats_r = stats.get_rect()
            window.blit(stats, (10, 387, 81, 31))
            stats_font = pygame.font.SysFont(None, 30)

            generated = stats_font.render(f" Generated : {root.generated_nodes_number} ", True, BLACK, WHITE)
            generated_r = generated.get_rect()
            pygame.draw.rect(generated, RED, generated_r, 1)
            window.blit(generated, (43, 457, 231, 41))

            stats_font.set_underline(True)
            generated = stats_font.render(f" Explored with : ", True, C2)
            generated_r = generated.get_rect()
            window.blit(generated, (43, 490, 231, 41))

            stats_font.set_underline(False)
            generated = stats_font.render(f"   DFS : {len(set(solver.explored_nodes_list))}   ", True, BLACK, WHITE)
            generated_r = generated.get_rect()
            pygame.draw.rect(generated, RED, generated_r, 1)
            window.blit(generated, (150, 530, 231, 41))

            generated = stats_font.render(f"   BFS : {bfsExploredNodeNumber}   ", True, BLACK, WHITE)
            generated_r = generated.get_rect()
            pygame.draw.rect(generated, RED, generated_r, 1)
            window.blit(generated, (307, 530, 231, 41))

            generated = stats_font.render(f"   A* : {depth + 1}   ", True, BLACK, WHITE)
            generated_r = generated.get_rect()
            pygame.draw.rect(generated, RED, generated_r, 1)
            window.blit(generated, (471, 530, 231, 41))

            window.blit(stats, (10, 387, 81, 31))

            stats = None

    if count is not None and count >= leng - 1:
        stats = True

pygame.quit()

