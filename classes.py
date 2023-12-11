import random


class_options = {}


class DNDClass:
    def __init__(self, class_name, primary_abilities, hit_die, saving_throw_prof, num_of_skills, skill_list, weapon_prof, tool_prof, armor_training, starting_equipment, class_features):
        self.primary_abilities = primary_abilities
        self.class_name = class_name
        self.hit_die = hit_die
        self.saving_throw_prof = saving_throw_prof
        self.num_of_skills = num_of_skills
        self.skill_list = skill_list
        self.weapon_prof = weapon_prof
        self.tool_prof = tool_prof
        self.armor_training = armor_training
        self.starting_equipment = starting_equipment
        self.class_features = class_features
        self.add_to_chooseable_options()
        self.choose_equipment()


    def __str__(self):
        return f"{self.class_name}"

    def add_to_chooseable_options(self):
        if len(self.primary_abilities) == 2:
            if self.primary_abilities[0] in class_options:
                class_options[self.primary_abilities[0]].append(self)
            else:
                class_options.update({self.primary_abilities[0]:[self]})
            if self.primary_abilities[1] in class_options:
                class_options[self.primary_abilities[1]].append(self)
            else:
                class_options.update({self.primary_abilities[1]:[self]})
        elif self.primary_abilities in class_options:
            class_options[self.primary_abilities].append(self)
        else:
            class_options.update({self.primary_abilities:[self]})

    def choose_equipment(self):
        if isinstance(self.starting_equipment, tuple):
            my_choice = random.choice(self.starting_equipment[1:])
            updated_starting_equipment = self.starting_equipment[0]
            for key, value in my_choice.items():
                if key in  self.starting_equipment[0]:
                    self.starting_equipment[0][key] += value
                    self.updated_starting_equipment = self.starting_equipment[0]
                else:
                    self.starting_equipment[0][key] = value
                    self.updated_starting_equipment = self.starting_equipment[0]
            self.starting_equipment = updated_starting_equipment
        



barbarian_additional_equipment = {"explorer's pack":1, "handaxes":4, "GP":15}
barb_equip1 = {"greataxe":1} 
barb_equip2 = {"battleaxe":1, "shield":1, "GP":15}
barbarian_equipment = (barbarian_additional_equipment)

bard_equipment = (barb_equip1, barb_equip2)



cleric_equipment = ()



druid_equipment = ()


fighter_additional_equipment = {"Chain Mail":1, "Crossbow Bolts":20, "Dungeoneer’s Pack":1, "Light Crossbow":1,"Quiver":1, "GP":1}
fight_equip1 = {"Greatsword":1}
fight_equip2 = {"Longsword":1, "Shield":1, "GP":25}
fighter_equipment = (fighter_additional_equipment, fight_equip1, fight_equip2)


monk_equipment = ()


paladin_equipment = ()


ranger_equipment = ()


rogue_equipment = ()


sorcerer_equipment = ()


warlock_equipment = ()


wiard_equipment = ()






barbarian_features = () 
bard_features = ()
cleric_features = ()
druid_features = ()
fighter_features = ()
monk_features = ()
paladin_features = ()
ranger_features = ()
rogue_features = ()
sorcerer_features = ()
warlock_features = ()
wiard_features = ()







barbarian = DNDClass("Barbarian", "Strength", 12, ("Strength", "Constitution"), 2, ("Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"), ("simple", "martial"), None, ("light", "medium", "shields"), barbarian_equipment, barbarian_features)
fighter = DNDClass("Fighter", ("Strength", "Dexterity"), 10, ("Strength", "Constitution"), 2, ("Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Persuasion", "Perception", "Survival"),("simple","martial"), None, ("light", "medium", "heavy", "shields"), fighter_equipment,fighter_features)




