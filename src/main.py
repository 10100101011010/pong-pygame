from settings import * 
from sprites import * 
from groups import AllSprites
import json
import os
from os.path import join, dirname
import shutil

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.running = True

        # sound
        pygame.mixer.music.load(join('audio', '2021-10-19_-_Funny_Bit_-_www.FesliyanStudios.com.mp3')) 
        pygame.mixer.music.set_volume(0.5)                    
        pygame.mixer.music.play(-1)                                

        self.hit_sound = pygame.mixer.Sound(join('audio', '8-bit-explosion-10-340462.mp3'))
        self.hit_sound.set_volume(0.5)

        self.score_sound = pygame.mixer.Sound(join('audio', 'experimental-8-bit-sound-270302.mp3'))
        self.score_sound.set_volume(0.5)

        # sprites 
        self.all_sprites = AllSprites()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites, self.paddle_sprites))

        self.ball = Ball(
            self.all_sprites,
            self.paddle_sprites,
            self.update_score,
            self.hit_sound,
            self.score_sound
        )

        Opponent((self.all_sprites, self.paddle_sprites), self.ball)

        # score
        BASE_DIR = dirname(dirname(__file__))  
        DATA_DIR = join(BASE_DIR, 'data')
        os.makedirs(DATA_DIR, exist_ok=True)  

        self.score_path = join(DATA_DIR, 'score.txt')
        template_path = join(DATA_DIR, 'score_template.txt')

        if not os.path.exists(self.score_path):
            shutil.copyfile(template_path, self.score_path)

        with open(self.score_path) as score_file:
            self.score = json.load(score_file)

        self.font = pygame.font.Font(None, 160)

    def display_score(self):
        # player 
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg detail'])
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(player_surf, player_rect)

        # opponent
        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg detail'])
        opponent_rect = opponent_surf.get_frect(center = (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(opponent_surf, opponent_rect)

        # line separator
        pygame.draw.line(self.display_surface, COLORS['bg detail'], (WINDOW_WIDTH /2, 0), (WINDOW_WIDTH /2, WINDOW_HEIGHT), 6)

    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(self.score_path, 'w') as score_file:
                        json.dump(self.score, score_file)
            
            # update 
            self.all_sprites.update(dt)

            # draw 
            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw()
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()