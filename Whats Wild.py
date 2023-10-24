import pydealer
from pydealer.const import POKER_RANKS

# Set the default rank dict to reference.
deck = pydealer.Deck(rebuild=True, re_shuffle=True)
deck = pydealer.Deck(ranks=POKER_RANKS)
hand = pydealer.Stack()
comm = pydealer.Stack()

totalin=0
totalwin=0
thit = 0

#Start of Game
startbet = 25 #starting bet, change this to test RTP
tricard = 10 #second bet

bet1 = startbet #betting points, we MUST bet but we can PULL bets out
bet2 = startbet
bet3 = startbet

LetItRide=0 #if Let it Ride = 1, then we got something, dont pull bet.

# Add the cards to the top of the hand (Stack).
deck.shuffle()
hand = deck.deal(1)
hand += deck.deal(1)
hand += deck.deal(1)
hand.sort()
print ("v roki imamo: ")
print (hand)

strranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
keep = ["10", "J", "Q", "K", "A"] #change here if you wanna keep more

#cards = deck.find_list(keep)
handkeep = hand.find_list(keep)


#3cardbonus bet
for x in range (3):
    for y in range(3):
        if((hand[x].value == hand[y].value) & (x != y)):
            thit = 1 #pair
            if((hand[0].value==hand[1].value) & (hand[1].value==hand[2].value)):
                thit= 30 #Triple
                LetItRide=1 #če imamo triple, potem avtomatsko let it ride
                break
            
for z in range(len(strranks)-2):
    if ((hand[0].value==strranks[z])&(hand[1].value==strranks[z+1])&(hand[2].value==strranks[z+2])):
        thit= 6 #straight
        break

if((hand[0].suit==hand[1].suit) & (hand[1].suit==hand[2].suit)):
    if (thit== 6):
        thit= 40 #Straight flush
    else:
        thit= 3 #flush
        
print (thit)
print ("\n")
#Check do we Pull or Let it Ride?
if len(handkeep) > 1:
   for x in range(len(handkeep)):
        for y in range(len(handkeep)):
            if (hand[handkeep[y]].value == hand[handkeep[x]].value) & (y != x):
                LetItRide=1
                break
                
if LetItRide == 1:
   print ("Let It Ride")  
else:
    bet1=0 #We PULL, take back first bet
    print ("Pull")

#Reveal the first card
comm += deck.deal(1)
print ("na mizi imamo: ")
print (comm)

if LetItRide == 0:
    if len(handkeep) > 0:
       for x in range(len(handkeep)):
            if (hand[handkeep[x]].value == comm[0].value):
                    LetItRide=1
                    break
    for i in range(1,3):
        if (hand[0].value == hand[i].value):
            for j in range (1,3):
                for k in range (2,3):
                    if((hand[j].value == hand[k].value) & (j!=k)):
                        LetItRide=1
                        break
if LetItRide == 1:
   print ("Let it Ride")  
else:
    bet2=0 #We PULL, take back second bet
    print ("Pull")
hand += comm.deal(1)
hand.sort()
handkeep = hand.find_list(keep)

#povlečemo WILD karto    
wild = deck.deal(1)
wilder = wild[0].value
numwild = 0
print ("Wild:")
print (wilder)
cards = [0, 1, 2, 3]
#check we have any wild in hand
for i in range(len(hand)):
    if(hand[i].value == wilder):
        numwild = numwild+1
        print ("Imamo wild karto:")
        print (hand[i])
        
if (numwild > 0) & (LetItRide == 0):        
        if (numwild >1):
            LetItRide = 1 #če imaš dva wilda je avtomatsko triple? ali pa dva para+
        else:
            if(len(handkeep)>0):
                LetItRide = 1 #high pair
            for i in range (0,4):
                temp = [0, 1, 2, 3]
                temp.remove(i)
                if((hand[temp[0]].value) == (hand[temp[1]].value) == (hand[temp[2]].value)):
                    LetItRide = 1 #imamo 4ofaKind
                    find = 1
                    break

if (LetItRide == 1):
    print ("Let it Ride")  
else:
    bet3=0 #We PULL, take back third bet
    print ("Pull")

print (bet1,bet2,bet3)              
#allmiss = 0
#Equity
#eq1 = allmiss*(startbet+bet1+bet2)


hand += deck.deal(1) #damo karto na mizo oziroma, v roko, da potem lažje primerjamo
if(hand[4].value==wilder):
    numwild = numwild+1
    
