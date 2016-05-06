import random as r

class Organism:
    def __init__(self, ident, x_start, y_start):
        lifeforms.append(self)
        self.age = 0
        self.x = x_start
        self.y = y_start
        self.alive = True
        self.ident = ident

    def active(self):
        self.move()
        self.age += 1
        if self.energy <= 0:
            self.alive = False
            self.x, self.y = -1, -1
        if self.age == self.dna['repro']:
            self.divide()

    def move(self):
        '''Moves organism distance determined by its dna['speed'] parameter'''

        speed = self.dna['speed']
        direction_list = {'left': (-speed, 0),
                        'right': (speed, 0),
                        'up': (0, speed),
                        'down': (0, -speed),
                        None: (0, 0)}

        new_move = r.choice(list(direction_list.keys()))
        (new_x, new_y) = (self.x + direction_list[new_move][0], 
                        self.y + direction_list[new_move][1])
        if new_move == None:
            return
        if new_x in range(10) and new_y in range(10):
            self.x, self.y = new_x, new_y
            self.energy -= self.dna['metabolism']
        else:
            return

    def divide(self):
        '''Creates two new daughter bacteria, sets self.alive to False,
        moves self to (-1, -1)'''

        for i in range(2):
            organism_creator(self.x, self.y)
        self.alive = False
        self.x, self.y = -1, -1



class Bacterium(Organism):
    def __init__(self, ident, x_start, y_start):
        super().__init__(ident, x_start, y_start)
        self.dna = {'speed': 1, 'metabolism': 5, 'repro': 5}
        self.energy = 100
        self.icon = 'X'


def organism_creator(x_start, y_start):
    '''Makes one new organism at given location and gives it an id number'''

    ident = len(lifeforms)
    new_bacterium = Bacterium(ident, x_start, y_start)
    return new_bacterium


def world_printer(lifeforms):
    '''Takes a list of lifeform objects and prints their locations'''

    world = [[' ' for i in range(10)] for i in range(10)]
    print('\n')
    for lifeform in lifeforms:
        if lifeform.alive == True:
            location = world[lifeform.y][lifeform.x]
            if location == ' ':
                thing = lifeform.icon
            else:
                thing = location + lifeform.icon
            world[lifeform.y][lifeform.x] = thing
    for line in world:
        print(''.join(line))
    print('\n')



lifeforms = []
for i in range(5):
    organism_creator(r.randint(0, 9), r.randint(0, 9))
world_printer(lifeforms)
while True:
    for lifeform in lifeforms:
        lifeform.active()
    world_printer(lifeforms)
    input('Advance?')
world_printer(lifeforms)


