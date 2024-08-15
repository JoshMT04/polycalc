# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:32:35 2024

@author: joshm
"""
unit_cost_dict = {'Warrior':2, 'Archer':3, 'Defender':3,
       'Rider':3,'Cloak':8, 'Dagger':1, 'Mind bender':5, 
       'Swordsman':5, 'Catapult':8, 'Knight':8,
       'Giant':20}
unit_health_dict = {'Warrior':10, 'Archer':10, 'Defender':15,
       'Rider':10,'Cloak':5, 'Dagger':10, 'Mind bender':10, 
       'Swordsman':15, 'Catapult':10, 'Knight':10,
       'Giant':40}

class Unit:
    
    unit_class = None
    maxHealth = 10
    movement = 1
    attack = 2
    defence = 2
    cost = 2
    atk_range = 1
    retaliate = True
    skills = ['Dash', 'Fortify']
    defenceBonus = 1
    unit_in_unit = None
    splash = False
    multiplier = 1
    
    def __init__(self, health, veteran, attacker):
        self.health = health
        self.veteran = veteran
        self.attacker = attacker
        
        if self.veteran:
            self.maxHealth += 5
        if 'Carry' in self.skills and self.attacker:
            self.unit_in_unit = input(f'Which unit was used to make your {self.unit_class}?\n').capitalize()
            self.maxHealth = unit_health_dict[self.unit_in_unit]
            self.cost += unit_cost_dict[self.unit_in_unit]
        if 'Carry' in self.skills and not self.attacker:
            self.maxHealth = int(input(f'What is the maximum health of the enemy {self.unit_class}?\n'))
            self.cost += 3
        if 'Splash' in self.skills and self.attacker:
            splashQs = input(f'Can the attacking {self.unit_class} splash additional units? (T/F)\n')
            if splashQs == 'T':
                self.splash = True
        if not self.attacker:
            dBon = input(f'Does the defending {self.unit_class} have a defence bonus? (T/F)\n')
            if dBon == 'T':
                self.defenceBonus = 1.5
        if self.defenceBonus >= 1.5 and 'Fortify' in self.skills:
            fortBon = input(f'Does the defending {self.unit_class} have a walled city bonus? (T/F)\n')
            if fortBon == 'T':
                self.defenceBonus = 4.0
        if 'Persist' in self.skills:
            chainQs = input('Are you able to chain knight attacks? (T/F)\n')
            if chainQs == 'T':
                self.multiplier += 0.5
        if 'Convert' in self.skills:
            self.multiplier += 2
        if 'Poison' in self.skills:
            self.multiplier += 1
    
    def __repr__(self): 
        return "Unit({}, {})".format(self.health, self.veteran)
    
    def __str__(self):
        return ("The stats for your unit:\n"
                "Max Health: {}\n"
                "Movement: {}\n"
                "Attack: {}\n"
                "defence: {}\n"
                "Cost: {}\n"
                "Attack Range: {}\n"
                "Retaliate: {}\n"
                "Skills: {}\n"
                "Veteran: {}\n"
                "Unit in unit: {}").format(
                    self.maxHealth, 
                    self.movement, 
                    self.attack, 
                    self.defence, 
                    self.cost, 
                    self.atk_range, 
                    self.retaliate, 
                    self.skills, 
                    self.veteran,
                    self.unit_in_unit)

class Warrior(Unit):
    
    unit_class = 'Warrior'
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Archer(Unit):
    
    unit_class = 'Archer'
    defence = 1
    cost = 3
    atk_range = 2
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Defender(Unit):
    
    unit_class = 'Defender'
    maxHealth = 15
    attack = 1
    defence = 3
    cost = 3
    skills = ['Fortify']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Rider(Unit):
    
    unit_class = 'Rider'
    movement = 2
    defence = 1
    cost = 3
    skills = ['Dash', 'Escape', 'Fortify']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Cloak(Unit):
    
    unit_class = 'Cloak'
    maxHealth = 5
    movement = 2
    attack = 0
    defence = 0.5
    cost = 8
    retaliate = False
    skills = ['Hide', 'Sneak', 'Infiltrate', 'Dash']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Dagger(Unit):
    
    unit_class = 'Dagger'
    cost = 1
    skills = ['Dash', 'Surprise', 'Independent']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Mind_bender(Unit):
    
    unit_class = 'Mind Bender'
    attack = 0
    defence = 1
    cost = 5
    retaliate = False
    skills = ['Heal', 'Convert', 'Detect']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Swordsman(Unit):
    
    unit_class = 'Swordsman'
    maxHealth = 15
    attack = 3
    defence = 3
    cost = 5
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Catapult(Unit):
    
    unit_class = 'Catapult'
    attack = 4
    defence = 0
    cost = 8
    atk_range = 3
    retaliate = False
    skills = None
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Knight(Unit):
    
    unit_class = 'Knight'
    movement = 3
    attack = 3
    defence = 1
    cost = 8
    skills = ['Dash', 'Persist', 'Fortify']
    attack_chain = True
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Giant(Unit):
    
    unit_class = 'Knight'
    maxHealth = 40
    attack = 5
    defence = 4
    cost = 20
    skills = None
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Bunny(Unit):
    
    unit_class = 'Bunny'
    maxHealth = 20
    attack = 5
    cost = 0
    skills = ['Independent']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Bunta(Unit):
    
    unit_class = 'Bunta'
    maxHealth = 20
    attack = 5
    cost = 0
    skills = ['Independent']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Raft(Unit):
    
    unit_class = 'Raft'
    movement = 2
    attack = 0
    defence = 1
    retaliate = False
    skills = ['Carry', 'Float']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Scout(Unit):
    
    unit_class = 'Scout'
    movement = 3
    cost = 5
    atk_range = 2
    skills = ['Dash', 'Carry', 'Float', 'Scout']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Rammer(Unit):
    
    unit_class = 'Rammer'
    movement = 3
    attack = 3
    defence = 3
    skills = ['Dash', 'Carry', 'Float', 'Scout']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Bomber(Unit):
    
    unit_class = 'Bomber'
    movement = 2
    attack = 3
    defence = 2
    atk_range = 3
    retaliate = False
    skills = ['Carry', 'Float', 'Splash', 'Stiff']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Juggernaut(Unit):
    
    unit_class = 'Juggernaut'
    movement = 2
    attack = 4
    defence = 4
    retaliate = False
    skills = ['Float', 'Splash', 'Stomp']
    unit_in_unit = 'Giant'
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Dinghy(Unit):
    
    unit_class = 'Dinghy'
    maxHealth = 5
    movement = 2
    attack = 0
    defence = 0.5
    cost = 8
    retaliate = False
    skills = ['Hide', 'Sneak', 'Infiltrate', 'Dash']
    unit_in_unit = 'Cloak'
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Pirate(Unit):
    
    unit_class = 'Pirate'
    cost = 1
    skills = ['Dash', 'Surprise', 'Independent']
    unit_in_unit = 'Dagger'
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)

class Amphibian(Rider):
    
    unit_class = 'Amphibian'
    skills = ['Dash', 'Escape', 'Fortify', 'Float']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Tridention(Knight):
    
    unit_class = 'Tridention'
    maxHealth = 15
    movement = 2
    skills = ['Dash', 'Escape', 'Fortify', 'Float']

    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Crab(Giant):
    
    unit_class = 'Crab'
    attack = 4
    defence = 5
    skills = ['Escape', 'Float']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
    
class Polytaur(Unit):
    
    maxHealth = 15
    attack = 3
    defence = 1
    skills = ['Dash', 'Fortify', 'Independent']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Dragon_egg(Unit):
    
    attack = 0
    cost = 20
    retaliate = False
    skills = ['Grow', 'Fortify']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
    
class Baby_Dragon(Unit):
    
    maxHealth = 15
    movement = 2
    attack = 3
    defence = 3
    cost = 20
    skills = ['Grow', 'Dash', 'Fly', 'Escape', 'Scout']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
    
class Fire_Dragon(Baby_Dragon):
    maxHealth = 2
    movement = 3
    attack = 4
    atk_range = 2
    skills = ['Dash', 'Fly', 'Splash', 'Scout']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
    
class Ice_Archer(Archer):
    
    attack = 0.1
    skills = ['Dash', 'Fortify', 'Freeze']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
    
class Battle_Sled(Unit):
    
    maxHealth = 15
    movement = 2
    attack = 3
    cost = 5
    skills = ['Dash', 'Escape', 'Skate']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Mooni(Unit):
    
    attack = 0
    cost = 10
    retaliate = False
    skills = ['Skate', 'Freeze Area']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Ice_Fortress(Unit):
    
    maxHealth = 20
    attack = 4
    defence = 3
    cost = 15
    skills = ['Skate', 'Scout']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Gaami(Unit):
    
    maxHealth = 30
    attack = 4
    defence = 4
    cost = 20
    skills = ['Auto Freeze', 'Freeze Area']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Hexapod(Rider):
    
    maxHealth = 5
    attack = 3
    skills = ['Dash', 'Escape', 'Creep', 'Sneak']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Kiton(Defender):
    
    skills = ['Poison']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Phychi(Archer):
    
    maxHealth = 5
    attack = 1
    movement = 2
    skills = ['Fly', 'Dash', 'Poison', 'Surprise']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
    
class Shaaman(Mind_bender):
    
    attack = 1
    skills = ['Boost', 'Convert']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Raychi(Unit):
    
    maxHealth = 15
    movement = 3
    attack = 3
    skills = ['Dash', 'Float', 'Creep', 'Navigate', 'Explode']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Exida(Catapult):
    
    attack = 3
    defence = 1
    skills = ['Poison', 'Splash']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Doomux(Knight):
    
    maxHealth = 20
    attack = 4
    defence = 2
    cost = 10
    skills = ['Dash', 'Creep', 'Explode']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
        
class Centipede(Giant):
    
    maxHealth = 20
    movement = 2
    attack = 4
    defence = 3
    skills = ['Dash', 'Eat', 'Creep']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)
    
class Segment(Unit):
    
    cost = 10
    skills = ['Independent', 'Creep', 'Explode']
    
    def __init__(self, health, veteran, attacker):
        super().__init__(health, veteran, attacker)