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
                     "Dexterity":False,
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
    def __init__(self, level=1, stats="Standard Array"):
        self.equipment = {"GP":0}
        self.stats= stats
        self.skill_proficency = skills_list.copy()
        self.skill_bonuses = skills_list.copy()
        self.saving_throw_prof = saving_throw_list.copy()
        self.saving_throw_bonuses = saving_throw_list.copy()
        self.armor_training = set()
        self.weapon_prof = set()
        self.tool_prof = set()
        self.languages = set()
        self.list_of_feats = set()
        self.initiative = 0
        self.hp_modifier = 0
        self.spell_list = {}
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
        self.handle_feats()
        self.strength_mod = (self.strength - 10) // 2
        self.dexterity_mod = (self.dexterity - 10) // 2
        self.constitution_mod = (self.constitution - 10) // 2
        self.wisdom_mod = (self.wisdom - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.charisma_mod = (self.charisma - 10) // 2
        self.update_skill_bonuses()
        self.initiative += self.dexterity_mod
        self.update_saving_throws()
        self.allignment = random.choice(["Lawful Good", "Lawful Neutral", "Lawful Evil", "Neutral Good", "True Neutral", "Neutral Evil", "Chaotic Good", "Chaotic Neutral", "Chaotic, Evil"])
        self.hp = self.dndclass.hit_die + self.constitution_mod + self.hp_modifier
        
        


    def assign_stats(self):
        stats_to_use = []
        if self.stats == "Rolled":
            rolled_stats = []
            for i in range(7):
                rolled_num = [random.randint(1, 6) for _ in range(4)]
                min_number = min(rolled_num)
                rolled_num.remove(min_number)
                rolled_stats.append(sum(rolled_num))
            rolled_stats.remove(min(rolled_stats))
            stats_to_use = rolled_stats
            print(stats_to_use)
        else:
            stats_to_use = [15,14,13,12,10,8]
        stats_to_assign = ["strength","dexterity","constitution","wisdom","intelligence","charisma"]
        while stats_to_use:
            picked_num = random.choice(stats_to_use)
            picked_stat = random.choice(stats_to_assign)
           
            setattr(self,picked_stat, picked_num)
           
            stats_to_use.remove(picked_num)
            stats_to_assign.remove(picked_stat)
           
    def assign_name(self):
        self.first_name = random.choice(first_name)
        self.last_name = random.choice(last_name)


    def assign_race(self):
        self.race = random.choice(race_list)
        if self.race.gain_skill_prof != None:
            self.mark_skills_as_proficent(self.race.gain_skill_prof)
        if self.race.gain_tool_prof != None:
            for tool in self.race.gain_tool_prof:
                self.tool_prof.add(tool) 
            print(tool)
        if self.race.gain_feat != None:
            for feat in self.race.gain_feat:
                self.list_of_feats.add(feat)
        if self.race.gain_hp is not None:
            if isinstance(self.race.gain_hp, (list, tuple)):
                hp_amount, per_x_levels = self.race.gain_hp
                self.hp_modifier += (hp_amount * (per_x_levels * self.level))
            elif isinstance(self.race.gain_hp, int):
                self.hp_modifier += self.race.gain_hp
        if self.race.gain_spells is not None:
            if isinstance(self.race.gain_spells, dict):
                self.merge_spell_lists(self.race.gain_spells)
            elif isinstance(self.race.gain_spells, list):
                self.merge_spell_lists(self.race.gain_spells[0])



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
        if self.background.feat != None:
            for feat in self.background.feat:
                self.list_of_feats.add(feat)




    def handle_feats(self):
        for feat in self.list_of_feats:
            if feat.gain_skill_prof is not None:
                self.mark_skills_as_proficent(feat.gain_skill_prof)
            if feat.gain_hp is not None:
                if self.hp_modifier is None:
                    self.hp_modifier = feat.gain_hp
            if feat.gain_tool_prof is not None:
                for tool in feat.gain_tool_prof:
                    self.tool_prof.add(tool) 
            if feat.gain_spells != {}:
                self.merge_spell_lists(feat.gain_spells)
            if feat.gain_initiative is not None:
                if feat.gain_initiative == "Proficency Bonus":
                    self.initiative += self.proficency_bonus
            if feat.gain_armor_training is not None:
                for armor in feat.gain_armor_training:
                    self.armor_training.add(armor)




    def mark_skills_as_proficent(self, new_skills):
        for skill in new_skills:
            if self.skill_proficency[skill] != True:
                self.skill_proficency[skill] = True
            else:
                pick_one = []
                for skill, value in self.skill_proficency.items():
                    if value == False:
                        pick_one.append(skill)
                new_skill_gained = random.choice(pick_one)
                self.skill_proficency[new_skill_gained] = True
                




    def merge_inventories(self, new_inv):
        for key, value in new_inv.items():
                if key in  self.equipment:
                    self.equipment[key] += value
                else:
                    self.equipment[key] = value


    def merge_spell_lists(self, new_spells):
        for key, value in new_spells.items():
                if key in  self.spell_list:
                    self.spell_list[key].append(value)
                else:
                    self.spell_list[key] = value


    def update_skill_bonuses(self):
        strength_skills = ["Athletics"]
        dexterity_skills = ["Acrobatics", "Sleight of Hand", "Stealth"]
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
            elif skill in dexterity_skills:
                self.skill_bonuses[skill] += self.dexterity_mod
            elif skill in wisdom_skills:
                self.skill_bonuses[skill] += self.wisdom_mod
            elif skill in intelligence_skills:
                self.skill_bonuses[skill] += self.intelligence_mod
            elif skill in charisma_skills:
                self.skill_bonuses[skill] += self.charisma_mod


    def update_saving_throws(self):
        for stat, is_proficient in self.saving_throw_prof.items():
            if is_proficient:  # Check if the saving throw is proficient
                self.saving_throw_bonuses[stat] = 0 + self.proficency_bonus
            else:
                self.saving_throw_bonuses[stat] = 0


        self.saving_throw_bonuses["Strength"] += self.strength_mod
        self.saving_throw_bonuses["Dexterity"] += self.dexterity_mod
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
weapon_prof_str = ', '.join(str(weapon).capitalize() for weapon in new.weapon_prof) if new.weapon_prof else "None"







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
print(f"I am good with {weapon_prof_str} weapons.")
print(f"I am handy with {tools_str}")
print(f"I can also speak {languages_str}.")
print(f"I can wear the following Armor types; {new.armor_training}")
print(f"######################################################################")
print(f"I have taken some feats; {new.list_of_feats}")
print(f"######################################################################")
print(f"Here is my spellbook; {new.spell_list}")

