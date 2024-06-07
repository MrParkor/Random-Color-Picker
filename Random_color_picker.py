#Imports
from random import randint
from colorist import ColorRGB, BgColorRGB 


#Variables
COLOR_1_GE3TAMRQGM : list = []
CLOSE_COLOR_GAZTAMJXGE : list = [0,0,0]
CONTRAST_GAZTANJQGQ : list = [0,0,0]
PLUS_OR_MINUSGI2DCMJSGA : int = randint(1,2)

BigColorChange : int = randint(50,70)
SmallColorChange : int = randint(1,10)

#Code
def BigColorAdder(CompareList : list, CompareIndex : int, ChangeList : list, ChangeIndex : int):
    if CompareList[CompareIndex] + BigColorChange <= 255:
        ChangeList[ChangeIndex] = CompareList[CompareIndex] + BigColorChange
    else:
        ChangeList[ChangeIndex] = CompareList[CompareIndex] - BigColorChange

def BigColorSub(CompareList : list, CompareIndex : int, ChangeList : list, ChangeIndex : int):
    if CompareList[CompareIndex] - BigColorChange >= 0:
        ChangeList[ChangeIndex] = CompareList[CompareIndex] - BigColorChange
    else:
        ChangeList[ChangeIndex] = CompareList[CompareIndex] + BigColorChange

def SmallColorAdder(CompareList : list, CompareIndex : int, ChangeList : list, ChangeIndex : int):
    if CompareList[CompareIndex] + SmallColorChange <= 255:
        ChangeList[ChangeIndex] = CompareList[CompareIndex] + SmallColorChange
    else:
        ChangeList[ChangeIndex] = CompareList[CompareIndex] - SmallColorChange
        
def SmallColorSub(CompareList : list, CompareIndex : int, ChangeList : list, ChangeIndex : int):
    if CompareList[CompareIndex] - SmallColorChange >= 0:
        ChangeList[ChangeIndex] = CompareList[CompareIndex] - SmallColorChange
    else:
        ChangeList[ChangeIndex] = CompareList[CompareIndex] + SmallColorChange
        
        
        
        

def MainColorPicker298DB() -> None:
    for _ in range(3): # COLOR_1_GE3TAMRQGM
        COLOR_1_GE3TAMRQGM.append(randint(0,255))  
#FIRST_COLOR = ColorRGB(COLOR_1_GE3TAMRQGM[0],COLOR_1_GE3TAMRQGM[1],COLOR_1_GE3TAMRQGM[2])

def CloseColorPicker75DB() -> None:
    ColorChange :int = randint(1,len(COLOR_1_GE3TAMRQGM)-1)
    
    NumberOfColorChange : int = randint(1,2)



    if NumberOfColorChange == 1:
        if PLUS_OR_MINUSGI2DCMJSGA == 1: # Plus
            if ColorChange == 0:
                BigColorAdder(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
            if ColorChange == 1:
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                BigColorAdder(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
            if ColorChange == 2:
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                BigColorAdder(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)

        if PLUS_OR_MINUSGI2DCMJSGA == 2: # Minus
            if ColorChange == 0:
                BigColorSub(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                SmallColorSub(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                SmallColorSub(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
            if ColorChange == 1:
                SmallColorSub(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                BigColorSub(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                SmallColorSub(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
            if ColorChange == 2:
                SmallColorSub(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                SmallColorSub(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                BigColorSub(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
    
    if NumberOfColorChange == 2:
        if PLUS_OR_MINUSGI2DCMJSGA == 1: # Plus
            if ColorChange == 0:
                BigColorAdder(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                BigColorAdder(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
            if ColorChange == 1:
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                BigColorAdder(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                BigColorAdder(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
            if ColorChange == 2:
                SmallColorAdder(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                BigColorAdder(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                BigColorAdder(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)

        if PLUS_OR_MINUSGI2DCMJSGA == 2: # Minus
            if ColorChange == 0:
                BigColorSub(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                BigColorSub(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                SmallColorSub(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
            if ColorChange == 1:
                SmallColorSub(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                BigColorSub(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                BigColorSub(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)
            if ColorChange == 2:
                BigColorSub(COLOR_1_GE3TAMRQGM, 0, CLOSE_COLOR_GAZTAMJXGE, 0)
                SmallColorSub(COLOR_1_GE3TAMRQGM, 1, CLOSE_COLOR_GAZTAMJXGE, 1)
                BigColorSub(COLOR_1_GE3TAMRQGM, 2, CLOSE_COLOR_GAZTAMJXGE, 2)

def ContrastColorPicker7728() -> None:
    CONTRAST_GAZTANJQGQ[0] = 255-COLOR_1_GE3TAMRQGM[0]
    CONTRAST_GAZTANJQGQ[1] = 255-COLOR_1_GE3TAMRQGM[1]
    CONTRAST_GAZTANJQGQ[2] = 255-COLOR_1_GE3TAMRQGM[2]
    

def PrintColors3ADE0() -> None:
    FIRST_COLOR = ColorRGB(COLOR_1_GE3TAMRQGM[0], COLOR_1_GE3TAMRQGM[1], COLOR_1_GE3TAMRQGM[2])
    FIRST_COLOR_BG = BgColorRGB(COLOR_1_GE3TAMRQGM[0], COLOR_1_GE3TAMRQGM[1], COLOR_1_GE3TAMRQGM[2])
    
    SECOND_COLOR = ColorRGB(CLOSE_COLOR_GAZTAMJXGE[0], CLOSE_COLOR_GAZTAMJXGE[1], CLOSE_COLOR_GAZTAMJXGE[2])
    SECON_COLOR_BG = BgColorRGB(CLOSE_COLOR_GAZTAMJXGE[0], CLOSE_COLOR_GAZTAMJXGE[1], CLOSE_COLOR_GAZTAMJXGE[2])
    
    THIRD_COLOR = ColorRGB(CONTRAST_GAZTANJQGQ[0], CONTRAST_GAZTANJQGQ[1], CONTRAST_GAZTANJQGQ[2])
    THIRD_COLOR_BG = BgColorRGB(CONTRAST_GAZTANJQGQ[0], CONTRAST_GAZTANJQGQ[1], CONTRAST_GAZTANJQGQ[2])
    

    print(f"Main Color: {COLOR_1_GE3TAMRQGM} {FIRST_COLOR} {FIRST_COLOR_BG}  {FIRST_COLOR.OFF} {FIRST_COLOR_BG.OFF}")  
    print(f"Close Color: {CLOSE_COLOR_GAZTAMJXGE}  {SECOND_COLOR} {SECON_COLOR_BG}  {SECOND_COLOR.OFF} {SECON_COLOR_BG.OFF}")
    print(f"CONTRAST_GAZTANJQGQ: {CONTRAST_GAZTANJQGQ}  {THIRD_COLOR} {THIRD_COLOR_BG}  {THIRD_COLOR.OFF} {THIRD_COLOR_BG.OFF}")
      

def Main() -> None:
    MainColorPicker298DB()
    CloseColorPicker75DB()
    ContrastColorPicker7728()
    PrintColors3ADE0()



#Run
if __name__ == "__main__":
    Main()


