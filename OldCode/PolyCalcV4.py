#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 20:04:38 2024

@author: joshmassey-thompson
"""

import pandas as pd
import math

def proper_round(Result):
    if Result - math.floor(Result) < 0.5:
        return math.floor(Result)
    else:
        return math.ceil(Result)

stats = {'Health': pd.Series([10, 10, 15, 10, 5, 10, 10, 15, 10, 10, 40],
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
                                  'Knight', 'Giant']),
         'Range': pd.Series([1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1],
                            index = ['Warrior', 'Archer', 'Defender',
                                   'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                   'Swordsman', 'Catapult', 
                                   'Knight', 'Giant'])
         # 'Skills': pd.Series.to_string(['Dash, Fortify', 'Dash, Fortify', 'Fortify', 'Dash, Escape, Fortify', 
         #                      'Hide, Sneak, Infiltrate, Dash', 'Dash, Surprise, Independent', 
         #                      'Heal, Convert, Detect', 'Dash, Fortify', 'None', 
         #                      'Dash, Persist, Fortify', 'None'],
         #                     index = ['Warrior', 'Archer', 'Defender',
         #                            'Rider','Cloak', 'Dagger', 'Mind Bender', 
         #                            'Swordsman', 'Catapult', 
         #                            'Knight', 'Giant'])
         }

units_df = pd.DataFrame(stats)

attackers = 'Warrior, Giant, Warrior' # input("What are the attacking troops? ")
attackers_health = '10, 40, 5' # input("what is the health of each troop? ")
defender = 'Warrior' # input("What is the defending troop? ")
defender_health = '5' # input("How much health does the defender have? ")

attackers_list = attackers.split(', ')
attackers_health_list = attackers_health.split(', ')

attackerStatLists = [list(x) for x in zip(attackers_list, attackers_health_list)]

attackers_df = pd.DataFrame([attackers_list, attackers_health_list])
attackers_df_new = attackers_df.transpose()
attackers_df_new.columns = ['Unit', 'Health']
attackers_df_new.set_index('Unit', inplace = True)

defenseBonus = 1.0

# if defender != 'Giant' or :
#     dbonus = input(f'Does the defender have a defence bonus? (T/F) \n')
#     if dbonus == 'T' and defender != 'Giant' and defender != 'Catapult':
#         defenseBonus = 1.5
#         citywall = input('Is the defender on a walled city? (T/F) \n')
#         if citywall == 'T':
#             defenseBonus = 4.0
#     if dbonus == 'F':
#         defenseBonus = 1.0
starValueScores = list()

Knight_chain = bool()

if 'Knight' in attackers_list:
    knight_chain_qs = input('Can you chain knight attacks? (T/F)\n')
    if knight_chain_qs == 'T':
        Knight_chain = True

safe_cata = bool()

if 'Catapult' in attackers_list:
    safe_cata_qs = input('Is your catapult out of range of retaliation? (T/F)\n')
    if safe_cata_qs == 'T':
        safe_cata = True
    
safe_arch = bool()

if 'Archer' in attackers_list:
    safe_arch_qs = input('Is your archer out of range of retaliation? (T/F)\n')
    if safe_arch_qs == 'T':
        safe_arch = True
    
def starValue(attackDamage, defenderHealth, attacker, retaliationDamage, attackerHealth, defenderCost, attackerCost, multiplier):
    attackValue = int(attackDamage) / int(defenderHealth)
    attackValue * multiplier
    retaliationCost = int(retaliationDamage) / int(attackerHealth) # Favours higher health units too much
    print(f"Retaliation cost for {attacker} is {retaliationCost} and damage is {retaliationDamage}")
    if retaliationCost == 0:
        retaliationCost = 0.00000000000000000000001
    starValueScore = (attackValue * defenderCost) / (retaliationCost * attackerCost)
    starValueScores.append(starValueScore)

defender_health_int = list()
defender_health_record = list()
after_attacker_health_list = list()

def PolyDamageCalc(attacker, attacker_health, defender, defender_health):
    
    attackForce = float(units_df.loc[attacker, 'Attack']) * (float(attacker_health) / float(units_df.loc[attacker, 'Health']))
    defenseForce = float(units_df.loc[defender, 'Defense']) * (float(defender_health) / float(units_df.loc[defender, 'Health'])) * defenseBonus
    totalDamage = attackForce + defenseForce
    attackResult = (attackForce / totalDamage) * float(units_df.loc[attacker, 'Attack']) * 4.5
    defenseResult = (defenseForce / totalDamage) * float(units_df.loc[defender, 'Defense']) * 4.5
    
    round_attackResult = proper_round(attackResult)
    round_defenseResult = proper_round(defenseResult)
    if int(round_attackResult) > int(defender_health):
        round_attackResult = defender_health
    
    if attacker == 'Dagger':
        defenseResult = 0
        round_defenseResult = 0
    
    if attacker == 'Catapult' and safe_cata == True:
        defenseResult = 0
        round_defenseResult = 0
    
    if attacker == 'Archer' and safe_arch == True:
        defenseResult = 0
        round_defenseResult = 0

    if defender == 'Catapult':
        defenseResult = 0
        round_defenseResult = 0
    
    end_defenderHealth = int(defender_health) - int(round_attackResult)
    if end_defenderHealth < 0:
        end_defenderHealth = 0
    defender_health_int.append(end_defenderHealth)
    defender_health_record.append(end_defenderHealth)
    
    if end_defenderHealth > 0:
        end_attackerHealth = int(attacker_health) - int(round_defenseResult)
        if end_attackerHealth < 0:
            end_attackerHealth = 0
    elif end_defenderHealth <= 0:
        end_attackerHealth = attacker_health
        round_defenseResult = 0
    after_attacker_health_list.append(end_attackerHealth)

def PolyAttackScore(attacker, attacker_health, defender, defender_health):
    
    attackForce = float(units_df.loc[attacker, 'Attack']) * (float(attacker_health) / float(units_df.loc[attacker, 'Health']))
    defenseForce = float(units_df.loc[defender, 'Defense']) * (float(defender_health) / float(units_df.loc[defender, 'Health'])) * defenseBonus
    totalDamage = attackForce + defenseForce
    attackResult = (attackForce / totalDamage) * float(units_df.loc[attacker, 'Attack']) * 4.5
    defenseResult = (defenseForce / totalDamage) * float(units_df.loc[defender, 'Defense']) * 4.5
    
    round_attackResult = proper_round(attackResult)
    round_defenseResult = proper_round(defenseResult)
    if int(round_attackResult) > int(defender_health):
        round_attackResult = defender_health
    
    if attacker == 'Catapult' or attacker == 'Archer' or attacker == 'Dagger':
        defenseResult = 0
        round_defenseResult = 0
    
    end_defenderHealth = int(defender_health) - int(round_attackResult)
    if end_defenderHealth < 0:
        end_defenderHealth = 0
    
    if end_defenderHealth > 0:
        end_attackerHealth = int(attacker_health) - int(round_defenseResult)
        if end_attackerHealth < 0:
            end_attackerHealth = 0
    elif end_defenderHealth <= 0:
        end_attackerHealth = attacker_health
        round_defenseResult = 0
    
    multiplier = 1
    if end_defenderHealth == 0 and attacker == 'Knight' and Knight_chain == True:
        multiplier = 2
    
    starValue(round_attackResult, defender_health, attacker, round_defenseResult,
              attacker_health, units_df.loc[defender, 'Cost'],
              units_df.loc[defender, 'Cost'], multiplier)



for i in attackerStatLists:
    PolyAttackScore(i[0], i[1], defender, defender_health)
attackerStatListsNew = [list(x) for x in zip(attackers_list, attackers_health_list, starValueScores)]

attack_order_list = list()
attackers_log = list()
   
def AttackOrderCalc(attackers_list, attackerStatListsNew):
    bestAttack = int()
    bestAttackerUnit = str()
    n = 0
    bestAttacker_health = int()
    while n < 1:
        n += 1
        for i in attackerStatListsNew:
            if i[2] > bestAttack:
                bestAttack = i[2]
                bestAttackerUnit = i[0]
                bestAttacker_health = i[1]
                print(bestAttackerUnit, bestAttack)
        attack_order_list.append(bestAttackerUnit)
    
    PolyDamageCalc(bestAttackerUnit, bestAttacker_health, defender, defender_health)
    
    for i in attackerStatListsNew:
        if i[0] == bestAttackerUnit:
            attackers_log.append([i])
            attackerStatListsNew.remove(i)


def SecondaryAttackCalc(attackerStatListsNew):
    bestAttack = 0
    bestAttackerUnit = str()
    bestAttacker_health = int()
    for i in attackerStatListsNew:
        if i[2] > bestAttack:
            bestAttack = i[2]
            bestAttackerUnit = i[0]
            bestAttacker_health = i[1]
            print(bestAttackerUnit, bestAttacker_health)
            
    attack_order_list.append(bestAttackerUnit)
    
    PolyDamageCalc(bestAttackerUnit, bestAttacker_health, defender, defender_health_int[0])
    for i in attackerStatListsNew:
        if i[0] == bestAttackerUnit:
            attackers_log.append([i])
            attackerStatListsNew.remove(i)

AttackOrderCalc(attackers_list, attackerStatListsNew)

while len(attack_order_list) < len(attackers_list):
    health_remove = defender_health_int[0]
    if defender_health_int[0] <= 0:
        break
    SecondaryAttackCalc(attackerStatListsNew)
    defender_health_int.remove(health_remove)
    
x=0

for i in attack_order_list:
    print(f"For attack {x+1} you should use the {i}; the {defender}" 
          f" will be left with {defender_health_record[x]} health and"
          f" your {i} will have {after_attacker_health_list[x]} health")
    x += 1

# Add water units - account for splash damage using a multiplier, ask for the defender inside to calculate fraction of damage dealt, no retaliation for bomber or raft
# Distinguish between the same unit
# No retaliation from juggernaught or battleships






