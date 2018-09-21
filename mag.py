import person
import magSkills

class Mag(person.Person):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.max_hitpoint = 1000
        self.stats['defense'] = 500
        self.stats['resistance'] = 1500
        self.stats['damage'] = 500
        self.stats['hitpoint'] = self.max_hitpoint
        self.stats['chance_krit'] = 79
        self.stats['precision'] = 10
        self.stats['evasion'] = 0#20
        self.skills.append(magSkills.magic_arrow)
