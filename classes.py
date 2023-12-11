class_options = {}


class DNDClass:
    def __init__(self, class_name, primary_abilities, hit_die, saving_throw_prof, num_of_skills, skill_list, weapon_prof, tool_prof, armor_training, starting_equipment):
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
        self.add_to_chooseable_options()


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





barbarian_equipment = ("explorer's pack", ("greataxe", ("battleaxe", "shield", "10gold")), "4 handaxes", "15gold")
barbarian = DNDClass("Barbarian", "Strength", 12, ("Strength", "Constitution"), 2, ("Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"), ("simple", "martial"), None, ("light", "medium", "shields"), barbarian_equipment)
fighter_equipment = ("Chain Mail", "20 Crossbow Bolts", "Dungeoneer’s Pack", ("Greatsword", ("Longsword", "Shield", "25gold")), "Light Crossbow","Quiver", "11 GP")
fighter = DNDClass("Fighter", ("Strength", "Dexterity"), 10, ("Strength", "Constitution"), 2, ("Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Persuasion", "Perception", "Survival"),("simple","martial"), None, ("light", "medium", "heavy", "shields"), fighter_equipment)







