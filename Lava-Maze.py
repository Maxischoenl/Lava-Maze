import arcade.color
import pyglet
pyglet.options["osx_alt_loop"] = True

import arcade

    
class Labyrinth(arcade.Window):
    def __init__(self):
        super().__init__(1000, 500, "Lava Maze")
        self.stop = False

        arcade.set_background_color(arcade.color.LIGHT_RED_OCHRE)
        self.lul = arcade.load_sound("Maze.wav")
        arcade.play_sound(self.lul,looping = True)
        
        self.restart()

    def restart(self):
        
        self.stop=False
        self.block_liste = arcade.SpriteList()
        self.spieler_liste = arcade.SpriteList()
        self.win_liste = arcade.SpriteList()
        self.sponsor_liste = arcade.SpriteList()
        self.Bewegen_liste = arcade.SpriteList()
        self.Pfeil1_liste = arcade.SpriteList()
        self.Pfeil2_liste = arcade.SpriteList()
        self.Pfeil3_liste = arcade.SpriteList()
        self.Pfeil4_liste = arcade.SpriteList()
        self.Time= 60

        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 75
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 175
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25                                                                             
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 25
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 75
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 125
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 175
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 225
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 325
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 425
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 75
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 175
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 475
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 425
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 325
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 225
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 175
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 125
        block.center_y = 25
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 75
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 125
        block = arcade.Sprite("block.png")
        block.center_x = 175
        block.center_y = 75
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 125
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 175
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 75
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 175
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 375
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 175
        block.center_y = 175
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 175
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 125
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 125
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 125
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 125
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 225
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 225
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 275
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 525
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 75
        block.center_y = -25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 625
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 75
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 725
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 175
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 575
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 525
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 625
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 175
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 675
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 725
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 775
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 775
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 775
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 825
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 825
        block.center_y = 175
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 825
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 775
        block.center_y = 375
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 775
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 775
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 825
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 875
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 925
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 975
        block.center_y = 25
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 925
        block.center_y = 75
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 925
        block.center_y = 125
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 925
        block.center_y = 175
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 925
        block.center_y = 225
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 925
        block.center_y = 275
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 925
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 875
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 775
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 725
        block.center_y = 475
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 825
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 875
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 975
        block.center_y = 325
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 925
        block.center_y = 425
        self.block_liste.append(block)
        block = arcade.Sprite("block.png")
        block.center_x = 975
        block.center_y = 425
        self.block_liste.append(block)

        self.sponsor = arcade.Sprite("Sponsor.png")
        self.sponsor.center_y = 475
        self.sponsor.center_x = 950
        self.sponsor_liste.append(self.sponsor)

        self.Bewegen = arcade.Sprite("Kiste.png", 0.2)
        self.Bewegen.center_x = 625
        self.Bewegen.center_y = 425
        self.Bewegen.change_y = -2
        self.Bewegen_liste.append(self.Bewegen)
        self.Bewegen = arcade.Sprite("Kiste.png", 0.2)
        self.Bewegen.center_x = 525
        self.Bewegen.center_y = 425
        self.Bewegen.change_y = -1.9
        self.Bewegen_liste.append(self.Bewegen) 

        self.spieler = arcade.Sprite("Steve.png", 0.08)
        self.spieler.center_x = 75
        self.spieler.center_y = 25
        self.spieler_liste.append(self.spieler)

        self.joystickH = arcade.Sprite("Joystick Hintergrund.png")
        self.joystickH.center_x = 945
        self.joystickH.center_y = 50
        self.block_liste.append(self.joystickH)

        self.Pfeil1 = arcade.Sprite("Pfeil.png")
        self.Pfeil1.center_x = 945
        self.Pfeil1.center_y = 75
        self.Pfeil1_liste.append(self.Pfeil1)

        self.Pfeil2 = arcade.Sprite("pfeil2.png")
        self.Pfeil2.center_x = 970
        self.Pfeil2.center_y = 50
        self.Pfeil2_liste.append(self.Pfeil2)

        self.Pfeil3 = arcade.Sprite("Pfeil3.png")
        self.Pfeil3.center_x = 945
        self.Pfeil3.center_y = 25
        self.Pfeil3_liste.append(self.Pfeil3)

        self.Pfeil4 = arcade.Sprite("Pfeil4 .png")
        self.Pfeil4.center_x = 920
        self.Pfeil4.center_y = 50
        self.Pfeil4_liste.append(self.Pfeil4)
        
        self.bananenengine = arcade.PhysicsEngineSimple(self.spieler, [self.block_liste,self.Bewegen_liste])

    def on_key_press(self, symbol: int, modifiers: int):
        if self.stop==False:
            if symbol == arcade.key.W:
                self.spieler.change_y = 1.6
            if symbol == arcade.key.S:
                self.spieler.change_y = -1.6
            if symbol == arcade.key.D:
                self.spieler.change_x = 1.6
            if symbol == arcade.key.A:
                self.spieler.change_x = -1.6 
        if symbol == arcade.key.R:
            self.restart()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.spieler.change_y = 0
        if symbol == arcade.key.S: 
            self.spieler.change_y = 0
        if symbol == arcade.key.D:
            self.spieler.change_x = 0   
        if symbol == arcade.key.A:
            self.spieler.change_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        mauszeiger_sprite = arcade.Sprite()
        mauszeiger_sprite.center_x = x
        mauszeiger_sprite.center_y = y
        mauszeiger_sprite.set_hit_box([(2, 0), (-2, 2), (-2, -2), (2, -2)])

        if arcade.check_for_collision_with_list(mauszeiger_sprite, self.Pfeil1_liste):
            self.spieler.change_y = 1.6
            self.Pfeil1.texture = arcade.load_texture("Pfeil_grün.png")
        if arcade.check_for_collision_with_list(mauszeiger_sprite, self.Pfeil2_liste):
            self.spieler.change_x = 1.6
            self.Pfeil2.texture = arcade.load_texture("pfeil2_grün.png")
        if arcade.check_for_collision_with_list(mauszeiger_sprite, self.Pfeil3_liste):
            self.Pfeil3.texture = arcade.load_texture("Pfeil3_grün.png")
            self.spieler.change_y = -1.6      
        if arcade.check_for_collision_with_list(mauszeiger_sprite, self.Pfeil4_liste):
            self.Pfeil4.texture = arcade.load_texture("Pfeil4_grün.png")
            self.spieler.change_x = -1.6

    def on_mouse_release(self, x, y, button, modifiers):

            self.spieler.change_y = 0 
            self.Pfeil1.texture = arcade.load_texture("Pfeil.png")
            self.spieler.change_x = 0
            self.Pfeil2.texture = arcade.load_texture("pfeil2.png")
            self.spieler.change_y = 0
            self.Pfeil3.texture = arcade.load_texture("Pfeil3.png")     
            self.spieler.change_x = 0
            self.Pfeil4.texture = arcade.load_texture("Pfeil4 .png")

    def on_draw(self):
        self.clear()
        self.Bewegen_liste.draw()
        self.block_liste.draw()
        self.Pfeil1_liste.draw()
        self.Pfeil2_liste.draw()
        self.Pfeil3_liste.draw()
        self.Pfeil4_liste.draw()
        self.spieler_liste.draw()
        self.win_liste.draw()
        self.sponsor_liste.draw()
        
        arcade.draw_text(round(self.Time), 20, 20, arcade.color.WHITE, 12)
        if round(self.Time) == 0:
            self.stop = True
            self.lose = arcade.Sprite("Bananen.jpg")
            self.lose.center_x = 1000/2
            self.lose.center_y = 500/2
            self.win_liste.append(self.lose)
        
    def on_update(self, delta_time: float):
        self.clear()
        self.bananenengine.update()
        self.spieler_liste.update()
        self.win_liste.update()
        self.block_liste.update()
        self.sponsor_liste.update()
        self.Bewegen_liste.update()
        for bewegen in self.Bewegen_liste:
            if bewegen.center_y < 25 :
                bewegen.change_y = 1.3
            if bewegen.center_y > 375 :
                bewegen.change_y = -1.3  
        if self.spieler.center_x >= 1000:
            self.win = arcade.Sprite("win.png")
            self.win.center_x = 1000/2
            self.win.center_y = 500/2
            self.win_liste.append(self.win)
            self.stop = True
        if self.stop == False:
            self.Time = self.Time - delta_time


Labyrinth()
arcade.run()
# :):):):):):):):):):):)