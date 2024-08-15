#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 13:58:00 2024

@author: joshmassey-thompson
"""

import pandas as pd
import math
import string as st

digits = list(st.digits)

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

attackers = 'warrior, warrior, warrior'  # input("What are the attacking units?(Seperate list with ', '; capitalisation does not matter)\n")
attackers_health = '15, 10, 10' # input("what is the health of each unit?(Seperate list with ', ')\n")
attackers_vet = 'T, F, F' # input("Is each attacking unit a veteran?")
defender = 'defender' # input("What is the defending unit? \n")
defender_health = '15' # input("How much health does the defender have? \n")
defender_vet = 'F' # input("Is each attacking unit a veteran?")

defender = defender.capitalize()
attackers_list = attackers.split(', ')
attackers_list_temp = []
for unit in attackers_list:
    attackers_list_temp.append(unit.capitalize())
attackers_list = attackers_list_temp
attackers_health_list = attackers_health.split(', ')
attackers_vet_list = attackers_vet.split(', ')

attackers_df = pd.DataFrame([attackers_list, attackers_health_list, attackers_vet_list]).transpose()
attackers_df.columns = ['Unit', 'Health', 'Veteran']

attackers_df_dups = attackers_df.duplicated('Unit')
attackers_df = attackers_df.assign(dup_unit = attackers_df_dups)

units_mem = []
for index, row in attackers_df.iterrows():
    units_mem.append(row['Unit'])
attackers_df = attackers_df.assign(dup_unit = attackers_df_dups, unit_mem = units_mem)
    
n = {}
for index, row in attackers_df.iterrows():
    if row['dup_unit']:
        unit = row['Unit']
        if unit in n:
            n[unit] += 1
        else:
            n[unit] = 1
        attackers_df.at[index, 'Unit'] = f"{unit}{n[unit]}"

attackers_df.set_index('Unit', inplace=True)

attackers_df['Veteran'] = attackers_df['Veteran'].apply(lambda x: True if x == 'T' else False)

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

attackers_df = attackers_df.assign(unit_in_unit=units_in_units, 
                                   unit_in_unit_health=units_in_units_health, 
                                   unit_in_unit_cost=units_in_units_cost)

defender_boat_unit = str()
defender_boat_unit_health = int()

if units_df.loc[defender, 'Health'] == 'Varies':
    defender_boat_unit = input(f'Which unit was used to make the defending {defender}?\n')
    defender_boat_unit = defender_boat_unit.capitalize()
    defender_boat_unit_health = units_df.loc[defender_boat_unit, 'Health']
    units_df.loc[defender, 'Health'] = boat_unit_health
    
if defender == 'Bomber':
    units_df.loc[defender, 'Cost'] = (int(units_df.loc[defender_boat_unit, 'Cost']) + 15)
if defender == 'Rammer' or defender == 'Scout':
    units_df.loc[defender, 'Cost'] = (int(units_df.loc[defender_boat_unit, 'Cost']) + 5)
if defender == 'Raft':
    units_df.loc[defender, 'Cost'] = int(units_df.loc[defender_boat_unit, 'Cost'])

defenseBonus = 1.0

dbonus = input('Does the defender have a defence bonus?(T/F)\n')
if dbonus == 'T':
    defenseBonus = 1.5
if dbonus == 'T' and 'Fortify' in units_df.loc[defender, 'Skills']:
    citywall = input('Is the defender on a walled city?(T/F)\n')
    if citywall == 'T':
        dbonus = 4.0

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

safe_dist = str()
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

attackers_df = attackers_df.assign(safe_dist = safe_dist_list,
                                   knight_chain = Knight_chain_list,
                                   splash_damage = splash_list)

starValueScores = []

def starValue(attackDamage, defenderHealth, attacker, retaliationDamage, attackerHealth, defenderCost, attackerCost, multiplier):
    attackValue = int(attackDamage) / int(defenderHealth)
    retaliationCost = int(retaliationDamage) / int(attackerHealth) 
    if retaliationCost == 0:
        retaliationCost = 0.00000000000000000000001
    starValueScore = ((attackValue * int(defenderCost)) / (retaliationCost * int(attackerCost))) * multiplier
    starValueScores.append(starValueScore)

defender_health_int = list()
defender_health_record = list()
after_attacker_health_list = list()

defender_health_mem = []
defender_health_mem.append(defender_health)
defender_health_rounds = []
defender_health_rounds.append(defender_health)
after_attack_health_list = []
def PolyDamageCalc(attacker, attacker_health, defender, defender_health):
    attacker_for_units_df = attacker
    for num in digits:
        if num in attacker:
            attacker_for_units_df = attacker.replace(num, '')
    
    if attackers_df.loc[attacker, 'Veteran'] == True:
        attacker_max_health = attackers_df.loc[attacker, 'unit_in_unit_health'] + 5
    else:
        attacker_max_health = attackers_df.loc[attacker, 'unit_in_unit_health']
    
    if defender_vet == 'T':
        defender_max_health = units_df.loc[defender, 'Health'] + 5
    else:
        defender_max_health = units_df.loc[defender, 'Health']
    
    attackForce = float(units_df.loc[attacker_for_units_df, 'Attack']) * (float(attacker_health) / float(attacker_max_health))
    defenseForce = float(units_df.loc[defender, 'Defense']) * (float(defender_health) / float(defender_max_health)) * defenseBonus
    totalDamage = attackForce + defenseForce
    attackResult = (attackForce / totalDamage) * float(units_df.loc[attacker_for_units_df, 'Attack']) * 4.5
    defenseResult = (defenseForce / totalDamage) * float(units_df.loc[defender, 'Defense']) * 4.5

    if attackers_df.at[attacker, 'safe_dist'] == True or units_df.at[defender, 'Retaliate'] == False:
        defenseResult = 0
        
    round_attackResult = proper_round(float(attackResult))
    round_defenseResult = proper_round(float(defenseResult))
    if int(round_attackResult) > int(defender_health):
        round_attackResult = defender_health

    end_defenderHealth = int(defender_health) - int(round_attackResult)
    
    if end_defenderHealth > 0:
        end_attackerHealth = int(attacker_health) - int(round_defenseResult)
        if end_attackerHealth < 0:
            end_attackerHealth = 0
    else:
        end_attackerHealth = attacker_health
        round_defenseResult = 0
    defender_health_mem.append(end_defenderHealth)
    defender_health_rounds.append(end_defenderHealth)
    after_attack_health_list.append(end_attackerHealth)
    
def PolyAttackScore(attacker, attacker_health, defender, defender_health):
    attacker_for_units_df = attacker
    for num in digits:
        if num in attacker:
            attacker_for_units_df = attacker.replace(num, '')

    if attackers_df.loc[attacker, 'Veteran'] == True:
        attacker_max_health = attackers_df.loc[attacker, 'unit_in_unit_health'] + 5
    else:
        attacker_max_health = attackers_df.loc[attacker, 'unit_in_unit_health']
        

    attackForce = float(units_df.loc[attacker_for_units_df, 'Attack']) * (float(attacker_health) / float(attacker_max_health))
    defenseForce = float(units_df.loc[defender, 'Defense']) * (float(defender_health) / float(units_df.loc[defender, 'Health'])) * defenseBonus
    totalDamage = attackForce + defenseForce
    attackResult = (attackForce / totalDamage) * float(units_df.loc[attacker_for_units_df, 'Attack']) * 4.5
    defenseResult = (defenseForce / totalDamage) * float(units_df.loc[defender, 'Defense']) * 4.5

    if attackers_df.at[attacker, 'safe_dist'] == True or units_df.at[defender, 'Retaliate'] == False:
        defenseResult = 0
        
    round_attackResult = proper_round(float(attackResult))
    round_defenseResult = proper_round(float(defenseResult))
    if int(round_attackResult) > int(defender_health):
        round_attackResult = defender_health

    end_defenderHealth = int(defender_health) - int(round_attackResult)
        
    defender_health_int.append(end_defenderHealth)
    defender_health_record.append(end_defenderHealth)
    
    if end_defenderHealth > 0:
        end_attackerHealth = int(attacker_health) - int(round_defenseResult)
        if end_attackerHealth < 0:
            end_attackerHealth = 0
    else:
        end_attackerHealth = attacker_health
        round_defenseResult = 0
    after_attacker_health_list.append(end_attackerHealth)

    multiplier = 1
    
    if attackers_df.loc[attacker, 'knight_chain'] == True and end_defenderHealth == 0:
        multiplier = 2
    if attackers_df.loc[attacker, 'splash_damage'] == True:
        multiplier = 1 + (num_splash * 0.1)
    
    starValue(round_attackResult, defender_health, attacker, round_defenseResult,
              attacker_health, units_df.loc[defender, 'Cost'],
              attackers_df.loc[attacker, 'unit_in_unit_cost'], multiplier)

attackers_df_temp = attackers_df.reset_index()
for index, row in attackers_df_temp.iterrows():
    PolyAttackScore(attackers_df_temp.loc[index, 'Unit'], attackers_df_temp.loc[index, 'Health'], defender, defender_health)

attackers_df = attackers_df.assign(attackScore = starValueScores, end_defenderHealth = defender_health_record)

attack_order = []
attackers_df_temp = attackers_df.reset_index()
temp_dups = attackers_df_temp['unit_mem'].duplicated()
attackers_df_temp = attackers_df_temp.assign(temp_dup = temp_dups)
scoreDups = attackers_df_temp['attackScore'].duplicated()
attackers_df_temp = attackers_df_temp.assign(scoreDup = scoreDups)

def bestAttack(attackers_df_temp):
    bestAttack = attackers_df_temp['attackScore'].max()
    
    bestAttackUnit = str()
    bestAttackUnitHealth = int()
    
    x=0
    while x < 1:
        for index, row in attackers_df_temp.iterrows():
            if row['attackScore'] == bestAttack and row['scoreDup'] == False:
                attack_order.append(row['Unit'])
                bestAttackUnit = row['Unit']
                bestAttackUnitHealth = row['Health']
                x += 1

    PolyDamageCalc(attackers_df.loc[bestAttackUnit, 'unit_mem'], bestAttackUnitHealth, defender, defender_health_mem[0])
    del defender_health_mem[0]

bestAttack(attackers_df_temp)

n = 1
while n < len(attackers_df):
    if defender_health_mem[0] == 0:
        break
    for unit in attack_order:
        for index, row in attackers_df_temp.iterrows():
            if unit == row['Unit']:
                attackers_df_temp.drop(index, inplace=True)

    starValueScores.clear()
    attackers_df_temp.drop(['attackScore'], axis=1, inplace=True)
    for unit in attackers_df_temp['Unit']:
        PolyAttackScore(unit, attackers_df.loc[unit, 'Health'], defender, defender_health_mem[0])
    attackers_df_temp = attackers_df_temp.assign(attackScore = starValueScores)
    
    attackers_df_temp.drop(['temp_dup'], axis=1, inplace=True)
    temp_dups = attackers_df_temp['unit_mem'].duplicated()
    attackers_df_temp = attackers_df_temp.assign(temp_dup = temp_dups)
    
    attackers_df_temp.drop(['scoreDup'], axis=1, inplace=True)
    scoreDups = attackers_df_temp['attackScore'].duplicated()
    attackers_df_temp = attackers_df_temp.assign(scoreDup = scoreDups)
    
    bestAttack(attackers_df_temp)
    
    n += 1

x=0
for i in attack_order:
    print(f"For attack {x+1} you should use the {i}; the {defender}" 
          f" will be left with {defender_health_rounds[x+1]} health and"
          f" your {i} will have {after_attack_health_list[x]} health")
    x += 1











