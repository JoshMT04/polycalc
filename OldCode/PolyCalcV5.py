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

stats = {'Health': pd.Series([10, 10, 15, 10, 5, 10, 10, 15, 10, 10, 40, 'Varies',
                              'Varies','Varies','Varies', 40, 5, 10],
                             index=['Warrior', 'Archer', 'Defender',
                                    'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                    'Swordsman', 'Catapult', 'Knight',
                                    'Giant', 'Raft', 'Scout', 'Rammer', 
                                    'Bomber', 'Juggernaut', 'Dinghy', 'Pirate']),
         'Attack': pd.Series([2, 2, 1, 2, 0, 2, 0, 3, 4, 3.5, 5, 0, 2, 3, 3, 
                              4, 0, 2],
                             index=['Warrior', 'Archer', 'Defender',
                                    'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                    'Swordsman', 'Catapult', 'Knight',
                                    'Giant', 'Raft', 'Scout', 'Rammer', 
                                    'Bomber', 'Juggernaut', 'Dinghy', 'Pirate']),
         'Defense': pd.Series([2, 1, 3, 1, 0.5, 2, 1, 3, 0, 1, 4, 1, 2, 3, 2, 
                               4, 0.5, 2],
                               index = ['Warrior', 'Archer', 'Defender',
                                      'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                      'Swordsman', 'Catapult', 'Knight',
                                      'Giant', 'Raft', 'Scout', 'Rammer', 
                                      'Bomber', 'Juggernaut', 'Dinghy', 'Pirate']),
         'Cost': pd.Series([2, 3, 3, 3, 8, 1, 5, 5, 8, 8, 20, 'Varies', 'Varies',
                            'Varies', 'Varies', 20, 8, 1],
                           index = ['Warrior', 'Archer', 'Defender',
                                  'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                  'Swordsman', 'Catapult', 'Knight',
                                  'Giant', 'Raft', 'Scout', 'Rammer', 
                                  'Bomber', 'Juggernaut', 'Dinghy', 'Pirate']),
         'Range': pd.Series([1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 0, 2, 1, 3, 1, 1, 1],
                            index = ['Warrior', 'Archer', 'Defender',
                                   'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                   'Swordsman', 'Catapult', 'Knight',
                                   'Giant', 'Raft', 'Scout', 'Rammer', 
                                   'Bomber', 'Juggernaut', 'Dinghy', 'Pirate']),
         'Retaliate': pd.Series([True, True, True, True, False, True, False, True,
                                 False, True, True, False, True, True, False, 
                                 False, False, True],
                                index = ['Warrior', 'Archer', 'Defender',
                                       'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                       'Swordsman', 'Catapult', 'Knight',
                                       'Giant', 'Raft', 'Scout', 'Rammer', 
                                       'Bomber', 'Juggernaut', 'Dinghy', 'Pirate']),
         'Terrain': pd.Series(['Land', 'Land', 'Land', 'Land', 'Land', 'Land', 'Land',
                               'Land', 'Land', 'Land', 'Land', 'Water', 'Water',
                               'Water','Water','Water','Water','Water'],
                              index = ['Warrior', 'Archer', 'Defender',
                                     'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                     'Swordsman', 'Catapult', 'Knight',
                                     'Giant', 'Raft', 'Scout', 'Rammer', 
                                     'Bomber', 'Juggernaut', 'Dinghy', 'Pirate']),
          'Skills': pd.Series([['Dash', 'Fortify'], ['Dash', 'Fortify'], ['Fortify'], ['Dash', 'Escape', 'Fortify'], 
                                 ['Hide', 'Sneak', 'Infiltrate', 'Dash'], ['Dash', 'Surprise', 'Independent'], 
                                 ['Heal', 'Convert', 'Detect'], ['Dash', 'Fortify'], ['None'], 
                                 ['Dash', 'Persist', 'Fortify'], ['None'], ['Carry', 'Float'],
                                 ['Dash', 'Carry', 'Float', 'Scout'], ['Dash', 'Carry', 'Float'],
                                 ['Carry', 'Float', 'Splash', 'Stiff'], ['Carry', 'Float', 'Stiff', 'Stomp'],
                                 ['Carry', 'Float', 'Hide', 'Sneak', 'Infiltrate'], ['Dash', 'Surprise', 'Independent']],
                                index = ['Warrior', 'Archer', 'Defender',
                                       'Rider','Cloak', 'Dagger', 'Mind Bender', 
                                       'Swordsman', 'Catapult', 'Knight',
                                       'Giant', 'Raft', 'Scout', 'Rammer', 
                                       'Bomber', 'Juggernaut', 'Dinghy', 'Pirate'])
          }

