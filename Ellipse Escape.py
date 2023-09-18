from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse, Color
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
import random

class Player(Widget):
    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.size = (70, 70)
        self.pos = (50, Window.height / 2)
        self.jumping = False
        self.score = 0
        with self.canvas:
            Color(1, 0, 0)  # sets color to red
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.score_label = Label(text=f"{self.score}", pos=(self.pos[0] + 20, self.pos[1] + 20), font_size='20sp')
        self.add_widget(self.score_label)

    def jump(self):
        self.jumping = True

    def fall(self):
        self.jumping = False

    def update(self):
        if self.jumping and self.pos[1] < Window.height - self.size[1]:
            self.pos = (self.pos[0], self.pos[1] + 10)
        elif not self.jumping and self.pos[1] > 0:
            self.pos = (self.pos[0], self.pos[1] - 10)
        self.ellipse.pos = self.pos
        self.score_label.pos = (self.pos[0] + 20, self.pos[1] + 20)

    def increment_score(self, dt):
        self.score += 1
        self.score_label.text = f"{self.score}"

class Hurdle(Widget):
    def __init__(self, player, **kwargs):
        super(Hurdle, self).__init__(**kwargs)
        self.size = (50, random.randint(50, 300)) if random.random() < 0.7 else (50, random.randint(50, 150))
        self.pos = (Window.width, random.randint(0, Window.height - self.size[1]))
        with self.canvas:
            Color(random.random(), random.random(), random.random())  # sets color to a random color
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.speed = 2
        self.player = player

    def update(self):
        self.pos = (self.pos[0] - self.speed, self.pos[1] - self.speed if self.pos[1] > self.player.pos[1] else self.pos[1] + self.speed if self.pos[1] < self.player.pos[1] else self.pos[1])
        self.rect.pos = self.pos

class Game(Widget):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.player = Player()
        self.hurdle = Hurdle(self.player)
        self.add_widget(self.player)
        self.add_widget(self.hurdle)
        self.is_game_over = False
        self.update_event = Clock.schedule_interval(self.update, 1/60)
        self.score_event = Clock.schedule_interval(self.player.increment_score, 1)

    def on_touch_down(self, touch):
        self.player.jump()

    def on_touch_up(self, touch):
        self.player.fall()

    def update(self, dt):
        self.hurdle.update()
        self.player.update()
        if self.player.collide_widget(self.hurdle) or self.player.top > Window.height or self.player.y < 0:
            self.is_game_over = True
            self.update_event.cancel()
            self.score_event.cancel()
            self.game_over()

        if self.hurdle.pos[0] < 0:
            self.hurdle.canvas.clear()
            with self.hurdle.canvas:
                Color(random.random(), random.random(), random.random())
                self.hurdle.rect = Rectangle(pos=self.hurdle.pos, size=self.hurdle.size)
            self.hurdle.pos = (Window.width, random.randint(0, Window.height - self.hurdle.size[1]))
            if self.player.score != 0 and self.player.score % 10 == 0:
                self.hurdle.speed += 5

    def game_over(self):
        view = ModalView(size_hint=(None, None), size=(300, 200))
        view.add_widget(Label(text=f"Game Over\nScore: {self.player.score}"))
        view.open()

class GameApp(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    GameApp().run()
