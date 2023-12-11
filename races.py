


# so far only Dwarf and human have been added


class Race:
    def __init__(self, race_name, creature_type, size, speed_in_feet, life_span_in_years, special_traits):
        self.race_name = race_name
        self.creature_type = creature_type
        self.size  = size         
        self.speed_in_feet = speed_in_feet
        self.life_span_in_years =  life_span_in_years
        self.special_traits = special_traits

    def __str__(self):
        return f"{self.race_name}"
    

resourceful = "You gain Inspiration whenever you finish a Long Rest"
skillfull = "You gain Proficiency in one Skill of your choice "
versatile = "You gain the Skilled Feat or another 1st-level Feat of your choice"
darkvision = "You have Darkvision with a range of 60 feet."
dwarven_resilience = "You have Resistance to Poison Damage. You also have Advantage on saving throws you make to avoid or end the Poisoned Condition on yourself."
dwarven_toughness = "Your Hit Point Maximum increases by 1, and it increases by 1 again whenever you gain a level"
forge_wise = "Your divine creator gave you an uncanny affinity for working with stone or metal. You gain Tool Proficiency with two of the following options of your choice: Jeweler’s Tools, Mason’s Tools, Smith’s Tools, or Tinker’s Tools"
stonecunning = "As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes. You must be on a stone surface or touching such a surface to use this Tremorsense. The stone can be natural or worked. You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest."


human_special_traits = (resourceful, skillfull, versatile)
dwarf_special_traits = (darkvision, dwarven_resilience, dwarven_toughness, forge_wise, stonecunning)


human = Race("Human", "humanoid", ("medium", "small"), 30, 80, human_special_traits)
dwarf = Race("Dwarf", "humanoid", "medium", 30, 350, dwarf_special_traits)

race_list = (human, dwarf)

