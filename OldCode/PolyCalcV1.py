#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:18:52 2024

@author: joshmassey-thompson
"""
import pandas as pd
import math

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
                                      'Knight', 'Giant'])
         }

units_df = pd.DataFrame(stats)


attacker = input('What is the attacking troop? ')
attacker_health = float(input('How much health is the attacking troop on? '))
defender = input('What is the defending troop? ')
defender_health = float(input('How much health is the defending troop on? '))
defenseBonus = 1.0

def proper_round(Result):
    if Result - math.floor(Result) < 0.5:
        return math.floor(Result)
    else:
        return math.ceil(Result)

def PolyAttackCalc(attacker, attacker_health, defender, defender_health):
    if defender != 'Giant':
        dbonus = input('Do you have a defence bonus? (T/F) \n')
        if dbonus == 'T':
            defenseBonus = 1.5
            citywall = input('Are you on a walled city? (T/F) \n')
            if citywall == 'T':
                defenseBonus = 4.0
        if dbonus == 'F':
            defenseBonus = 1.0
    
    attackForce = float(units_df.loc[attacker, 'Attack']) * (float(attacker_health) / float(units_df.loc[attacker, 'Health']))
    defenseForce = float(units_df.loc[defender, 'Defense']) * (float(defender_health) / float(units_df.loc[defender, 'Health'])) * defenseBonus
    totalDamage = attackForce + defenseForce
    attackResult = (attackForce / totalDamage) * float(units_df.loc[attacker, 'Attack']) * 4.5
    defenseResult = (defenseForce / totalDamage) * float(units_df.loc[defender, 'Defense']) * 4.5
        
    round_attackResult = proper_round(attackResult)
    round_defenseResult = proper_round(defenseResult)
    
    end_defenderHealth = defender_health - round_attackResult
    if end_defenderHealth < 0:
        end_defenderHealth = 0
    
    if end_defenderHealth > 0:
        end_attackerHealth = attacker_health - round_defenseResult
        if end_attackerHealth < 0:
            end_attackerHealth = 0
    else:
        end_attackerHealth = attacker_health
    
    print(f"Attacker Health:{end_attackerHealth} \nDefender Health:{end_defenderHealth}")

PolyAttackCalc(attacker, attacker_health, defender, defender_health)


