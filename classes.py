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
        



barbarian_additional_equipment = {"Explorer's Pack":1, "Handaxes":4, "GP":15}
barb_equip1 = {"Greataxe":1} 
barb_equip2 = {"Battleaxe":1, "Shield":1, "GP":15}
barbarian_equipment = (barbarian_additional_equipment, barb_equip1, barb_equip2)

bard_equipment = {"Dagger":2, "Entertainer's Pack":1, "Leather Armor":1, "Musical instrument (your choice)":1, "GP":26}

cleric_equipment = {"Chain Shirt":1, "Holy Symbol":1, "Mace":1, "Priest's Pack":1, "Shield":1, "GP":7}

druid_equipment = {"Druidic Focus (Quarterstaff)":1, "Explorer's Pack":1, "Herbalism Kit":1, "Leather Armor":1, "Shield":1, "Sickle":1, "GP":9}

fighter_additional_equipment = {"Chain Mail":1, "Crossbow Bolts":20, "Dungeoneer’s Pack":1, "Light Crossbow":1,"Quiver":1, "GP":1}
fight_equip1 = {"Greatsword":1}
fight_equip2 = {"Longsword":1, "Shield":1, "GP":25}
fighter_equipment = (fighter_additional_equipment, fight_equip1, fight_equip2)

monk_equipment = {"Artisan's Tools":1, "Dagger":5, "Explorer's Pack":1, "Musical Instrument":1, "Spear":1, "GP":9}

paladin_equipment = {"Chain Mail":1, "Holy Symbol":1, "Javelin":6, "Longsword":1, "Priest's Pack":1, "Shield":1, "GP":9}

ranger_additional_equipment = {"Arrows":20, "Druidic Focus (Sprig of Mistletoe)":1, "Explorer’s Pack":1, "Quiver":1, "Scimitar":1, "Shortsword":1, "Studded Leather Armor":1, "GP":7}
ranger_equip1 = {"Longbow":1}
ranger_equip2 = {"Shortbow":1}
ranger_equipment = (ranger_additional_equipment, ranger_equip1, ranger_equip2)

rogue_equipment = {"Arrows":20, "Burglar’s Pack":1, "Dagger":2, "Leather Armor":1, "Quiver":1, "Shortbow":1, "Shortsword":1, "Thieves’ Tools":1, "GP":18}

sorcerer_equipment = {"Arcane Focus (Crystal)":1, "Dagger":2, "Dungeoneer's Pack":1, "Spear":1, "GP":28}

warlock_equipment = {"Arcane Focus (Orb)":1, "Book (Occult Lore)":1, "Dagger":2, "Leather Armor":1, "Scholar's Pack":1, "Sickle":1, "GP":15}

wizard_equipment = {"Arcane Focus (Qurterstaff)":1, "Dagger":2, "Robe":1, "Scholar's Pack":1, "GP":5}






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
wizard_features = ()





barbarian = DNDClass("Barbarian", "Strength", 12, ("Strength", "Constitution"), 2, ("Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"), ("Simple", "Martial"), None, ("Light", "Medium", "Shield"), barbarian_equipment, barbarian_features)
bard = DNDClass("Bard", "Charisma", 8, ("Dexterity", "Charisma"), 3, ("Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"), "Simple", "3 Instruments of your choice", "Light", bard_equipment, bard_features)
cleric = DNDClass("Cleric", "Wisdom", 8, ("Wisdom", "Charisma"), 2, ("History", "Insight", "Medicine", "Persuasion", "Religion"), "Simple", None, ("Light", "Medium", "Sheild"), cleric_equipment, cleric_features)
druid = DNDClass("Druid", "Wisdom", 8, ("Intelligence", "Wisdom"), 2, ("Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"), ("Simple"), "Herbalism Kit", ("Light", "Shield"), druid_equipment, druid_features )
fighter = DNDClass("Fighter", ("Strength", "Dexterity"), 10, ("Strength", "Constitution"), 2, ("Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Persuasion", "Perception", "Survival"),("Simple","Martial"), None, ("Light", "Medium", "Heavy", "Shield"), fighter_equipment, fighter_features)
monk = DNDClass("Monk", ("Deterity and Wisdom"), 8, ("Strength", "Deterity"), 2, ("Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"), ("Simple", "Martial (if light)"), "choose 1 artisan tool OR 1 instrument", (None), monk_equipment, monk_features)
paladin = DNDClass("Paladin", ("Strength and Charisma"), 10, ("Wisdom", "Charisma"), 2, ("Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"), ("Simple", "Martial"), None, ("Light", "Medium", "Heavy", "Sheild"), paladin_equipment, paladin_features)
ranger = DNDClass("Ranger", ("Dexterity", "Wisdom"), 10, ("Strength", "Dexterity"), 3, ("Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"), ("Simple", "Martial"), None, ("Light", "Medium", "Sheild"), ranger_equipment, ranger_features)
rogue = DNDClass("Rogue", "Dexterity", 8, ("Dexterity", "Intelligence"), 4, ("Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Persuasion", "Sleight of Hand", "Stealth"), ("Simple", "Martial (if finesse)"), "thieves' Tools", "Light", rogue_equipment, rogue_features)
sorcerer = DNDClass("Sorcerer", "Charisma", 6, ("Constitution", "Charisma"), 2, ("Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"), "Simple", None, None, sorcerer_equipment, sorcerer_features)
warlock = DNDClass("Warlock", "Charisma", 8, ("Wisdom", "Charisma"), 2, ("Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"), "Simple", None, "Light", warlock_equipment, warlock_features)
wizard = DNDClass("Wizard", "Intelligence", 6, ("Intelligence", "Wisdom"), 2, ("Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"), "Simple", None, None, wizard_equipment, wizard_features)




