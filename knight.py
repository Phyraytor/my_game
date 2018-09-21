import person

class Knight(person.Person):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.max_hitpoint = 2000
        self.stats['defense'] = 1500
        self.stats['resistance'] = 500
        self.stats['damage'] = 250
        self.stats['hitpoint'] = self.max_hitpoint
        self.stats['chance_krit'] = 47
        self.stats['precision'] = 10
        self.stats['evasion'] = 60


        '''-------------------------------------**********--------------------------------------'''
        '''--------------**********-------------Faster axe--------------**********--------------'''
        '''-------------------------------------**********--------------------------------------'''
        '''cast_bonus = {'front_block' : 5}'''
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': [] }

            '''result['self'].append({
                'func': self.create_dot,
                'name': 'bandages',
                'type': 'hil',
                'damage': damage * 0.1,
                'stage': 4,
                'time': 0.9,
            })'''

            result['target']['hit'] = {
                'name': name,
                'type': 'physical',
                'damage': damage,
            }

            '''result['target']['dot'] = {
                'name': 'bleeding',
                'type': 'physical',
                'damage': damage * 0.2,
                'stage': 3,
                'time': 0.7,
            }'''
            #result['target']['stop'] = self.stats['time']
            return result

        skill = person.classSkill.Skill(name='Faster axe', cast=0.4, coldown=0, bonus={}, finish=finish, mult=0.2)
        self.skills.append(skill)
