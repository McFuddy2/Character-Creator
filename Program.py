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
        self.equipment = {"GP":0}
        self.skill_proficency = skills_list.copy()
        self.skill_bonuses = skills_list.copy()
        self.saving_throw_prof = saving_throw_list.copy()
        self.saving_throw_bonuses = saving_throw_list.copy()
        self.armor_training = set()
        self.weapon_prof = set()
        self.tool_prof = set()
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
        self.assign_race()
        self.assign_background()
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
        self.allignment = random.choice(["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic, Evil"])
        self.hp_modifier = 0
        self.hp = self.dndclass.hit_die + self.constitution_mod + self.hp_modifier
        
        


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
        if self.race.gain_skill_prof != None:
            for key, value in self.race.gain_skill_prof:
                race_skills = random.sample(value, key)
                for skill in race_skills:
                    self.skill_proficency[skill] = True
        if self.race.gain_tool_prof != None:
            for key, value in self.race.gain_skill_prof:
                race_tools = random.sample(value, key)
                for tool in race_tools:
                    self.tool_prof.append(tool) 
        if self.race.gain_feat != None:
            pass 
        if self.race.gain_hp != None:
            for hp_amount, per_x_levels in self.race.gain_hp:
                self.hp_modifier += (hp_amount * (per_x_levels*self.level))
        if self.race.gain_spells != None:
            pass 



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


        self.weapon_prof.add(self.dndclass.weapon_prof) 
        self.tool_prof.add(self.dndclass.tool_prof)
        self.armor_training.add(self.dndclass.armor_training)


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


        self.tool_prof.add(self.background.tool_prof)
        self.languages.add("Common")
        self.languages.add(self.background.language)
        


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
equipment_items = [(quantity, item) for item, quantity in new.equipment.items()]
equipment_str = "\n".join([f"{item[0]}x {item[1]}" for item in equipment_items])
skills_str = "\n".join([f"{skill:<20} {bonus}" for skill, bonus in new.skill_bonuses.items()])

grouped_items = [equipment_items[i:i+3] for i in range(0, len(equipment_items), 3)]
formatted_equipment = "\n".join([", ".join([f"{item[0]}x {item[1]}" for item in group]) for group in grouped_items])
languages_str = ', '.join(new.languages)
tools_str = "None" 
if new.tool_prof != None:
    tools_str = ', '.join(tool for tool in new.tool_prof if tool is not None)







print(f"######################################################################")
print(f"I am {new.first_name} {new.last_name}, I am a proud {new.race}") 
print(f"I use to be a {new.background} and now I am a {new.dndclass}.")
print(f"######################################################################")
print(f"My equipment includes: {formatted_equipment}")
print(f"######################################################################")
print(f"My stats are:")
print(f"HP:  {new.hp}       Initiative: {new.initiative}")
print(f"STR: {new.strength_mod} ({new.strength})   DEX: {new.dexterity_mod} ({new.dexterity})")
print(f"CON: {new.constitution_mod} ({new.constitution})   WIS: {new.wisdom_mod} ({new.wisdom})")
print(f"INT: {new.intelligence_mod} ({new.intelligence})   CHA: {new.charisma_mod} ({new.charisma})")
print(f"######################################################################")
print(f"Here is my skills list:\n{skills_str}")
print(f"######################################################################")
print(f"I am good with {new.weapon_prof} weapons.")
print(f"I am handy with {tools_str}")
print(f"I can also speak {languages_str}.")
print(f"I can wear the following Armor types; {new.armor_training}")
print(f"######################################################################")



