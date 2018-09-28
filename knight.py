import person

class Knight(person.Person):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.max_hitpoint = 4000
        self.stats['defense'] = 1500
        self.stats['resistance'] = 500
        self.stats['damage'] = 250
        self.stats['hitpoint'] = self.max_hitpoint
        self.stats['chance_krit'] = 47
        self.stats['damage_krit'] = 10
        self.stats['precision'] = 10
        self.stats['evasion'] = 60


        '''-------------------------------------**********--------------------------------------'''
        '''--------------**********-------------Faster axe--------------**********--------------'''
        '''-------------------------------------**********--------------------------------------'''
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }
            return result

        skill = person.classSkill.Skill(name='Faster axe', cast=1, coldown=0, lvl=0, finish=finish, mult=1)
        self.skills.append(skill)
"""

        '''---------------------------------------****----------------------------------------'''
        '''--------------**********---------------Bash----------------**********--------------'''
        '''---------------------------------------****----------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
                'ignoring_block': 10,
            }
            return result

        Bash = person.classSkill.Skill(name='Bash', cast=0.9, coldown=2.3, lvl=1, finish=finish, mult=0.6)
        self.skills.append(Bash)


        '''------------------------------------**********-------------------------------------'''
        '''--------------**********------------Hit shield-------------**********--------------'''
        '''------------------------------------**********-------------------------------------'''
        cast_bonus = {'front_block': 70}
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }
            result['target']['stop'] = self.stats['time']
            return result

        Hit_shield = person.classSkill.Skill(name='Hit shield', cast=1.6, coldown=2.5, lvl=2, finish=finish, mult=0.45, bonus=cast_bonus)
        self.skills.append(Hit_shield)

        '''------------------------------------**********-------------------------------------'''
        '''--------------**********------------Rink molot-------------**********--------------'''
        '''------------------------------------**********-------------------------------------'''
        cast_bonus = {'front_block': 40, 'back_block': 100}
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }
            return result

        Rink_molot = person.classSkill.Skill(name='Rink molot', cast=0.2, coldown=4, lvl=3, finish=finish, mult=0.3, repeat=5, bonus=cast_bonus)
        self.skills.append(Rink_molot)

        '''------------------------------------**********-------------------------------------'''
        '''--------------**********------------Earthquake-------------**********--------------'''
        '''------------------------------------**********-------------------------------------'''
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }
            result['target']['fall'] = {
                'this_time': self.stats['time'],
                'fall_time': 1,
            }
            return result

        Earthquake = person.classSkill.Skill(name='Earthquake', cast=1.2, coldown=4, lvl=4, finish=finish, mult=0.7)
        self.skills.append(Earthquake)

        '''------------------------------------************-------------------------------------'''
        '''--------------**********------------Break chains-------------**********--------------'''
        '''------------------------------------************-------------------------------------'''
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['self'] .append({
                'name': 'Break chains',
                'func': self.create_bonus,
                'time': 4,
                'mult_damage': 0.3,
                'defense': 100 * self.lvl,
                'resistance': 50 * self.lvl,
                'precision': 30 * self.lvl,
            })
            return result

        Break_chains = person.classSkill.Skill(name='Break chains', cast=0.4, coldown=5, lvl=5, finish=finish, mult=0)
        self.skills.append(Break_chains)

        '''--------------------------------------********---------------------------------------'''
        '''--------------**********--------------Bull run---------------**********--------------'''
        '''--------------------------------------********---------------------------------------'''
        cast_bonus = {'evasion': 1000}
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }
            result['target']['stop'] = self.stats['time']
            return result

        Bull_run = person.classSkill.Skill(name='Bull run', cast=0.7, coldown=5, lvl=6, finish=finish, mult=0.5)
        self.skills.append(Bull_run)

        '''--------------------------------------************-----------------------------------'''
        '''--------------**********--------------Cheetah jump-----------**********--------------'''
        '''--------------------------------------************-----------------------------------'''
        cast_bonus = {'evasion': 100}
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }
            result['target']['fall'] = {
                'this_time': self.stats['time'],
                'fall_time': 0.3,
            }
            return result

        Bull_run = person.classSkill.Skill(name='Bull run', cast=0.4, coldown=5, lvl=7, finish=finish, mult=0.2)
        self.skills.append(Bull_run)

        '''--------------------------------------************-----------------------------------'''
        '''--------------**********--------------Cheetah jump-----------**********--------------'''
        '''--------------------------------------************-----------------------------------'''
        cast_bonus = {'evasion': 100}
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }
            result['target']['fall'] = {
                'this_time': self.stats['time'],
                'fall_time': 0.3,
            }
            return result

        Bull_run = person.classSkill.Skill(name='Bull run', cast=0.4, coldown=5, lvl=7, finish=finish, mult=0.2)
        self.skills.append(Bull_run)

        '''-----------------------------------------******--------------------------------------'''
        '''--------------**********-----------------Cuwany--------------**********--------------'''
        '''-----------------------------------------******--------------------------------------'''
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }
            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }
            return result

        Cuwany = person.classSkill.Skill(name='Cuwany', cast=1, coldown=4, lvl=8, finish=finish, mult=1.5)
        self.skills.append(Cuwany)"""