units_df = pd.DataFrame(stats)

attackers = input("What are the attacking units?(Seperate list with ', '; capitalisation does not matter)\n")
attackers_health = input("what is the health of each unit?(Seperate list with ', ')\n")
defender = input("What is the defending troop? \n")
defender_health = input("How much health does the defender have? \n")

defender_list = []
defender_list.append(defender.capitalize())
defender = defender_list[0]

attackers_list = attackers.split(', ')
attackers_list_new = []
for unit in attackers_list:
    attackers_list_new.append(unit.capitalize())
attackers_list = attackers_list_new
attackers_health_list = attackers_health.split(', ')

attackerStatLists = [list(x) for x in zip(attackers_list, attackers_health_list)]

attackers_df = pd.DataFrame([attackers_list, attackers_health_list])
attackers_df_new = attackers_df.transpose()
attackers_df_new.columns = ['Unit', 'Health']
attackers_df_new.set_index('Unit', inplace = True)

units_in_units = []
units_in_units_health = []
units_in_units_cost = []

for unit in attackers_list:
    if units_df.loc[unit, 'Health'] == 'Varies':
        boat_unit = input(f'Which unit was used to make your {unit}?\n')
        boat_unit = boat_unit.capitalize()
        units_in_units.append(boat_unit)
        boat_unit_health = units_df.loc[boat_unit, 'Health']
        units_in_units_health.append(boat_unit_health)
    else:
        units_in_units.append(unit.capitalize())
        units_in_units_health.append(units_df.loc[unit, 'Health'])
    if unit == 'Bomber':
        units_in_units_cost.append(units_df.loc[boat_unit, 'Cost'] + 15)
    elif unit == 'Scout' or unit == 'Rammer':
        units_in_units_cost.append(units_df.loc[boat_unit, 'Cost'] + 5)
    elif unit == 'Raft':
        units_in_units_cost.append(units_df.loc[boat_unit, 'Cost'])
    else:
        units_in_units_cost.append(units_df.loc[unit, 'Cost'])

attackers_df_new = attackers_df_new.assign(unit_in_unit = units_in_units)
attackers_df_new = attackers_df_new.assign(unit_in_unit_health = units_in_units_health)
attackers_df_new = attackers_df_new.assign(unit_in_unit_cost = units_in_units_cost)

if units_df.loc[defender, 'Health'] == 'Varies':
    boat_unit = input(f'Which unit was used to make the defending {defender}?\n')
    boat_unit = boat_unit.capitalize()
    boat_unit_health = units_df.loc[boat_unit, 'Health']
    units_df.loc[defender, 'Health'] = boat_unit_health
    if defender == 'Bomber':
        boat_unit_cost = units_df.loc[boat_unit, 'Cost'] + 15
    if defender == 'Scout' or defender == 'Rammer':
        boat_unit_cost = units_df.loc[boat_unit, 'Cost'] + 5
    if defender == 'Raft':
        boat_unit_cost = units_df.loc[boat_unit, 'Cost']
    units_df.loc[defender, 'Health'] = boat_unit_cost

defenseBonus = 1.0

dbonus = input('Does the defender have a defence bonus?(T/F)\n')
if dbonus == 'T':
    defenseBonus = 1.5
if dbonus == 'T' and units_df.loc[defender, 'Skills'].str.contains('Fortify'):
    citywall = input('Is the defender on a walled city?(T/F)\n')
    if citywall == 'T':
        dbonus = 4.0
    
starValueScores = list()

Knight_chain = bool()

jug_bomb_splash = bool()
num_splash = int()
splash_list = []

for unit in attackers_list:
    if unit == 'Bomber' or unit == 'Juggernaut':
        splash_qs = input(f'Can your {unit} splash other units?(T/F) \n')
        if splash_qs == 'T':
            jug_bomb_splash = True
            num_splash_qs = input('How many units will be splashed? (1-9)\n')
        else:
            jug_bomb_splash = False
    else:
        jug_bomb_splash = False
    splash_list.append(jug_bomb_splash)
    
Knight_chain = bool()
Knight_chain_list = []

for unit in attackers_list:
    if unit == 'Knight':
        knight_chain_qs = input('Can you chain knight attacks?(T/F)\n')
        if knight_chain_qs == 'T':
            Knight_chain = True
        else:
            Knight_chain = False
    else:
        Knight_chain = False
    Knight_chain_list.append(Knight_chain)

safe_dist = bool()
safe_dist_list = []

