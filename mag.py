import person

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
        self.stats['evasion'] = 20

        '''-------------------------------------***********-------------------------------------'''
        '''--------------**********-------------Magic Arrow--------------**********-------------'''
        '''-------------------------------------***********-------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            '''def kill_shield(damage: float) -> dict:
                result = {'target': {}}
                result['target']['hit'] = {
                    'name': 'frost shiled',
                    'type': 'magic',
                    'damage': damage
                }
                return result

            def end_shield(hil: float) -> dict:
                result = {'self': {}}
                result['self']['hil'] = hil
                return result
            '''
            result = {'target': {}, 'self': []}

            '''
            result['self'].append({
                'func': self.create_shield,
                'name': 'frost shiled',
                'hitpoint': self.stats['damage'],
                'resist': 20,
                'time': 10,
                'die': kill_shield,
                'end': end_shield,
            })

            result['self'].append({
                'func': self.get_hitpoint,
                'name': 'my hill',
                'damage': damage * 0.1,
            })'''

            result['self'].append({
                'func': self.create_bonus,
                'name': 'Insight',
                'time': 5,
                'mult_damage': 0.02,
            })

            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }

            '''result['target']['curse'] = {
                'name': 'minus defense',
                'time': 3,
                'defense': 100,
            }'''

            return result

        magic_arrow = person.classSkill.Skill(name='Magic arrow', cast=0.5, coldown=0, bonus={}, finish=finish, mult=0.2)
        self.skills.append(magic_arrow)

        '''--------------------------------------*********------------------------------------'''
        '''--------------**********--------------Fire ball-------------**********-------------'''
        '''--------------------------------------*********------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }
            result['target']['dot'] = {
                'name': 'Combustion',
                'type': 'magic',
                'damage': damage * 0.25,
                'stage': 2,
                'time': 1.4,
            }
            return result

        fire_ball = person.classSkill.Skill(name='Fire ball', cast=1.1, coldown=2.25, bonus={}, finish=finish, mult=0.85)
        self.skills.append(fire_ball)

        '''----------------------------------------******-------------------------------------'''
        '''--------------**********----------------Cobble--------------**********-------------'''
        '''----------------------------------------******-------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }
            result['target']['fall'] = {
                'this_time': self.stats['time'],
                'fall_time': 0.2,
            }
            return result

        Cobble = person.classSkill.Skill(name='Cobble', cast=1.2, coldown=3, bonus={}, finish=finish, mult=0.7)
        self.skills.append(Cobble)


































