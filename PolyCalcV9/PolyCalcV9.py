# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:23:48 2024

@author: joshm
"""
# Set WD to current folder so module loads in correctly
import os
os.chdir('C:/Users/joshm/OneDrive - Imperial College London/Computational Projects/PolyCalc/AttackCalc')

from Calc_Functions import *

#Import the Unit_classes and create a dictionary with all of them in
import Unit_Classes as uc

unit_classes = {
    'Warrior': uc.Warrior, 'Archer': uc.Archer,'Defender': uc.Defender,'Rider': uc.Rider, 
    'Cloak': uc.Cloak, 'Dagger': uc.Dagger, 'Mind bender': uc.Mind_bender, 'Swordsman': uc.Swordsman,
    'Catapult': uc.Catapult, 'Knight': uc.Knight, 'Giant': uc.Giant,'Bunny': uc.Bunny,'Bunta': uc.Bunta,
    'Raft': uc.Raft,'Scout': uc.Scout,'Rammer': uc.Rammer,'Bomber': uc.Bomber,'Juggernaut': uc.Juggernaut,
    'Dinghy': uc.Dinghy,'Pirate': uc.Pirate, 'Amphibian': uc.Amphibian,'Tridention': uc.Tridention,
    'Crab': uc.Crab, 'Polytaur': uc.Polytaur, 'Dragon Egg': uc.Dragon_egg,'Baby Dragon': uc.Baby_Dragon,
    'Fire Dragon': uc.Fire_Dragon,'Ice Archer': uc.Ice_Archer,'Battle Sled': uc.Battle_Sled,'Mooni': uc.Mooni,
    'Ice Fortress': uc.Ice_Fortress,'Gaami': uc.Gaami,'Hexapod': uc.Hexapod,'Kiton': uc.Kiton,'Phychi': uc.Phychi,
    'Shaaman': uc.Shaaman,'Raychi': uc.Raychi,'Exida': uc.Exida,'Doomux': uc.Doomux,'Centipede': uc.Centipede,
    'Segment': uc.Segment 
    }

# Define the attacking and defending units
attackers = 'warrior, warrior, Kiton'  
attackers_health = [10, 10, 10]
attackers_vet = 'T, F, F' 
defenders = 'defender'
defenders_health = [10]
defenders_vet = 'F'

# Create a dictionary with all the attacking units and their classes to access all information later
attackers_vet_list = attackers_vet.split(', ')
for index, value in enumerate(attackers_vet_list):
    if value == 'F':
        attackers_vet_list[index] = False
    elif value == 'T':
        attackers_vet_list[index] = True
        
attack_list = []
n = 0
while n < len(attackers_vet_list):
    attack_list.append(True)
    n += 1

attackers_list = [
    [attacker.capitalize(), health, vet, defend] 
    for attacker, health, vet, defend in zip(attackers.split(', '), 
                                     attackers_health, 
                                     attackers_vet_list,
                                     attack_list)]

attacker_dict = {}
for n, i in enumerate(attackers_list, start=1):
    unit_type, unit_health, unit_vet, unit_attack = i[0], i[1], i[2], i[3]
    if unit_type in unit_classes:
        unit_class = unit_classes[unit_type]
        unit = unit_class(unit_health, unit_vet, unit_attack)
        attacker_dict[f'attacker{n}'] = unit

# Create a corresponding defenders dictionary
defenders_vet_list = defenders_vet.split(', ')
for index, value in enumerate(defenders_vet_list):
    if value == 'F':
        defenders_vet_list[index] = False
    elif value == 'T':
        defenders_vet_list[index] = True
        
defend_list = []
n = 0
while n < len(defenders_vet_list):
    defend_list.append(False)
    n += 1

defenders_list = [
    [defender.capitalize(), health, vet, defend] 
    for defender, health, vet, defend in zip(defenders.split(', '), 
                                     defenders_health, 
                                     defenders_vet_list,
                                     defend_list)]

defender_dict = {}
for n, i in enumerate(defenders_list, start=1):
    unit_type, unit_health, unit_vet, unit_defend = i[0], i[1], i[2], i[3]
    if unit_type in unit_classes:
        unit_class = unit_classes[unit_type]
        unit = unit_class(unit_health, unit_vet, unit_defend)
        defender_dict[f'defender{n}'] = unit

attackOrderDict = AttackOrder(attacker_dict, defender_dict['defender1'])






















