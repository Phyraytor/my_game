import classSkill


''' Create Magic Arrow'''
cast_bonus = {}
def finish(name: str, damage: float) -> dict:
    def kill_shield(damage: float) -> dict:
        result = {'target': {}}
        result['target']['hit'] = {'name': 'frost shiled',
                                           'type': 'magic',
                                           'damage': damage}
        return result

        def end_shield(hil: float) -> dict:
            result = {'self': {}}
            result['self']['hil'] = hil
            return result

        result = {'target': {}, 'self': [] }

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
        })

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
        result['target']['curse'] = {
            'name': 'minus defense',
            'time' : 3,
            'defense': 100,
        }

        return result

magic_arrow = classSkill.Skill(name='Magic arrow', cast=0.5, coldown=0, bonus=cast_bonus, finish=finish, mult=0.2)