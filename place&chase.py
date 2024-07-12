lib={'a':True}
#print(lib)
class board():
    point=[]
    inPoint=[]
    color=(0,0,0)
    def __init__(self,color,inPoint,point) -> None:
        self.color=color
        self.point=point
        self.inPoint=inPoint
class skills():
    using=None
    action=[]
    def __init__(self,using,action,classIn) -> None:
        self.using=using
        self.action=action
        classIn.append(self)
        self.type=classIn
class info():
    intro,picture=[None]*2
    def __init__(self,intro,picture) -> None:
        self.intro=intro
        self.picture=picture
class card():
    board,skills,info=[None]*3
    type=[]
    def __init__(self,board,skills,info,type) -> None:
        self.board=board
        self.skills=skills
        self.info=info
        type.append(self)
        self.type=type
    def get_belong(self,player)->None:
        self.player=player
    game.append
class game():
    turn=None
    skill=None
    event=None
    def __init__(self,turn,ground,event) -> None:
        self.turn,self.ground,self.event=turn,ground,event
class player():
    selfcard,hand,charas=[None]*3
    def __init__(self,selfcard,hand,charas)->None:
        self.card=selfcard
        self.hand=hand
        self.charas=charas
def eveadd(thing,dscp)->None:#thing记录发生主谓宾,describtion记录描述
    game.event.append({'thing':thing,'dscp':dscp})
from random import *
#from pygame import *
def my_deathsay(self,func, skill, condition=lambda self: True):
    if condition:
        self.func(**skill)
def zhouji(self)->None:
    #攻击前:此卡第一个点数+2
    if lib['a']: 
        game.skills.usings.append([self,zhouji])
        self.board.point+=2
        game.event.append([self,zhouji,game.turn])
def death_say(self,skill)->None:
    if 'dead' in self.info.status:
        enemy=game.event[-1][0]
        skill(enemy)
        eveadd([self,death_say,enemy],{'turn':game.turn})
a=card(board('red',[1],[1]),skills())
def attack_normal(self,obj,point):
    eveadd([self,attack_normal,obj])
    if lib['attack']:
        obj.board.point[0]-=point
    else:eveadd([self,attack_normal,obj],{'skilled':False})
#Ainit()

    
'''
4. **绘制游戏界面**:
   - 绘制玩家手牌区,场上卡牌区等游戏元素.
   - 显示玩家信息(生命值,已使用资源等).

5. **实现游戏逻辑**:
   - 处理玩家之间的交互,包括抽牌,打出卡牌,攻击对方玩家等.
   - 实现卡牌效果的逻辑,如造成伤害,恢复生命等.

6. **游戏循环**:
   - 实现游戏主循环,监听玩家输入并更新游戏状态.
   - 不断重绘游戏界面,显示最新的游戏状态.

7. **结束游戏**:
   - 当满足结束条件时,显示游戏结果并提供重新开始或退出游戏的选项.

通过以上步骤,你可以初步构建一个简单的卡牌游戏架构.在具体实现过程中,你可能需要处理更多细节和优化,比如卡牌效果的复杂逻辑,玩家之间的多人对战等.祝你设计开发顺利!
'''