# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:03:55 2024

@author: joshm
"""
import math

# Damage calculator function
def PolyDamageCalc(attacker, defender):
    
    attackForce = attacker.attack * (attacker.health / attacker.maxHealth)
    defenceForce = defender.defence * (defender.health / defender.maxHealth) * defender.defenceBonus 
    totalDamage = attackForce + defenceForce 
    attackResult = math.ceil((attackForce / totalDamage) * attacker.attack * 4.5) 
    defenceResult = math.floor((defenceForce / totalDamage) * defender.defence * 4.5)
   
    if not defender.retaliate:
        defenceResult = 0
    elif attackResult >= defender.health:
        defenceResult = 0
        attackResult = defender.health
    elif 'Convert' in attacker.skills:
        defenceResult = 0
        attackResult = defender.health
    
    end_defenderHealth = defender.health - attackResult
    end_attackerHealth = attacker.health - defenceResult

    return attackResult, defenceResult, end_attackerHealth, end_defenderHealth


def starValue(attacker, defender):
    attackResult, defenceResult, end_attackerHealth, end_defenderHealth = PolyDamageCalc(attacker, defender)
    if attacker == 'Juggernaut' and end_defenderHealth != 0:
        attacker.multiplier -= 0.5
    if 'Eat' in attacker.skills and end_defenderHealth <= 0:
        attacker.multiplier += 1
    attackValue = 1 + (attackResult / defender.health) * defender.cost * attacker.multiplier
    retaliationCost = 1 + (defenceResult / attacker.health) * attacker.cost
    starValue = attackValue / retaliationCost
    return starValue

def bestAttacker(attacker_dict, defender):
    bestStarValue = 0
    bestUnitKey = None
    for attacker in attacker_dict.keys():
        starVal = starValue(attacker_dict[attacker], defender)
        print(starVal)
        if starVal > bestStarValue:
            bestStarValue = starVal
            bestUnitKey = attacker
    
    bestUnitInstance = attacker_dict[bestUnitKey]
    del attacker_dict[bestUnitKey]
    return bestUnitInstance


def AttackOrder(attacker_dict, defender):
    attackOrderDict = {}
    nAttackers = len(attacker_dict)
    n = 0
    x = 1
    while n < nAttackers:
        bestUnitInstance = bestAttacker(attacker_dict, defender)
        attackOrderDict[f'attack{x}'] = bestUnitInstance
        
        attackResult, defenceResult, end_attackerHealth, end_defenderHealth = PolyDamageCalc(bestUnitInstance, defender)
        if end_defenderHealth <= 0:
            break
        defender.health = end_defenderHealth
        if 'Poison' in bestUnitInstance.skills:
            defender.defenceBonus = 0.8
        n += 1
        x += 1
    
    return attackOrderDict












