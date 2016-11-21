import random
from itertools import count
from tabulate import tabulate

class Action(object):
    def __init__(self,name,description,bank): #constructor
        self.name=name
        self.description=description
        self.bank=bank #how it changes current player bank state
    def wyb_pola(self): #Choosing affected field
        pole=raw_input()
        self.pole=pole
    def wyb_gracza(self): #Choosing affected player
        player=raw_input()
        self.player=player
    def wyb_agenta(self): #Choosing affected agent
        agent=raw_input()
        self.agent=agent

class Card(object):
    def __init__(self,ID,actions,text,name): #constructor
        self.name=name
        self.ID=ID
        self.actions=actions
        self.text=text
    def check_card(self): #creates 1 row explaining a card
        action_names=[]
        while len(self.actions)!=0:
            current_action=self.actions.pop()
            action_names.append(current_action.name)
        card=[self.name,action_names,self.text]
        return card
    def is_reaction(self):
        if a_murd_bl_kpm in self.actions or a_murd_bl_g in self.actions:
            return True
        else:
            return False

class Agent(object):
    def __init__(self,Name,owner):
        self.name=name
        self.owner=owner
    def __init__(self,ID,name,building,agents,unrest,cost,action,neighbourhood): #constructor
        self.ID=ID
        self.building=building #0=Nobody,1+player
        self.name=name
        self.agents=agents #list in format ["1","1","2","Demon"]
        self.unrest=unrest
        self.cost=cost #Cost of buying a building
        self.action=action #Action available due to building
        self.neighbourhood=neighbourhood

    def check_state(self): #return single row presenting current state of a District
        state=[]
        state.append(self.name)
        if self.building==-1:
            state.append("Nikt")
        else:
            state.append(Players[self.building].name)
        if self.agents==[]:
            state.append("Pusto")
        else:
            agents_in=self.agents
            agents_in.sort
            agents_list=[]
            agents_to_add=[]
            while len(agents_in)>0:
                if isinstance(agents_in[0].owner,Gracz):
                    count=sum(p.owner==agents_in[0].owner for p in agents_in)
                    new= "%s agentow gracza %s" % s,agents_in[0].owner
                    agents_to_add.append(new)
                    agents_in=agents_in[sum-1,len(agents_in)]
                elif isinstance(agents_in[0].name):
                    count=sum(p.name==agents_in[0].name for p in agents_in)
                    new="%s %s(y/e)" % count,agents_in[0].name
                    agents_to_add.append(new)
                    agents_in=agents_in[sum-1,len(agents_in)]
                else:
                    break
            state.append(agents_to_add)
        if self.unrest==0:
            state.append("Spokoj")
        else:
            state.append(self.unrest)
        state.append(self.cost)
        state.append(self.action.description)
        return state

class District(object):
    def __init__(self,ID,name,building,agents,unrest,cost,action,neighbourhood): #constructor
        self.ID=ID
        self.building=building #0=Nobody,1+player
        self.name=name
        self.agents=agents #list in format ["1","1","2","Demon"]
        self.unrest=unrest
        self.cost=cost #Cost of buying a building
        self.action=action #Action available due to building
        self.neighbourhood=neighbourhood

    def check_state(self): #return single row presenting current state of a District
        state=[]
        state.append(self.name)
        if self.building==-1:
            state.append("Nikt")
        else:
            state.append(Players[self.building].name)
        if self.agents==[]:
            state.append("Pusto")
        else:
            agents_in=self.agents
            agents_in.sort
            agents_list=[]
            agents_to_add=[]
            while len(agents_in)>0:
                if isinstance(agents_in[0].owner,Gracz):
                    count=sum(p.owner==agents_in[0].owner for p in agents_in)
                    new= "%s agentow gracza %s" % s,agents_in[0].owner
                    agents_to_add.append(new)
                    agents_in=agents_in[sum-1,len(agents_in)]
                elif isinstance(agents_in[0].name):
                    count=sum(p.name==agents_in[0].name for p in agents_in)
                    new="%s %s(y/e)" % count,agents_in[0].name
                    agents_to_add.append(new)
                    agents_in=agents_in[sum-1,len(agents_in)]
                else:
                    break
            state.append(agents_to_add)
        if self.unrest==0:
            state.append("Spokoj")
        else:
            state.append(self.unrest)
        state.append(self.cost)
        state.append(self.action.description)
        return state

