# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 01:50:05 2020

@author: canseco
"""
import random

def CreatePoker():
    poker = []
    for i in range(1, 5):
        for j in range(1, 14):
            poker.append(i*100+j)
            
    return poker

def DisplayCard(num):
    suits = ["♣", "♢", "♡", "♠"]
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit_id = int(num / 100) - 1
    num_id = num % 100 - 1
   
    return suits[suit_id] + numbers[num_id]

def ShuffleCards(card_list):
    random.shuffle(card_list)
    
def DisplayCards(card_list):
    for c in card_list:
        print(DisplayCard(c), end=', ')

def DealCards(card_list):
    hand = []
    if len(card_list) > 5:
        for i in range(5):
            hand.append(card_list.pop(0))
    return hand


#Second shuffle
def ShuffleCards2(card_list):
    
    half = int(len(card_list) / 2)
    LeftCards = card_list[:half]
    RightCards = card_list[half:]
    
    card_list = []
    
    while len(LeftCards) > 0 and len(RightCards) > 0:
        if len(LeftCards) > 5 and len(RightCards) > 5:
            card_list.append(LeftCards.pop(random.randint(1,5)))
            card_list.append(RightCards.pop(random.randint(1,5)))
        else:
            card_list.append(LeftCards.pop(0))
            card_list.append(RightCards.pop(0))

    
    return card_list
    

# 順子
def IsStraight(card_list):
    result = False
    num = []
    checknum = []


    if len(card_list) == 5:
        for x in range(len(card_list)):
            num.append(card_list[x] % 100)
        if 1 in num and 13 in num:
            num.pop(num.index(1))
            num.sort()
            checknum.append(num[0])
            for x in range(1,len(num)):
                checknum.append(checknum[x-1]+1)
            if checknum == num:
                result = True

        else:
            num.sort()
            checknum.append(num[0])
            for x in range(1,len(num)):
                checknum.append(checknum[x-1]+1)
            if checknum == num:
                result = True
    
    
    return result

# 同花
def IsFlush(card_list):
    result = False
    suits = []
    

    if len(card_list) == 5:
        for x in range(len(card_list)):
            suits.append(int(card_list[x] / 100))
        if suits.count(suits[0]) == len(suits):
            result = True

    return result


#full house
def IsFullHouse(card_list):
    result = False
    num = []
    
    if len(card_list) == 5:
        for x in range(len(card_list)):
            num.append(card_list[x] % 100)

        num_set = set(num)
        
        if num.count(list(num_set)[0]) == 3 and num.count(list(num_set)[1]) == 2:
            result = True
        elif num.count(list(num_set)[0]) == 2 and num.count(list(num_set)[1]) == 3:
            result = True

    return result

#Pair
def IsPair(card_list):
    result = 0
    num = []
    num_reuslt = []
    
    if len(card_list) == 5:
        for x in range(len(card_list)):
            num.append(card_list[x] % 100)
        
        num_set = set(num)
        
        for x in num_set:
            count = 0
            for y in num:
                if x == y:
                    count += 1
            num_reuslt.append(count)
            
        num_reuslt.sort()
                    
            
        if num_reuslt == [1,1,1,2]:
            result = 1
        elif num_reuslt == [1,1,3]:
            result = 2
        elif num_reuslt == [1,2,2]:
            result = 3
        elif num_reuslt == [1,4]:
            result = 4

        
    return result
        

#牌型
def checkCards(card_list):
    result = "nothing"
    
    if IsStraight(card_list) and IsFlush(card_list):
        result = "Straight Flush"
    elif IsStraight(card_list):
        result = "Straight"
    elif IsFlush(card_list):
        result = "Flush"
    elif IsFullHouse(card_list):
        result = "Full House"
    elif IsPair(card_list) == 1:
        result = "One Pairs"
    elif IsPair(card_list) == 2:
        result = "Three of a kind"
    elif IsPair(card_list) == 3:
        result = "Two Pairs"
    elif IsPair(card_list) == 4:
        result = "Four of a Kind"
        
    return result


# for more information - https://en.wikipedia.org/wiki/List_of_poker_hands
# you can do more ....

# main program begins here

userinput = int(input('Enter number of Player: '))

p_host = CreatePoker()
print("\nDealer....")       
DisplayCards(p_host)
        
print("\n\nafter shuffling....")
# ShuffleCards(p_host)
p_host = ShuffleCards2(p_host)
DisplayCards(p_host)
for x in range(userinput):
    print("\n\nplayer {0}....".format(x+1))
    x = DealCards(p_host)
    DisplayCards(x)
    print("\n")
    print(checkCards(x))
    
print("\n")
DisplayCards(p_host)

      
      
      
      
      

    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   

# def DisplayPoker(poker_list):  
#     for x in poker_list:
#         print(DisplayCard(x), end=' ')
#     print()
        
# def ShufflePoker(poker_list):
#     temp_list = poker_list
#     poker_list.reverse()
    
    
    
# myPoker = CreatePoker()
# DisplayPoker(myPoker)
# ShufflePoker(myPoker)
# print('After shffule')
# DisplayPoker(myPoker)
    
# print(CreatePoker())
# print(DisplayCard(401))