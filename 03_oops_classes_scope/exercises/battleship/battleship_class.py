import random
class Battleship:
    import random
    def __init__(self, grid):
        self.grid=grid
        # self.x=x
        # self.y=y

    def ship(self):
        
        x=random.randrange(len(self.grid))
        y=random.randrange(len(self.grid))

        return x, y

    def hit (self):
        p=self.ship()
        self.grid[p[0]][p[1]]=1
        attempts=0
        guesses=[]
        print("enter x")
        x=input()
        print ('enter y')
        y=input()

        while self.grid[int(x)][int(y)]!=1:
            p=(int(x), int(y))
            guesses.append(p)
            attempts+=1
            print('Try again')
            print("you already hit at:", guesses)
            print("enter x")
            x=input()
            print ('enter y')
            y=input()


        print("you win!"+'with', attempts, 'attempts')


        # guesses.append(x,y)
        # attempts+=1






grid=[[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
      [0,0,0,0,0]]

field1=Battleship(grid)
field1.ship()


field1.hit()
