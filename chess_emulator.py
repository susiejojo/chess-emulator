gridmatrix = [[" " for x in range(8)] for y in range(8)] 
for i in range(8):
    for j in range(8):
        if (i==0 or i==7):
            gridmatrix[i][0]="R"
            gridmatrix[i][1]="K"
            gridmatrix[i][2]="B"
            gridmatrix[i][3]="Q"
            gridmatrix[i][4]="0"
            gridmatrix[i][5]="B"
            gridmatrix[i][6]="K"
            gridmatrix[i][7]="R"
        if (i==1 or i==6):
            gridmatrix[i][0]="P"
            gridmatrix[i][1]="P"
            gridmatrix[i][2]="P"
            gridmatrix[i][3]="P"
            gridmatrix[i][4]="P"
            gridmatrix[i][5]="P"
            gridmatrix[i][6]="P"
            gridmatrix[i][7]="P"
class pieces:
    def _init_(self,x,y):
        self.positionx=x
        self.positiony=y       
class pawn(pieces):
    def __init__(self,x,y):
        pieces._init_(self,x,y)
    def show(self):
        print ("P")
    def move(self,posx,posy):
        if (gridmatrix[posx][posy]==" "):
            gridmatrix[self.positionx][self.positiony]=" "
            self.positiony=posy
            self.positionx=posx
            gridmatrix[self.positionx][self.positiony]="P"
    def move2(self,posx,posy):
        if (gridmatrix[posx][posy]==" " and gridmatrix[posx-1][posy]==" "):
            gridmatrix[self.positionx][self.positiony]=" "
            self.positiony=posy
            self.positionx=posx
            gridmatrix[self.positionx][self.positiony]="P"
        
        
class rook(pieces):
    def __init__(self,x,y):
        pass
    def show(self):
        print ("R")
    def move(self,posx,poy):
        flag1=0
        flag2=0
        for j in range(self.positiony,posy+1):
            if (gridmatrix[self.positionx][j]!=" "):
                flag1=1
                break
        for j in range(self.positionx,posx+1):
            if (gridmatrix[j][self.positiony]!=" "):
                flag2=1
                break
        if (flag1==0 or flag2==0):
            self.positionx=posx
            self.positiony=posy
            gridmatrix[posx][posy]="R"
            gridmatrix[self.positionx][self.positiony]=" "
        
class bishop(pieces):
    def __init__(self,x,y):
        pieces._init_(self,x,y)
    def show(self):
        print ("B")
    def move(self):
        if (self.positiony+1==""):
            self.positiony+=1
    def move2(self):
        if (self.positiony+1=="" and self.positiony+2==""):
            self.positiony+=2
    def capture(self):
        if (self.positionx+1 !="" and self.positiony+1!=""):
            self.positionx+=1
            self.positiony+=1
class knight(pieces):
    def __init__(self,x,y):
        pieces._init_(self,x,y)
class queen(pieces):
    def __init__(self,x,y):
        pieces._init_(self,x,y)
class king(pieces):
    def __init__(self,x,y):
        pieces._init_(self,x,y)
class grid:
    def __init__(self):
        pass
    def displaygrid(self):
        for i in range(1,18):
                if (i%2!=0):
                    print ("   +"),
                    for j in range(8):
                        print ("--- +"),
                    print
                if (i%2==0):
                    print 8-i/2+1,
                    print (" |  "+gridmatrix[i/2-1][0]+"  |  "+gridmatrix[i/2-1][1]+"  |  "+gridmatrix[i/2-1][2]+"  |  "+gridmatrix[i/2-1][3]+"  |  "+gridmatrix[i/2-1][4]+"  |  "+gridmatrix[i/2-1][5]+"  |  "+gridmatrix[i/2-1][6]+"  |  "+gridmatrix[i/2-1][7]+"  |")
        for i in range (97,105):
            print "  "+chr(i)+"   ",
        print

#main
grid1=grid()
grid1.displaygrid()
rookw1=rook(7,0)
rookw2=rook(7,7)
rookb1=rook(0,0)
rookb2=rook(0,7)
bishopw1=bishop(7,2)
bishopw2=bishop(7,5)
bishopb1=bishop(0,2)
bishopb2=bishop(0,5)
kingw=king(7,1)
kingw=king(7,6)
kingb=king(0,1)
kingb=king(0,6)
queenw=queen(7,3)
queenb=queen(0,3)
pawnw=[]
pawnw[0]=pawn(6,0)
pawnw[1]=pawn(6,1)
pawnw[2]=pawn(6,2)
pawnw[3]=pawn(6,3)
pawnw[4]=pawn(6,4)
pawnw[5]=pawn(6,5)
pawnw[6]=pawn(6,6)
pawnw[7]=pawn(6,7)
pawnb=[]
pawnb[0]=pawn(1,0)
pawnb[1]=pawn(1,1)
pawnb[2]=pawn(1,2)
pawnb[3]=pawn(1,3)
pawnb[4]=pawn(1,4)
pawnb[5]=pawn(1,5)
pawnb[6]=pawn(1,6)
pawnb[7]=pawn(1,7)
while True:
    turn=1
    if (turn%2!=0):
        print("It's white's turn!")
        string=raw_input()
        L=string.split(" ")
        piece=L[0]
        command=L[1]
        inpx=7-int(L[2])
        inpy=int(L[3])
        if (piece ):
            pawn.forName(piece).move(inpx+1,inpy-1)
            grid1.displaygrid()
        turn+=1
    if (turn%2==0):
        print("It's black's turn!")
        string=raw_input()
        L=string.split(" ")
        piece=L[0]
        command=L[1]
        inpx=7-int(L[2])
        inpy=int(L[3])
        if (piece=="pawnb1"):
            pawnb1.move(inpx+1,inpy-1)
            grid1.displaygrid()
