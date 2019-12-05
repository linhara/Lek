import pygame
import classBird as C

WIN_WIDTH = 500
WIN_HEIGHT = 800

def main():
    bird = C.Bird(130,350)
    Bullets = []
    base = C.Base(730)
    pipes=[C.Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    shoot = False

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flapp()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    shoot = True
                    Bullets.append(C.Pewpew(bird.x, bird.y))  #byt ut nummer till bird cord

        add_pipe = False
        base.move()
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                pass
                #print("ded")
                #quit()

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        bird.move()

        if add_pipe:
            score += 1
            pipes.append(C.Pipe(600))

        for r in rem:
            pipes.remove(r)


        if bird.y + bird.img.get_height() >= 730:#or bird.y < 0:
            print("ded")
            quit()


        if shoot == True:
            for shot in Bullets:
                shot.move()



        C.draw_window(win, bird, pipes, base, score, Bullets)

main()