class Identity(object):
    def __init__(self,ID,name,win_cond): #construtor
         self.ID=ID
         self.name=name
         self.win_cond=win_cond

class Deck(object):
    def __init__(self,ID,name,cards):  #constructor
        self.ID=ID
        self.name=name
        self.cards=cards

    def Shuffle(self): #Shuffles Deck
        random.shuffle(self.cards)
    def draw(self):
        pass

class Player(object):
    def __init__(self,ID,name,identity,hand,bank):
        self.ID=ID
        self.name=name
        self.identity=identity
        self.hand=hand
        self.bank=bank
    def check_hand(self): #provides hand in table format
        hand=[]
        current_card=0
        while current_card<len(self.hand):
            hand.append(self.hand[current_card].check_card())
            current_card+=1
        return hand
    def show_hand(self): #provides hand in table format with headers
        return tabulate(self.check_hand(), headers=["Nazwa","Akcje","Tekst"])
    def check_state(self):
        state=[]
        state.append(self.ID)
        state.append(self.name)
        state.append(len(self.hand))
        state.append(self.bank)
        return state
    def check_hand_short(self):
        state=[]
        for card in self.hand:
            state.append([card.ID,card.name])
        return state
    def check_hand_reactions(self):
        state=[]
        for card in self.hand:
            if card.is_reaction=True:
                state.append([card.ID,card.name])
        return state
players=[]
sio_dol=None
dzi_mag=None
chy_rze=None
pom_bos=None
szory=None
hippo=None
mroki=None
przycmi=None
dlu_mur=None
wys_bog=None
sie_spi=None
nas_wzg=None
a_sio_dol=Action("Dodaj Agenta","Raz podczas wlasnej tury, kosztem $3, mozna ummiescic jednego wlasnego agenta w Siostrach Dolly albo dzielniy z nia sasiadujacej",-3)
a_dzi_mag=Action("Wymiana Karty","Raz podczas wlasnej tury moozna dobrac Karte Akcji, a nastepnie odrzucic jedna z posiadanych Kart Akcji",0)
a_chy_rze=Action("Pobranie $2","Raz podczas wlasnej tury mozna otrzymac $2 z banku",2)
a_pom_bos=Action("Powtrzymanie Zdarzenia","Jezeli ktorykolwiek z agentow lub budynkow Playera jest dotkniety skutkami losowego Zdarzenia, wowczas gracz moze zaplacic $3 by uchronic sie przed skutkami tego zdarzenia",-3)
a_szory=Action("Odrzucenie Karty","Raz podczas wlasnej tury mozna odrzucic Karte Akcji otrzymujac w zamian $2 z banku",2)
a_hippo=Action("Pobranie $2","Raz podczas wlasnej tury mozna otrzymac $2 z banku",2)
a_mroki=Action("Umieszczenie Niepokoju","W dowolnym momencie wlasnej tury mozna umiescic jeden znacznik niepokojow w Mrokach albo dzielnic z nia sasiadujacej",0)
a_przycmi=Action("Umieszczenie Agenta","Raz podczas wlasnej tury, kosztem $3, mozna ummiescic jednego wlasnego agenta w Przycmionej albo dzielniy z nia sasiadujacej",-3)
a_dlu_mur=Action("Pobranie $1","Raz podczas wlasnej tury mozna otrzymac $1 z banku",1)
a_wys_bog=Action("Usuniecie Niepokoju","Raz podczas wlasnej tury, kosztem $2, mozna usunac jeden znacznikk niepokojow z planszy",-2)
a_sie_spi=Action("Pobranie $3","Raz podczas wlasnej tury mozna otrzymac $3 z banku",3)
a_nas_wzg=Action("Pobranie $1","Raz podczas wlasnej tury mozna otrzymac $1 z banku",1)
sio_dol=District(1,"Siostry Dolly",-1,[],0,6,a_sio_dol,[chy_rze,dzi_mag,nas_wzg])
dzi_mag=District(2,"District Magow",-1,[],0,18,a_dzi_mag,[sio_dol,chy_rze,wys_bog,sie_spi,nas_wzg])
chy_rze=District(3,"Chytrych Rzemieslnikow",-1,[],0,12,a_chy_rze,[sio_dol,dzi_mag,wys_bog,pom_bos,szory])
pom_bos=District(4,"Pomniejsze Bostwa",-1,[],0,14,a_pom_bos,[chy_rze,szory,hippo])
szory=District(5,"Szory",-1,[],0,6,a_szory,[chy_rze,a_szory,wys_bog,pom_bos,hippo,mroki,przycmi])
hippo=District(6,"Hippo",-1,[],0,12,a_hippo,[pom_bos,szory,mroki])
mroki=District(7,"Mroki",-1,[],0,6,a_mroki,[szory,hippo,przycmi])
przycmi=District(8,"Przycmiona",-1,[],0,8,a_przycmi,[mroki,szory,dlu_mur])
dlu_mur=District(9,"Dlugi Mury",-1,[],0,12,a_dlu_mur,[przycmi,wys_bog,sie_spi])
wys_bog=District(10,"Wyspa Bogow",-1,[],0,12,a_wys_bog,[dzi_mag,chy_rze,szory,dlu_mur,sie_spi])
sie_spi=District(11,"Siedmiu Spiacych",-1,[],0,18,a_sie_spi,[dzi_mag,wys_bog,dlu_mur,nas_wzg])
nas_wzg=District(12,"Nastroszone Wzgorze",-1,[],0,12,a_nas_wzg,[sio_dol,dzi_mag,sie_spi])
districts=[sio_dol,dzi_mag,chy_rze,pom_bos,szory,hippo,mroki,przycmi,dlu_mur,wys_bog,sie_spi,nas_wzg]

