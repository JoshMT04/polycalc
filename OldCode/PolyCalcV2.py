#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:48:52 2024

@author: joshmassey-thompson
"""

import pandas as pd
import math

def proper_round(Result):
    if Result - math.floor(Result) < 0.5:
        return math.floor(Result)
    else:
        return math.ceil(Result)

stats = {'Health': pd.Series([10, 10, 15, 10, 5, 10, 10,15,10,10,40],
                             index=['Warrior', 'Archer', 'Defender',
                                    'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                    'Swordsman', 'Catapult', 'Knight',
                                    'Giant']),
         'Attack': pd.Series([2, 2, 1,2,0,2,0,3,4,3.5,5],
                             index=['Warrior', 'Archer', 'Defender',
                                    'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                    'Swordsman', 'Catapult', 'Knight', 
                                    'Giant']),
         'Defense': pd.Series([2, 1, 3,1,0.5,2,1,3,0,1,4],
                               index = ['Warrior', 'Archer', 'Defender',
                                      'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                      'Swordsman', 'Catapult', 
                                      'Knight', 'Giant']),
         'Cost': pd.Series([2, 3, 3, 3, 8, 1, 5, 5, 8, 8, 20],
                           index = ['Warrior', 'Archer', 'Defender',
                                  'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                  'Swordsman', 'Catapult', 
                                  'Knight', 'Giant'])
         }

units_df = pd.DataFrame(stats)

attackers = input("What are the attacking troops? ")
attackers_health = input("what is the health of each troop? ")
defender = input("What is the defending troop? ")
defender_health = input("How much health does the defender have? ")

attackers_list = attackers.split(', ')
attackers_health_list = attackers_health.split(', ')

attackerStatLists = [list(x) for x in zip(attackers_list, attackers_health_list)]

defenseBonus = 1.0

if defender != 'Giant':
    dbonus = input(f'Does the defender have a defence bonus? (T/F) \n')
    if dbonus == 'T':
        defenseBonus = 1.5
        citywall = input('Is the defender on a walled city? (T/F) \n')
        if citywall == 'T':
            defenseBonus = 4.0
    if dbonus == 'F':
        defenseBonus = 1.0
starValueScores = list()

def starValue(attackDamage, defenderHealth, retaliationDamage, attackerHealth, defenderCost, attackerCost):
    attackValue = int(attackDamage) / int(defenderHealth)
    retaliationCost = int(retaliationDamage) / int(attackerHealth)
    starValueScore = (attackValue * defenderCost) / (retaliationCost * attackerCost)
    starValueScores.append(starValueScore)


def PolyAttackScore(attacker, attacker_health, defender, defender_health):
    
    attackForce = float(units_df.loc[attacker, 'Attack']) * (float(attacker_health) / float(units_df.loc[attacker, 'Health']))
    defenseForce = float(units_df.loc[defender, 'Defense']) * (float(defender_health) / float(units_df.loc[defender, 'Health'])) * defenseBonus
    totalDamage = attackForce + defenseForce
    attackResult = (attackForce / totalDamage) * float(units_df.loc[attacker, 'Attack']) * 4.5
    defenseResult = (defenseForce / totalDamage) * float(units_df.loc[defender, 'Defense']) * 4.5
        
    round_attackResult = proper_round(attackResult)
    round_defenseResult = proper_round(defenseResult)
    
    end_defenderHealth = int(defender_health) - int(round_attackResult)
    if end_defenderHealth < 0:
        end_defenderHealth = 0
    
    if end_defenderHealth > 0:
        end_attackerHealth = int(attacker_health) - int(round_defenseResult)
        if end_attackerHealth < 0:
            end_attackerHealth = 0
    else:
        end_attackerHealth = attacker_health
        
    starValue(round_attackResult, defender_health, round_defenseResult,
              attacker_health, units_df.loc[defender, 'Cost'], units_df.loc[defender, 'Cost'])

bestAttack = 0
bestAttackerUnit = str()
n = 0

while n < (len(attackers_list)/2):
    n += 1
    for i in attackerStatLists:
        PolyAttackScore(i[0], i[1], defender, defender_health)
    attackerStatListsNew = [list(x) for x in zip(attackers_list, attackers_health_list, starValueScores)]
    
    for i in attackerStatListsNew:
        if i[2] > bestAttack:
            bestAttack = i[2]
            bestAttackerUnit = i[0]

print("The best unit to attack with is your", bestAttackerUnit)















