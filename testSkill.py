import skill

def myStart() -> dict:
    return {}

def myFinish(damage: float) -> dict:
    result = {}
    result['self'] = {'category': 'bonus',
                      'name': 'Insight',
                      'time': 9,
                      'mult_damage': 0.02}
    result['target'] = {'category': 'hit',
                        'name': 'fire',
                        'type': 'magic',
                        'damage': damage}
    return result

mySkill = skill.Skill(name='fire', cast=0.5, coldown=0, start=myStart, finish=myFinish, mult=0.2)


time = 0
while time < 1:
    print(mySkill.active)
    if not mySkill.active:
        print( mySkill.start(time) )
        time += mySkill.cast
    else:
        print( mySkill.finish(1) )