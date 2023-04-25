from ursina import *
import numpy as np

board_entities = []

turn = 0
key_list=[]
val_list=[]
test=[
    [[0,1,2],[3,4,5],[6,7,8]],
      [[9,10,11],[12,13,14],[15,16,17]],
      [[18,19,20],[21,22,23],[24,25,26]]
      ]
winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14],
        [15, 16, 17], [18, 19, 20], [21, 22, 23], [24, 25, 26],

        [0, 3, 6], [1, 4, 7], [2, 5, 8], [9, 12, 15], [10, 13, 16],
        [11, 14, 17], [18, 21, 24], [19, 22, 25], [20, 23, 26],

        [0, 4, 8], [2, 4, 6], [9, 13, 17], [11, 13, 15], [18, 22, 26],
        [20, 22, 24],

        [0, 9, 18], [1, 10, 19], [2, 11, 20], [3, 12, 21], [4, 13, 22],
        [5, 14, 23], [6, 15, 24], [7, 16, 25], [8, 17, 26],

        [0, 12, 24], [1, 13, 25], [2, 14, 26], [6, 12, 18], [7, 13, 19],
        [8, 14, 20], [0, 10, 20], [3, 13, 23], [6, 16, 26], [2, 10, 18],
        [5, 13, 21], [8, 16, 24], [0, 13, 26], [2, 13, 24], [6, 13, 20],
        [8, 13, 18]
    )

coords=[]
mapper={}
x_p=[]
o_p=[]

colors = {
    'white': color.rgba(255, 255, 255, 255),
    'red': color.rgba(255, 0, 0, 255),
    'blue': color.rgba(0, 0, 255, 255),
}

app = Ursina()


class Cube(Entity):

    def __init__(self, origin_x=0, origin_y=0, origin_z=0):
        super().__init__(
            model='cube',
            texture='white_cube',
            Text='test',
            color=colors['white'],
            collider='box',
            origin_x=origin_x,
            origin_y=origin_y,
            origin_z=origin_z,
        )

        self.marked = 'none'

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if mark_cube(self):
                # destroy(self)
                    ai();

def ai():
    # print(np.array(board_entities).shape)
    t=board_entities[random.randint(0,2)][random.randint(0,8)]
    # print(board_entities[0][0])
    # t.origin=Vec3(2.0,-2.0,2.0)
    # board_entities[0].origin_x=-2.0,
    # board_entities[0].origin_z=2.0,
    t.marked = 'red'
    t.color = colors['red']
    
def mark_cube(e):
    # print(e.origin_x,e.origin_y,e.origin_z)
    
    if e.marked != 'none':
        return
    
    

    else:
        # print(val_list)
        e.marked = 'blue'
        e.color = colors['blue']
        # print(list(e.origin))
        for l ,i in zip(val_list,range(27)):
            if l==list(e.origin):
                print(i)

                x_p.append(i)

                print(x_p)
        # if 
        return True
    # e = Cube(
    #             origin_y=2.0,
    #             origin_x=-2.0,
    #             origin_z=2.0,
    #         )
    # e.marked = 'red'
    # e.color = colors['red']


def create_assets():
    n=0
    for i in np.linspace(-2, 2, 3):
        board = []
        for j in np.linspace(-2, 2, 3):
            for k in np.linspace(-1, 2, 3):
                print(n,i,j,k)
                coords.append([i,j,k])
                n+=1
                e = Cube(
                    origin_y=i,
                    origin_x=j,
                    origin_z=k,
                )
                board.append(e)
        board_entities.append(board)
    # print(board_entities)


EditorCamera()


def main():
    global val_list,key_list
    create_assets()
    for i,j in zip(range(27),coords):
        mapper[i]=j
    print(mapper[0])
    key_list = list(mapper.keys())
    val_list = list(mapper.values())
    
    # print key with val 100
    # print(val_list.index([2.0 -2.0 -1.0]))

    app.run()
    print(x_p)


if __name__ == "__main__":
    main()