print ("na mizi imamo: ")
print (hand[4])
hand.sort()
payout=0
quad=0
FOAK = 0
find = 0 #za breakat iz zanke
wildpool = []
roka = [0, 1, 2, 3, 4]
for l in range(5):
    if(hand[l].value==wilder):
        wildpool.append(l)

if(numwild == 3):
    for z in range(len(strranks)-4):
            if (0, 1, 2) in wildpool:
                if((hand[3].value==strranks[z+3])&(hand[4].value==strranks[z+4])):
                     if(hand[3].suit==hand[4].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                            
            if (0, 1, 3) in wildpool:
                if((hand[2].value==strranks[z+2])&(hand[4].value==strranks[z+4])):
                     if(hand[2].suit==hand[4].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break

            if (0, 1, 4) in wildpool:
                if((hand[3].value==strranks[z+3])&(hand[2].value==strranks[z+2])):
                     if(hand[3].suit==hand[2].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break

            if (0, 2, 3) in wildpool:
                if((hand[1].value==strranks[z+1])&(hand[4].value==strranks[z+4])):
                     if(hand[1].suit==hand[4].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break

            if (0, 2, 4) in wildpool:
                if((hand[1].value==strranks[z+1])&(hand[3].value==strranks[z+3])):
                     if(hand[1].suit==hand[3].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break

            if (0, 3, 4) in wildpool:
                if((hand[2].value==strranks[z+2])&(hand[1].value==strranks[z+1])):
                     if(hand[2].suit==hand[1].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break

            if (1, 2, 3) in wildpool:
                if((hand[0].value==strranks[z])&(hand[4].value==strranks[z+4])):
                     if(hand[0].suit==hand[4].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break


            if (1, 2, 4) in wildpool:
                if((hand[0].value==strranks[z])&(hand[3].value==strranks[z+3])):
                     if(hand[0].suit==hand[3].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break

            if (2, 3, 4) in wildpool:
                if((hand[0].value==strranks[z])&(hand[1].value==strranks[z+1])):
                     if(hand[0].suit==hand[1].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break

            if (1, 3, 4) in wildpool:
                if((hand[0].value==strranks[z])&(hand[2].value==strranks[z+2])):
                     if(hand[0].suit==hand[2].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                else:
                    payout=50 #dobil smo samo triple wild
                    find = 1
                    break
else:
    if(numwild == 2):
        for z in range(len(strranks)-4):
             if (0, 1) in wildpool:
                if((hand[2].value==strranks[z+2])&(hand[3].value==strranks[z+3])&(hand[4].value==strranks[z+4])):
                     if(hand[3].suit==hand[4].suit==hand[2].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                        else:
                            payout=40 #imamo straight flush
                            find = 1
                            break
                     else:
                        payout=4 #imamo straight
                        find = 1
                        break
             if (0, 2) in wildpool:
                if((hand[3].value==strranks[z+3])&(hand[1].value==strranks[z+1])&(hand[4].value==strranks[z+4])):
                     if(hand[3].suit==hand[1].suit==hand[4].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                        else:
                            payout=40 #imamo straight flush
                            find = 1
                            break
                     else:
                        payout=4 #imamo straight
                        find = 1
                        break
             if (0, 3) in wildpool:
                if((hand[4].value==strranks[z+4])&(hand[2].value==strranks[z+2])&(hand[1].value==strranks[z+1])):
                     if(hand[1].suit==hand[4].suit==hand[2].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                        else:
                            payout=40 #imamo straight flush
                            find = 1
                            break
                     else:
                        payout=4 #imamo straight
                        find = 1
                        break
             if (0, 4) in wildpool:
                if((hand[1].value==strranks[z+1])&(hand[3].value==strranks[z+3])&(hand[2].value==strranks[z+2])):
                     if(hand[1].suit==hand[3].suit==hand[2].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                        else:
                            payout=40 #imamo straight flush
                            find = 1
                            break
                     else:
                        payout=4 #imamo straight
                        find = 1
                        break
             if (1, 2) in wildpool:
                if((hand[0].value==strranks[z])&(hand[3].value==strranks[z+3])&(hand[4].value==strranks[z+4])):
                     if(hand[0].suit==hand[1].suit==hand[3].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                        else:
                            payout=40 #imamo straight flush
                            find = 1
                            break
                     else:
                        payout=4 #imamo straight
                        find = 1
                        break
             if (1, 3) in wildpool:
                if((hand[0].value==strranks[z])&(hand[2].value==strranks[z+2])&(hand[4].value==strranks[z+4])):
                     if(hand[0].suit==hand[2].suit==hand[4].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                        else:
                            payout=40 #imamo straight flush
                            find = 1
                            break
                     else:
                        payout=4 #imamo straight
                        find = 1
                        break
             if (1, 4) in wildpool:
                if((hand[0].value==strranks[z])&(hand[3].value==strranks[z+3])&(hand[2].value==strranks[z+2])):
                     if(hand[0].suit==hand[4].suit==hand[2].suit):
                        if(z==10):
                            payout=200 #imamo wild royal
                            find = 1
                            break
                        else:
                            payout=40 #imamo straight flush
                            find = 1
                            break
                     else:
                        payout=4 #imamo straight
                        find = 1
                        break
             if (2, 3) in wildpool:
                if((hand[0].value==strranks[z])&(hand[1].value==strranks[z+1])&(hand[4].value==strranks[z+4])):
                     if(hand[0].suit==hand[1].suit==hand[4].suit):
                             if(z==10):
                                payout=200 #imamo wild royal
                                find = 1
                                break
                             else:
                                payout=40 #imamo straight flush
                                find = 1
                                break
                     else:
                        payout=4 #imamo straight
                        find = 1
                        break
             if (2, 4) in wildpool:
                if((hand[0].value==strranks[z])&(hand[1].value==strranks[z+1]&(hand[3].value==strranks[z+3]))):
                     if(hand[0].suit==hand[1].suit==hand[3].suit):
                                if(z==10):
                                    payout=200 #imamo wild royal
                                    find = 1
                                    break
                                else:
                                    payout=40 #imamo straight flush
                                    find = 1
                                    break
                     else:
                                payout=4 #imamo straight
                                find = 1
                                break
             if (3, 4) in wildpool:
                if((hand[0].value==strranks[z])&(hand[1].value==strranks[z+1])&(hand[2].value==strranks[z+2])):
                     if(hand[0].suit==hand[1].suit==hand[2].suit):
                                if(z==10):
                                    payout=200 #imamo wild royal
                                    find = 1
                                    break
                                else:
                                    payout=40 #imamo straight flush
                                    find = 1
                                    break
                     else:
                                payout=4 #imamo straight
                                find = 1
                                break
        if(payout < 75):
            for m in range(len(hand)-1):
                novaroka = roka
                novaroka.remove(m);
                if(hand[novaroka[m]].value==hand[novaroka[m+1]].value):
                    quad=quad+1
            if quad == 4:
                payout=75 #dobimo 5 of a kind
    else:
        if(numwild ==1):
            for z in range(len(strranks)-4):
                if (0) in wildpool:
                    if((hand[1].value==strranks[z+1])&(hand[2].value==strranks[z+2])&(hand[3].value==strranks[z+3])&(hand[4].value==strranks[z+4])):
                         if(hand[1].suit==hand[2].suit==hand[3].suit==hand[4].suit):
                                if(z==10):
                                    payout=200 #imamo wild royal
                                    find = 1
                                    break
                                else:
                                    payout=40 #imamo straight flush
                                    find = 1
                                    break
                         else:
                                payout=4 #imamo straight
                                find = 1
                                break
                if (1) in wildpool:
                    if((hand[0].value==strranks[z])&(hand[2].value==strranks[z+2])&(hand[3].value==strranks[z+3])&(hand[4].value==strranks[z+4])):
                             if(hand[0].suit==hand[2].suit==hand[3].suit==hand[4].suit):
                                if(z==10):
                                    payout=200 #imamo wild royal
                                    find = 1
                                    break
                                else:
                                    payout=40 #imamo straight flush
                                    find = 1
                                    break
                             else:
                                payout=4 #imamo straight
                                find = 1
                                break
                if (2) in wildpool:
                    if((hand[0].value==strranks[z])&(hand[1].value==strranks[z+1])&(hand[3].value==strranks[z+3])&(hand[4].value==strranks[z+4])):
                             if(hand[0].suit==hand[1].suit==hand[3].suit==hand[4].suit):
                                if(z==10):
                                    payout=200 #imamo wild royal
                                    find = 1
                                    break
                                else:
                                    payout=40 #imamo straight flush
                                    find = 1
                                    break
                             else:
                                payout=4 #imamo straight
                                find = 1
                                break
                if (3) in wildpool:
                    if((hand[0].value==strranks[z])&(hand[1].value==strranks[z+1])&(hand[2].value==strranks[z+2])&(hand[4].value==strranks[z+4])):
                             if(hand[0].suit==hand[1].suit==hand[2].suit==hand[4].suit):
                                if(z==10):
                                    payout=200 #imamo wild royal
                                    find = 1
                                    break
                                else:
                                    payout=40 #imamo straight flush
                                    find = 1
                                    break
                             else:
                                payout=4 #imamo straight
                                find = 1
                                break
                if (4) in wildpool:
                    if((hand[0].value==strranks[z])&(hand[2].value==strranks[z+2])&(hand[3].value==strranks[z+3])&(hand[1].value==strranks[z+1])):
                             if(hand[0].suit==hand[2].suit==hand[3].suit==hand[1].suit):
                                if(z==10):
                                    payout=200 #imamo wild royal
                                    find = 1
                                    break
                                else:
                                    payout=40 #imamo straight flush
                                    find = 1
                                    break
                             else:
                                payout=4 #imamo straight
                                find = 1
                                break
                                
                                
                if((hand[0].value==hand[1].value==hand[2].value==hand[3].value) | (hand[4].value==hand[1].value==hand[2].value==hand[3].value) | (hand[0].value==hand[4].value==hand[2].value==hand[3].value) | (hand[0].value==hand[1].value==hand[4].value==hand[3].value) | (hand[0].value==hand[1].value==hand[2].value==hand[4].value)):
                    if(payout < 75):
                        payout=75
                if(payout < 10):
                    for m in range(len(hand)-1):
                        for n in range(len(hand)):
                            if((hand[m].value==hand[m+1].value==hand[n].value) & ( n != m) & (n != m+1)):
                                payout=10 #four of a kind
                            else:
                                if(hand[0].value==hand[2].value==hand[4].value):
                                    payout=10 #four of a kind
                                    find = 1
                                    break
                        if find == 1:
                            break
        else:
            #preverimo dobitek brez wildov
                    for z in range(len(strranks)-4):
                        if ((hand[0].value==strranks[z])&(hand[1].value==strranks[z+1])&(hand[2].value==strranks[z+2])&(hand[3].value==strranks[z+3])&(hand[4].value==strranks[z+4])):
                            payout=4 #Imamo straight
                            if((hand[0].suit==hand[1].suit)&(hand[2].suit==hand[3].suit)&(hand[4].suit==hand[2].suit)&(hand[1].suit==hand[2].suit)):
                                payout=40 #imamo tudi straight flush
                                if(z==10):
                                    payout=1000#imamo royal flush
                            find = 1
                            break
                        if find == 1:
                            break
                    if(payout < 10):
                        for q in range(len(hand)-1):
                            if(hand[q].value==hand[q+1].value):
                                FOAK = FOAK+1
                            else:
                                break
                        if(FOAK==4):
                            payout=10
                            find = 1
                            
                    if(payout < 5):
                        if((hand[0].value==hand[1].value==hand[2].value) & (hand[3].value==hand[4].value) | (hand[2].value==hand[3].value==hand[4].value) & (hand[0].value==hand[1].value)):
                            payout=5
                            find = 1
                            
                    if(payout < 4):
                        if((hand[0].suit==hand[1].suit)&(hand[2].suit==hand[3].suit)&(hand[4].suit==hand[2].suit)&(hand[1].suit==hand[2].suit)):
                            payout = 4
                            find= 1
                    if(payout < 1):
                        for t in range(len(hand)-2):
                            if(hand[t].value==hand[t+1].value==hand[t+2].value):
                                payout = 1
                                find = 1
                                break
                    if(payout < 1):
                        if(((hand[0].value==hand[1].value) & (hand[2].value==hand[3].value)) | ((hand[3].value==hand[4]) & (hand[0].value==hand[1].value)) | ((hand[1].value==hand[2].value) & (hand[3].value == hand[4].value))):
                            payout = 1
                            find = 1
                    if(payout < 1):
                        for x in range (5):
                            for y in range(5):
                                if((hand[x].value == hand[y].value) & (x != y)):
                                    payout = 1
                                    find = 1
                                    break

                    
Dobitek = (startbet+bet1+bet2+bet3)*payout+thit*tricard+(startbet+bet1+bet2+bet3)*find
print("Dobitek je:")
print(Dobitek)
