import time

import colorama.winterm
from ursina import *
from ursina.prefabs.first_person_controller import  FirstPersonController
import random
#trqbva da polzwam blender za da napravq figuri
#vrata v nqkoi ot uglite kudeto moga da se kriq
#nqkakwa figura shte se pokazwa ot nebeto, shte ima figuri koito se spalnvat okolo player i toi trqbva da gi strelq,shte pishe round 1 , round 2 i tn i shte stava po slojno vseki round i taka do 10ti round.Shte naprawq i nqkakwi epilepsy neshta
Destroy = False
umnojenie = 100
class Voxel(Button):
    def __init__(self, position = (0,0,0), model = "cube", scale=1, texture = "white_cube", parent = scene ):
        super().__init__(
            parent = parent,
            position = position,
            model = model,
            scale = scale,
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.lime
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                voxel = Voxel((self.position + mouse.normal))
            if key == "right mouse down":
                destroy(self)
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture = "skybox",
            scale = (300,-150,300),
            color = color.light_gray
        )
class Enemy(Entity):
    def __init__(self, model ="human", texture = "grass", scale =3 ):
        x = random.randint(30,48)
        z = random.randint(-50,50)
        super().__init__(
            parent = scene,
            position = (x,0,z),
            model = model,
            color = color.white,
            scale = scale,
            texture = texture,
        )
    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                destroy(self)
                Enemy(model="human", texture="white_cube", scale=4)



    def update(self):
        if distance(player,self.position) > 15:
            self.lookAt(self)
            self.position += self.forward *time.dt*0.0001
        else:
            self.position += self.forward * time.dt
            self.lookAt(player)
        polezrenie = Entity(parent=self, model="circle", scale=9.75, position=(0, 0.04, 0), color=color.rgb(255,204,203))
        polezrenie.rotation_x = 90
        self.collider = MeshCollider(self, mesh=enemy.model, center=Vec3(0, 0, 0))



app = Ursina()
#player
player = FirstPersonController()
player.position = (0,0,0)


#enemy
enemies = []
enemy_number = 2
for health in range(enemy_number):
    enemy = Enemy(model="human", texture="zomb",scale=3 )
    enemies.append(enemy)


def update():
    if held_keys["shift"]:
        player.speed = 10
        r = random.randint(0, 1)
        g = random.randint(0, 1)
        b = random.randint(0, 1)
        scene.fog_color = color.rgb(r,g,b)
        scene.fog_density = 0.2
    else:
        player.speed = 4
        scene.fog_color = False
        scene.fog_density = 0.01
    if held_keys["e"] and door.hovered:
        door.rotation_y = 180
    if door.rotation_y == 180:
        if held_keys["space"]:
            door.rotation_y = 90
   # if player.y == 4: BUG BUG BUG BUG
       # player.y = 1
#MAP
#sky = Sky()
door = Entity(model="Blue Door", position = (-45,1,48.1))
door.rotation_y = 90
door.collider = MeshCollider(door, mesh=door.model, center=Vec3(0, 0, 0))
ground = Entity(model="plane",texture = "grass", collider="mesh", scale =(100,1,100))
bigC = Voxel(position=(240,120,0),scale=120, texture="parva.png")
bigC.rotation_y = 45

for y in range(1,5):
    for x in range(-50,-45):
        voxel = Voxel((x, y, 45),texture="crate")
for y in range(1,5):
    for z in range(45,46):
        voxel = Voxel((-45, y, z), texture="crate")
for y in range(1,5):
    for z in range(48,50):
        voxel = Voxel((-45, y, z), texture="crate")
for y in range(1,5):
    for x in range(-50,50):
        voxel = Voxel((x,y,50), texture="crate")
for y in range(1,5):
    for z in range(-50,50):
        voxel = Voxel((50,y,z),texture="crate")
for y in range(1,5):
   for z in range(-50,50):
        voxel = Voxel((-50,y,z),texture="crate")
for y in range(1,5):
    for x in range(-50,50):
        voxel = Voxel((x,y,-50),texture="crate")



app.run()