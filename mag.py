import person

class Mag(person.Person):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.max_hitpoint = 2000
        self.stats['defense'] = 500
        self.stats['resistance'] = 1500
        self.stats['damage'] = 500
        self.stats['hitpoint'] = self.max_hitpoint
        self.stats['chance_krit'] = 79
        self.stats['damage_krit'] = 10
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


            '''result['self'].append({
                'func': self.create_bonus,
                'name': 'Insight',
                'time': 5,
                'mult_damage': 0.02,
            })'''

            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }



            return result

        magic_arrow = person.classSkill.Skill(name='Magic arrow', cast=1, coldown=0, lvl=0, finish=finish, mult=1)
        self.skills.append(magic_arrow)
    """
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

        fire_ball = person.classSkill.Skill(name='Fire ball', cast=1.1, coldown=2.25, lvl=1, finish=finish, mult=0.85)
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

        Cobble = person.classSkill.Skill(name='Cobble', cast=1.2, coldown=3, lvl=2, finish=finish, mult=0.7)
        self.skills.append(Cobble)

        '''---------------------------------------********------------------------------------'''
        '''--------------**********---------------Ice ring-------------**********-------------'''
        '''---------------------------------------********------------------------------------'''
        cast_bonus = {'front_block': 45, 'back_block': 45}
        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }
            result['target']['curse'] = {
                'name': 'frost',
                'time': 6,
                'speed_cast': -0.3,
                'chance_krit': 4,
                'evasion': 7
            }
            return result

        Ice_ring = person.classSkill.Skill(name='Ice ring', cast=1.4, coldown=4, lvl=3, finish=finish, mult=1.2, bonus=cast_bonus)

        self.skills.append(Ice_ring)

        '''--------------------------------------*********------------------------------------'''
        '''--------------**********--------------Lightning-------------**********-------------'''
        '''--------------------------------------*********------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }
            result['target']['curse'] = {
                'name': 'Lightning',
                'time': 6,
                'resistance': 0.35,
            }
            return result

        Lightning = person.classSkill.Skill(name='Lightning', cast=0.8, coldown=4, lvl=4, finish=finish, mult=1.3)

        self.skills.append(Lightning)

        '''----------------------------------------******-------------------------------------'''
        '''--------------**********----------------Meteor--------------**********-------------'''
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
                'fall_time': 2.2,
            }
            return result

        Meteor = person.classSkill.Skill(name='Meteor', cast=1.7, coldown=7, lvl=5, finish=finish, mult=2.3)
        self.skills.append(Meteor)

        '''--------------------------------------*********------------------------------------'''
        '''--------------**********--------------Ice arrow-------------**********-------------'''
        '''--------------------------------------*********------------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }
            result['target']['curse'] = {
                'name': 'frost',
                'time': 6,
                'speed_cast': -0.3,
                'chance_krit': 4,
                'evasion': 7
            }
            return result

        Ice_arrow = person.classSkill.Skill(name='Ice arrow', cast=1, coldown=3, lvl=6, finish=finish, mult=0.6)
        self.skills.append(Ice_arrow)

        '''------------------------------------**************---------------------------------'''
        '''--------------**********------------Mult lightning----------**********-------------'''
        '''------------------------------------**************---------------------------------'''

        def finish(name: str, damage: float) -> dict:
            result = {'target': {}, 'self': []}
            result['target']['hit'] = {
                'name': name,
                'type': 'magic',
                'damage': damage,
            }
            result['target']['dot'] = {
                'name': 'Lightning',
                'type': 'magic',
                'damage': damage * 0.2,
                'stage': 3,
                'time': 1.7,
            }
            return result

        Mult_lightning = person.classSkill.Skill(name='Mult lightning', cast=0.15, coldown=6, lvl=7, finish=finish, mult=0.1, repeat=7)
        self.skills.append(Mult_lightning)

        '''--------------------------------------*********------------------------------------'''
        '''--------------**********--------------Fire wall-------------**********-------------'''
        '''--------------------------------------*********------------------------------------'''
        cast_bonus = {'front_block': 25}
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

        Fire_wall = person.classSkill.Skill(name='Fire wall', cast=0.9, coldown=3.5, lvl=8, finish=finish, mult=0.7, bonus=cast_bonus)
        self.skills.append(Fire_wall)"""