def a_bank(change,player):
    player.bank=+change
def a_agent(player):
    print "Gdzie chcesz umiescic agenta?"
    for district in districts:
        print district.name "(%s)" % districts.index(district)
    current_district=raw_input
    districts(current_district).agents.append(active_player.ID)
def a_building(player):
    test=0
    for district in districts:
        if district.building=0 and districts(current_district).cost<=player.bank>0:
            test=+1
    if test=0:
        print "Kolejny wielki sukces! Na mapie nie ma zadnych budynkow, ktore moglbys kupic"
    else:
        success=0
        while success!=1
            print "Gdzie chcesz umiescic budynek?"
            for district in districts:
                print district.name "(%s)" % districts.index(district)
                current_district=raw_input
                if districts(current_district).building=0 and districts(current_district).cost<=player.bank:
                    districts(current_district).building=active_player.ID
                    player.bank=-current_district.cost
                    success=1
                elif districts(current_district).building!=0:
                    print "Nie mozesz, znajduje sie tam budynek gracza %s." % Players(districts(current_district).building).name
                    print "Czy chcesz zrezygnowac z tej akcji? Jesli tak, wpisz 1. Jesli nie, wpisz cos innego"
                    success=raw_input
                elif districts(current_district).cost>player.bank:
                    print "Nie mozesz, masz ma malo monet."
                    print "Czy chcesz zrezygnowac z tej akcji? Jesli tak, wpisz 1. Jesli nie, wpisz cos innego"
                    success=raw_input
def a_rem_unrest():
    test=0
    for district in districts:
        if district.unrest>0:
            test=+1
    if test=0:
        print "Kolejny wielki sukces! Na mapie nie ma zadnych niepokojow"
    else:
        success=0
        while success!=1
            print "Gdzie chcesz usunac niepokoj?"
            for district in districts:
                print district.name "(%s)" % districts.index(district)
                current_district=raw_input
                if districts(current_district).unrest>0:
                    districts(current_district).unsrest=-1
                    success=1
                else:
                    print "Nie mozesz, nie ma tam niepokojow"
                    print "Czy chcesz zrezygnowac z tej akcji? Jesli tak, wpisz 1. Jesli nie, wpisz cos innego"
                    success=raw_input