for unit in attackers_list:
    if units_df.loc[unit, 'Range'] <= 1:
        safe_dist = False
    elif units_df.loc[unit, 'Range'] > 1 and units_df.loc[unit, 'Range'] <= units_df.loc[defender, 'Range'] and units_df.loc[defender, 'Retaliate'] == True:
        safe_dist_qs = input(f'Is your {unit} as safe distance from the defender?(T/F)\n')
        if safe_dist_qs == 'T':
            safe_dist = True
        else:
            safe_dist = False
    elif units_df.loc[unit, 'Range'] > units_df.loc[defender, 'Range'] and units_df.loc[defender, 'Retaliate'] == True:
        safe_dist_qs = input(f'Is your {unit} as safe distance from the defender?(T/F)\n')
        if safe_dist_qs == 'T':
            safe_dist = True
        else:
            safe_dist = False 
    safe_dist_list.append(safe_dist)

attackers_df_new = attackers_df_new.assign(safe_dist = safe_dist_list)
attackers_df_new = attackers_df_new.assign(knight_chain = Knight_chain_list)
attackers_df_new = attackers_df_new.assign(splash_damage = splash_list)

def starValue(attackDamage, defenderHealth, attacker, retaliationDamage, attackerHealth, defenderCost, attackerCost, multiplier):
    attackValue = int(attackDamage) / int(defenderHealth)
    retaliationCost = int(retaliationDamage) / int(attackerHealth) 
    if retaliationCost == 0:
        retaliationCost = 0.00000000000000000000001
    starValueScore = ((attackValue * defenderCost) / (retaliationCost * attackerCost)) * multiplier
    starValueScores.append(starValueScore)

defender_health_int = list()
defender_health_record = list()
after_attacker_health_list = list()

def PolyDamageCalc(attacker, attacker_health, defender, defender_health):
    attackForce = float(units_df.loc[attacker, 'Attack']) * (float(attacker_health) / float(attackers_df_new.loc[attacker, 'unit_in_unit_health']))
    defenseForce = float(units_df.loc[defender, 'Defense']) * (float(defender_health) / float(units_df.loc[defender, 'Health'])) * defenseBonus
    totalDamage = attackForce + defenseForce
    attackResult = (attackForce / totalDamage) * float(units_df.loc[attacker, 'Attack']) * 4.5
    defenseResult = (defenseForce / totalDamage) * float(units_df.loc[defender, 'Defense']) * 4.5

    if attackers_df_new.loc[attacker, 'safe_dist'] == True or units_df.loc[defender, 'Retaliate'] == False:
        defenseResult = 0
        
    round_attackResult = proper_round(attackResult)
    round_defenseResult = proper_round(defenseResult)
    if int(round_attackResult) > int(defender_health):
        round_attackResult = defender_health

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
    attackForce = float(units_df.loc[attacker, 'Attack']) * (float(attacker_health) / float(attackers_df_new.loc[attacker, 'unit_in_unit_health']))
    defenseForce = float(units_df.loc[defender, 'Defense']) * (float(defender_health) / float(units_df.loc[defender, 'Health'])) * defenseBonus
    totalDamage = attackForce + defenseForce
    attackResult = (attackForce / totalDamage) * float(units_df.loc[attacker, 'Attack']) * 4.5
    defenseResult = (defenseForce / totalDamage) * float(units_df.loc[defender, 'Defense']) * 4.5

    if attackers_df_new.loc[attacker, 'safe_dist'] == True or units_df.loc[defender, 'Retaliate'] == False:
        defenseResult = 0
    
    round_attackResult = proper_round(attackResult)
    round_defenseResult = proper_round(defenseResult)
    if int(round_attackResult) > int(defender_health):
        round_attackResult = defender_health
    
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
    if attackers_df_new.loc[attacker, 'knight_chain'] == True and end_defenderHealth == 0:
        multiplier = 2
    if attackers_df_new.loc[attacker, 'splash_damage'] == True:
        multiplier = 1 + (num_splash * 0.1)
    
    starValue(round_attackResult, defender_health, attacker, round_defenseResult,
              attacker_health, units_df.loc[defender, 'Cost'],
              attackers_df_new.loc[attacker, 'unit_in_unit_cost'], multiplier)



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
                
            elif i[2] == bestAttack:
                if units_df.loc[i[0], 'Cost'] < units_df.loc[bestAttackerUnit, 'Cost']:
                    bestAttackerUnit = i[0]
                    bestAttackerHealth = i[1]
                    bestAttack = i[2]
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

# Distinguish between the same unit





