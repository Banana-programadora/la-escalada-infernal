@namespace
class SpriteKind:
    fantasma=SpriteKind.create()
#Escenario
tiles.set_current_tilemap(tilemap("""level1"""))

#PERSONAJES

#camara
camara = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), SpriteKind.fantasma)
tiles.place_on_tile(camara, tiles.get_tile_location(4, 56))
scene.camera_follow_sprite(camara)
camara.vy=-10

#jugador
mono = sprites.create(img("""
    . . . . f f f f f . . . . . . .
    . . . f e e e e e f . . . . . .
    . . f d d d d e e e f . . . . .
    . c d f d d f d e e f f . . . .
    . c d f d d f d e e d d f . . .
    c d e e d d d d e e b d c . . .
    c d d d d c d d e e b d c . f f
    c c c c c d d d e e f c . f e f
    . f d d d d d e e f f . . f e f
    . . f f f f f e e e e f . f e f
    . . . . f e e e e e e e f f e f
    . . . f e f f e f e e e e f f .
    . . . f e f f e f e e e e f . .
    . . . f d b f d b f f e f . . .
    . . . f d d c d d b b d f . . .
    . . . . f f f f f f f f f . . .
"""), SpriteKind.player)
tiles.place_on_tile(mono, tiles.get_tile_location(3, 55))
mono.ay=300
controller.move_sprite(mono,80,0)
def on_event_pressed():
    mono.vy=-180
controller.up.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

#enemigo
def Colocar_enemigo(c,f,vx):
    enemigo = sprites.create(img("""
    . . . . c c c c c c . . . . . .
    . . . c 6 7 7 7 7 6 c . . . . .
    . . c 7 7 7 7 7 7 7 7 c . . . .
    . c 6 7 7 7 7 7 7 7 7 6 c . . .
    . c 7 c 6 6 6 6 c 7 7 7 c . . .
    . f 7 6 f 6 6 f 6 7 7 7 f . . .
    . f 7 7 7 7 7 7 7 7 7 7 f . . .
    . . f 7 7 7 7 6 c 7 7 6 f c . .
    . . . f c c c c 7 7 6 f 7 7 c .
    . . c 7 2 7 7 7 6 c f 7 7 7 7 c
    . c 7 7 2 7 7 c f c 6 7 7 6 c c
    c 1 1 1 1 7 6 f c c 6 6 6 c . .
    f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
    f 6 1 1 1 1 1 6 6 6 6 6 c f . .
    . f 6 1 1 1 1 1 1 6 6 6 f . . .
    . . c c c c c c c c c f . . . .
    """), SpriteKind.enemy)
    tiles.place_on_tile(enemigo, tiles.get_tile_location(c, f))
    enemigo.set_bounce_on_wall(True)
    enemigo.vx=vx
    enemigo.vy=0