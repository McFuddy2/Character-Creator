import random
from names import *
from races import *
from classes import *
from itertools import combinations
from backgrounds import *
from feats import *


# -Random generate flaws,bonds, and ideals
# -write out features/traits
# -take suggested spells
# -print all the above in a decently readable way.
saving_throw_list = {"Strength":False,
                     "Deterity":False,
                     "Constitution":False,
                     "Wisdom":False,
                     "Intelligence":False,
                     "Charisma":False}

skills_list = {"Acrobatics":False,
        "Animal Handling":False,
        "Arcana":False,
        "Athletics":False,
        "Deception":False,
        "History":False,
        "Insight":False,
        "Intimidation":False,
        "Investigation":False,
        "Medicine":False,
        "Nature":False,
        "Perception":False,
        "Performance":False,
        "Persuasion":False,
        "Religion":False,
        "Sleight of Hand":False,
        "Stealth":False,	
        "Survival":False}


class Character:
    def __init__(self, level=1):
        self.equipment = {}
        self.skill_proficency = skills_list.copy()
        self.skill_bonuses = skills_list.copy()
        self.saving_throw_prof = saving_throw_list.copy()
        self.saving_throw_bonuses = saving_throw_list.copy()
        self.armor_training = set()
        self.weapon_prof = set()
        self.languages = set()
        self.level = level
        self.proficency_bonus = 2
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.wisdom = 10
        self.intelligence = 10
        self.charisma = 10
        self.assign_stats()
        self.assign_name()
        self.assign_background()
        self.assign_race()
        self.pick_a_class()
        self.strength_mod = (self.strength - 10) // 2
        self.dexterity_mod = (self.dexterity - 10) // 2
        self.constitution_mod = (self.constitution - 10) // 2
        self.wisdom_mod = (self.wisdom - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.charisma_mod = (self.charisma - 10) // 2
        self.update_skill_bonuses()
        self.initiative = 0 + self.dexterity_mod
        self.update_saving_throws()
        self.allignment = random.choice("Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic, Evil")
        self.hp = self.dndclass.hit_die + self.constitution_mod



    def assign_stats(self):
        standard_array = [15,14,13,12,10,8]
        stats_to_assign = ["strength","dexterity","constitution","wisdom","intelligence","charisma"]
        while standard_array:
            picked_num = random.choice(standard_array)
            picked_stat = random.choice(stats_to_assign)
           
            setattr(self,picked_stat, picked_num)
           
            standard_array.remove(picked_num)
            stats_to_assign.remove(picked_stat)
           
    def assign_name(self):
        self.first_name = random.choice(first_name)
        self.last_name = random.choice(last_name)


    def assign_race(self):
        self.race = random.choice(race_list)

    def pick_a_class(self):
        stat_req_met = set()
        potential_class = set()
        if self.strength > 12: stat_req_met.add("Strength")
        if self.dexterity > 12: stat_req_met.add("Dexterity")
        if self.constitution > 12: stat_req_met.add("Constitution")
        if self.wisdom > 12: stat_req_met.add("Wisdom")
        if self.intelligence > 12: stat_req_met.add("Intelligence")
        if self.charisma > 12: stat_req_met.add("Charisma")

        for pair in combinations(stat_req_met, 2):
            stat_req_met.add(f"{pair[0]} and {pair[1]}")

        stat_req_met_list = list(stat_req_met)

        for stat in stat_req_met_list:
            if stat in class_options:
                potential_class.update(class_options[stat])


        self.dndclass = random.choice(list(potential_class))
        
        self.merge_inventories(self.dndclass.starting_equipment)


        class_skills = random.sample(self.dndclass.skill_list, self.dndclass.num_of_skills)
        for i in range(len(class_skills)):
            self.skill_proficency[class_skills[i]] = True


        self.saving_throw_prof[self.dndclass.saving_throw_prof[0]] = True
        self.saving_throw_prof[self.dndclass.saving_throw_prof[1]] = True





    def assign_background(self):
        self.background = random.choice(all_backgrounds)
        if self.background.ability_improvements[0] == "Strength":
            self.strength += 2

        elif self.background.ability_improvements[0] == "Dexterity":
            self.dexterity += 2
        elif self.background.ability_improvements[0] == "Constitution":
            self.constitution += 2
        elif self.background.ability_improvements[0] == "Wisdom":
            self.wisdom += 2
        elif self.background.ability_improvements[0] == "Intelligence":
            self.intelligence += 2
        elif self.background.ability_improvements[0] == "Charisma":
            self.charisma += 2

        if self.background.ability_improvements[0] == "Strength":
            self.strength += 1
        elif self.background.ability_improvements[1] == "Dexterity":
            self.dexterity += 1
        elif self.background.ability_improvements[1] == "Constitution":
            self.constitution += 1
        elif self.background.ability_improvements[1] == "Wisdom":
            self.wisdom += 1
        elif self.background.ability_improvements[1] == "Intelligence":
            self.intelligence += 1
        elif self.background.ability_improvements[1] == "Charisma":
            self.charisma += 1
        self.merge_inventories(self.background.equipment)

        self.skill_proficency[self.background.skill_prof[0]] = True
        self.skill_proficency[self.background.skill_prof[1]] = True


    def merge_inventories(self, new_inv):
        for key, value in new_inv.items():
                if key in  self.equipment:
                    self.equipment[key] += value
                else:
                    self.equipment[key] = value

    def update_skill_bonuses(self):
        strength_skills = ["Athletics"]
        deterity_skills = ["Acrobatics", "Sleight of Hand", "Stealth"]
        wisdom_skills = ["Animal Handling", "Insight", "Medicine", "Perception", "Survival"]
        intelligence_skills = ["Arcana", "History", "Investigation", "Nature", "Religion"]
        charisma_skills = ["Deception", "Intimidation", "Performance", "Persuasion"]

        for skill in self.skill_proficency:
            proficency = self.skill_proficency[skill] 
            if proficency == True:
                self.skill_bonuses[skill] = self.proficency_bonus
            else:
                self.skill_bonuses[skill] = 0
        for skill in self.skill_bonuses:
            if skill in strength_skills:
                self.skill_bonuses[skill] += self.strength_mod
            elif skill in deterity_skills:
                self.skill_bonuses[skill] += self.dexterity_mod
            elif skill in wisdom_skills:
                self.skill_bonuses[skill] += self.wisdom_mod
            elif skill in intelligence_skills:
                self.skill_bonuses[skill] += self.intelligence_mod
            elif skill in charisma_skills:
                self.skill_bonuses[skill] += self.charisma_mod


    def update_saving_throws(self):
        for stat in self.saving_throw_prof:
            if stat == True:
                self.saving_throw_bonuses[stat] = 0 + self.proficency_bonus
            else:
                self.saving_throw_bonuses[stat] = 0


        self.saving_throw_bonuses["Strength"] += self.strength_mod
        self.saving_throw_bonuses["Deterity"] += self.dexterity_mod
        self.saving_throw_bonuses["Constitution"] += self.constitution_mod
        self.saving_throw_bonuses["Wisdom"] += self.wisdom_mod
        self.saving_throw_bonuses["Intelligence"] += self.intelligence_mod
        self.saving_throw_bonuses["Charisma"] += self.charisma_mod



new = Character()


print(f"I am {new.first_name} {new.last_name}, I am a proud {new.race}") 
print(f"I use to be a {new.background} and now I am a {new.dndclass}.")
print(f"my equipment includes {new.equipment}")
print(f"my speed is {new.race.speed_in_feet} feet per round")
print(f"here is my skills list: {new.skill_bonuses}")
print(f"I have a STR of {new.strength} which is a {new.strength_mod} modifier")
print(f"I have a DEX of {new.dexterity} which is a {new.dexterity_mod} modifier")
print(f"I have a CON of {new.constitution} which is a {new.constitution_mod} modifier")
print(f"I have a WIS of {new.wisdom} which is a {new.wisdom_mod} modifier")
print(f"I have an INT of {new.intelligence} which is a {new.intelligence_mod} modifier")
print(f"and I have a CHA of {new.charisma} which is a {new.charisma_mod} modifier")
print(f"As a {new.race} I have the following special traits; {new.race.special_traits}")
print(f"I am no longer the {new.background} I once was. However I did learn a special feat that I think will benefit me, {new.background.feat}")
print(f"Because of my {new.background.feat}, {new.background.feat.feat_features}")





