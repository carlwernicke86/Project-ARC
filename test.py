import pygame, sys, random
__author__ = 'cardg_000'

GRAY = (211,211,211)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

fps = 60

WIN_W = 1000
WIN_H = 800

pygame.init()

class Hippo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 40
        self.height = 70
        self.speed = 5
        self.hunger = 6
        self.image = pygame.Surface((self.width,self.height)).convert()
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIN_W/2
        self.rect.centery = WIN_H/2

    def update(self, marble):
        key = pygame.key.get_pressed()

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > WIN_H - self.height:
            self.rect.y = WIN_H - self.height
        if self.rect.x > WIN_W - self.width:
            self.rect.x = WIN_W - self.width
        if self.rect.y < 0:
            self.rect.y = 0

        if key[pygame.K_w]:
            self.rect.y -= self.speed
        if key[pygame.K_s]:
            self.rect.y += self.speed
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed


        collision = pygame.sprite.spritecollide(self, marble, True)

        for k in collision:
            self.hunger -= 1

class Marble(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width = self.height = 5
        self.image = pygame.Surface((self.width, self.height)).convert()
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def main():
    game_loop = end_screen = True

    hippo_group = pygame.sprite.Group()
    marble_group = pygame.sprite.Group()

    clock = pygame.time.Clock()
    pygame.display.set_caption("Hippo")
    screen = pygame.display.set_mode((WIN_W, WIN_H), pygame.SRCALPHA)

    font = pygame.font.Font(None, 100)

    win = font.render("Congratulations! You Won!", 1, BLACK)
    winpos = win.get_rect()
    winpos.center = (WIN_W/2, WIN_H/2)

    hippo = Hippo()
    hippo_group.add(hippo)

    for i in range(6):
        x = random.randrange(50, WIN_W-50)
        y = random.randrange(50, WIN_H-50)
        marble = Marble(x,y)
        marble_group.add(marble)

    while game_loop:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        hunger = font.render(str(hippo.hunger), 1, GRAY)
        hungerpos = hunger.get_rect()
        hungerpos.center = (WIN_W/2, WIN_H - 100)

        screen.fill(WHITE)

        screen.blit(hunger, hungerpos)

        hippo_group.draw(screen)
        marble_group.draw(screen)

        hippo_group.update(marble_group)

        if hippo.hunger == 0:
            game_loop = False
            pygame.display.flip()

        pygame.display.flip()

        clock.tick(fps)

    while end_screen:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        screen.fill(WHITE)
        screen.blit(win, winpos)

        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()