def a_murd_bl_g(district,player):
    current_player=player
    print "Twoj agent w %s jest atakowany" % district.name
    success=0
    if len(current_player.check_hand_reactions()==0:
        print "Ale nie mozesz mu pomoc! : ("
        success=1
    while success!=1:
        print "Czy chcez go uratowac?[t/n]"
        choice=raw_input
        if choice==t:
            print "Ktora karte chcesz zagrac?"
            print current_player.check_hand_reactions()
            card=raw_input
            if card in current_player.check_hand_reactions():
                play_card(card)
                success=1
            else:
                print "To bez sensu"
                print "Czy chcesz zrezygnowac z tej akcji? Jesli tak, wpisz 1. Jesli nie, wpisz cos innego"
                success=raw_input
        elif choice==n:
            print "To nie"
            success=1
        else:
            print "Czo?"

def a_murd_bl_kpm():
def a_murd_bl_g():

def main():
    game_start()
    while len(Brown.cards)!=0:#Checks Game End conditiion
        pass

def player_creation(): #Creates all players
    print "Ilu bedzie graczy?"
    player_count=raw_input()
    player_count=int(player_count)
    player_id=0
    player_identity=0
    player_hand=[]
    while player_count!=0:
        print "Jak masz na imie?"
        player_name=raw_input()#Creates name
        player_id+=1#Creates correct ID
        player_identity=Identities.pop()#Creates identity
        player_identity=player_identity.ID
        while len(player_hand)<5:#Creates hand
                player_hand.append(Green.cards.pop())
        player_bank=10#Creates bank
        players.append(Player(player_id,player_name,player_identity,player_hand,player_bank))#adds player to players list
        player_count-=1
        print "Stworzono gracza %s" % player_name
    print Players

def game_start(): #Creates start setting
    print "Poczatek Gry"
    player_creation()
    active_player=0
    turn=0
    while active_player<len(Players):
        sio_dol.agents.append(["Agent",Players[active_player]])
        szory.agents.append(["Agent",Players[active_player]])
        mroki.agents.append(["Agent",Players[active_player]])
        active_player+=1 #Creates start board setting

def turn():
    active_player=0
    while active_player<len(players):
        end_turn=False
        print "Tura gracza %s" % Players[active_player].name
        print "Co chcesz zrobic?"
        while end_turn!=True:
            print "Obejrzec moje karty(1), obejrzec plansze(2), sprawdzic sytuacje innych graczy(3), zagrac swoja karte(4), skorzystac z ktoregoes ze swoich budynkow(5)"
            move=raw_input()
            if move==1:
                print "Twoje karty"
                print Players[active_player].show_hand
            elif move==2:
                print "Sytuacja na planszy"
                print full_map_state()
            elif move==3:
                print "Sytuac   ja wszystkich graczy"
                print full_players_state()
            elif move==4:
                print "Ktora karte chhcesz zagrac?"
                print check_hand_short
                card=raw_input
            pass
        active_player+=1

def full_map_state():
    header=["Nazwa","Wlasciciel","Agenci","Niepokoje","Cena Budynku","Pozwala na"]
    full_state=[]
    for district in districts:
        full_state.append(district.check_state())
    return tabulate (full_state,header)

def full_players_state():
    header=["Numer","Imie","Kart w rece","Bank"]
    full_state=[]
    for player in players:
        full_state.append(player.check_state())
    return tabulate (full_state,header)



Identities=[]
Vetinari=Identity(1,"Vetinari","Test1")
Potato=Identity(2,"Potato","Test2")
Identities.append(Vetinari)
Identities.append(Potato)
random.shuffle(Identities)
cards_in_deck=range(1,40)
Brown=Deck(2,"Brown",cards_in_deck)
Brown.cards_in_deck=[]
Green=Deck(1,"Green",cards_in_deck)
Jezus=Player(1,"Imie",Vetinari,districts,5)

print tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'])

print sio_dol.action.description
print full_map_state()
print Jezus.check_state()
a_bank(change=-1,player=Jezus)
print Jezus.check_state()

'''print Smierc.text
print Ziemniak.text
Cos=Deck()
Cos.cards_in_deck=[12,3,4,4,5,345,34,534,5,35]
Cos.Shuffle()
print Cos.cards_in_deck'''
''''
skryt=Action("Skrytobojstwo")
budynek=Action("Postaw Budynek")
smierc=Card("1",[skryt,skryt,budynek],"WITAM","Smierc")
ziemniak=Card("1",[skryt,skryt,budynek],"Potato potato","Ziemniak")
Jezus=Gracz(1,"Jezus",Vetinari,[smierc,ziemniak],3)
'''
'''   (self,ID,agent,budynek,skryt,usun,pieniadze,zwoj,zdarzenie):
        self.ID=ID
        self.agent=agent
        self.budynek=budynek
        self.skryt=skryt
        self.usun=usun
        self.pieniadze=pieniadze
        self.zwoj=zwoj
        self.zdarzenie=zdarzenie'''
