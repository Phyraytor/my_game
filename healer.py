import person

class Healer(person.Person):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.max_hitpoint = 2400
        self.stats['defense'] = 500
        self.stats['resistance'] = 1600
        self.stats['damage'] = 400
        self.stats['hitpoint'] = self.max_hitpoint
        self.stats['chance_krit'] = 49
        self.stats['damage_krit'] = 9
        self.stats['precision'] = 10
        self.stats['evasion'] = 20

        '''----------------------------------------******---------------------------------------'''
        '''--------------**********----------------Prayer----------------**********-------------'''
        '''----------------------------------------******---------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            
            result = {'target': {}, 'self': []}

            '''result['self'].append({
                'func': self.get_hitpoint,
                'name': 'my hill',
                'damage': damage,
            })'''

            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            } #Для теста

            return result

        Prayer = person.classSkill.Skill(name='Prayer', cast=0.5, coldown=0, lvl=0, finish=finish, mult=0.2)
        self.skills.append(Prayer)
"""
        '''------------------------------------------*****------------------------------------'''
        '''--------------**********------------------Flash-------------**********-------------'''
        '''------------------------------------------*****------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['stop'] = self.stats['time']
            return result

        Flash = person.classSkill.Skill(name='Flash', cast=0.3, coldown=3, lvl=1, finish=finish, mult=0)
        self.skills.append(Flash)

        '''----------------------------------------**************-------------------------------------'''
        '''--------------**********----------------Сleansing soul--------------**********-------------'''
        '''----------------------------------------**************-------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}

            result['target']['dot'] = {
                'name': 'Сleansing soul',
                'type': 'magic',
                'damage': damage,
                'stage': 4,
                'time': 0.8,
            }
            return result

        Сleansing_soul = person.classSkill.Skill(name='Сleansing soul', cast=0.7, coldown=4, lvl=2, finish=finish, mult=0.45)
        self.skills.append(Сleansing_soul)

        '''---------------------------------------------*****---------------------------------------'''
        '''--------------**********---------------------Shock----------------**********-------------'''
        '''---------------------------------------------*****---------------------------------------'''
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }
            result['target']['fall'] = {
                'this_time': self.stats['time'],
                'fall_time': 1.2,
            }
            return result

        Shock = person.classSkill.Skill(name='Shock', cast=1.2, coldown=5, lvl=3, finish=finish, mult=0.7)

        self.skills.append(Shock)

        '''--------------------------------------************------------------------------------'''
        '''--------------**********--------------Сolumn light-------------**********-------------'''
        '''--------------------------------------************------------------------------------'''
        cast_bonus = {'evasion': 100}  
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['self'].append({
                'func': self.get_hitpoint,
                'name': 'my hill',
                'damage': damage,
            })
            return result

        Сolumn_light = person.classSkill.Skill(name='Сolumn light', cast=1, coldown=5, lvl=4, finish=finish, mult=1)

        self.skills.append(Сolumn_light)

        '''--------------------------------------************-----------------------------------'''
        '''--------------**********--------------Purification------------**********-------------'''
        '''--------------------------------------************-----------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            '''result['self'].append({
                'func': self.times.delete('dot'),
                'name': 'Purification',
                'damage': damage,
            })'''
            return result

        Purification = person.classSkill.Skill(name='Purification', cast=1, coldown=5, lvl=4, finish=finish, mult=0)

        self.skills.append(Purification)

        '''----------------------------------------*******--------------------------------------'''
        '''--------------**********----------------Justice---------------**********-------------'''
        '''----------------------------------------*******--------------------------------------'''


        #Этот скил я тоже ещё не предусмотрел
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }
            return result

        Justice = person.classSkill.Skill(name='Justice', cast=1.2, coldown=5, lvl=3, finish=finish, mult=1.7)

        self.skills.append(Justice)

        '''--------------------------------------***********----------------------------------'''
        '''--------------**********--------------Angel wings-----------**********-------------'''
        '''--------------------------------------***********----------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['self'].append({
                'func': self.create_bonus,
                'name': 'Angel wings',
                'time': 7 * (1 + self.lvl / 10),
                'bonus_hil': 0.01 * self.lvl,
                'back_block': 100,
            })
            return result

        Angel_wings = person.classSkill.Skill(name='Angel wings', cast=0.35, coldown=9, lvl=7, finish=finish, mult=0)
        self.skills.append(Angel_wings)

        '''-------------------------------------***********-----------------------------------'''
        '''--------------**********-------------Benediction------------**********-------------'''
        '''-------------------------------------***********-----------------------------------'''
        
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['self'].append({
                'func': self.get_hitpoint,
                'name': 'Benediction',
                'damage': damage,
            })
            result['self'].append({
                'func': self.create_bonus,
                'name': 'Benediction',
                'time': 4 * (1 + self.lvl / 10),
                'evasion': 30 * self.lvl,
            })

            if person.random.randint(0, 20) < 5: result['self'][-1]['defense'] = 100 * self.lvl
            if person.random.randint(0, 20) < 5: result['self'][-1]['resistance'] = 100 * self.lvl
            if person.random.randint(0, 20) < 5: result['self'][-1]['damage'] = 100 * self.lvl
            if person.random.randint(0, 20) < 5: result['self'][-1]['precision'] = 100 * self.lvl
            return result

        Benediction = person.classSkill.Skill(name='Benediction', cast=0.9, coldown=4, lvl=8, finish=finish, mult=0.7)
        self.skills.append(Benediction)"""























