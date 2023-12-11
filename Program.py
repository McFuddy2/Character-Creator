import random
from names import first_name, last_name
from races import Race, race_list
from classes import class_options, DNDClass
from itertools import combinations
from backgrounds import Feat, Background, all_backgrounds, all_feats

# -UA content
# -Pick background based on where the +2 +1 go (check to see if that works… are there missing options? How to handle that…)
# -Random generate flaws,bonds, and ideals
# -randomly pick from starting equipment.
# -write out features/traits
# -take suggested spells
# -print all the above in a decently readable way.



class Character:
    def __init__(self):
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.wisdom = 10
        self.intelligence = 10
        self.charisma = 10
        self.assign_stats()
        self.assign_name()
        self.assign_race()
        self.pick_a_class()
        self.assign_background()


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

    def assign_background(self):
        self.background = random.choice(all_backgrounds)








new = Character()
print(f"I am {new.first_name} {new.last_name}, a proud {new.race}") 
print(f"I use to be a {new.background} and now i am a {new.dndclass}.")
print(f"my speed is {new.race.speed_in_feet} feet per round")
print(f"I have a STR of {new.strength}",
      f"I have a DEX of {new.dexterity}",
      f"I have a CON of {new.constitution}",
      f"I have a WIS of {new.wisdom}",
      f"I have an INT of {new.intelligence}",
      f"and I have a CHA of {new.charisma}")







