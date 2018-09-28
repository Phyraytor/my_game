import heapTime
import classSkill
import random

class Person:
    """Шаблон всех персонажей"""

    """private method"""
    @staticmethod
    def block_resist(block: int) -> float:
        if block > 100: block = 100
        if block < 0: block = 0
        return (100 - block) / 100

    @staticmethod
    def resist(defense: int) -> float:
        """Переводит защиту из числа в коэффииент (резист)"""
        if defense <= 0: return 1
        K = 1000.0 # Коэффициент размерности защиты
        return K / (defense + K)

    def spray_damage(self) -> float:
        ACCURACY = 100.0  # Кол-во знаков после запятой
        INTERVAL = 2.5
        return random.randint(0, self.stats['damage'] * ACCURACY) / (ACCURACY * INTERVAL)

    def chance_krit(self) -> int:
        K = 1000.0
        #print(self.name, "chanse krit =", round( K * (1 - K / (self.stats['chance_krit'] + K) ) / 10 ), "%" )
        return round( K * (1 - K / (self.stats['chance_krit'] + K) ) / 10 )

    @staticmethod
    def krit_damage(x:int) -> float:
        return (4 * (x ** 1.3) + 2 * x + 0.5) / ((x ** 1.3) + 9 * x + 1)

    def krit_strike(self) -> int:
        mult_damage = 1
        if random.randint(0, 100) <= self.chance_krit():
            print('Krit!')
            self.events['krit'] = True
            mult_damage += self.krit_damage( self.stats['damage_krit'] )
        return mult_damage

    def chance_evasion(self, precision: int) -> int:
        K = 21.0 #Коэффициент размерности уворота
        #print(self.name, "chanse evasion =", round(K * self.stats['evasion'] / ( (K + self.stats['evasion'] + (K + precision) ) ) / 3 ), "%")
        return round(K * self.stats['evasion'] / ( (K + self.stats['evasion'] + (K + precision) ) ) / 3)

    def evasion(self, precision: int) -> bool:
        return random.randint(0, 100) <= self.chance_evasion(precision)

    """public method"""
    def __init__(self, name: str) -> None:

        self.name = name
        self.lvl = 0
        self.exp = 0
        self.exp_to_lvl = 100
        self.cast = False
        self.skills = []
        self.active = True
        self.events = {}
        self.shield = {}
        #Stats - изменяемые другими персонажами характеристики
        self.stats = {
            'name': 'stats',
            'category': 'skills',
            'time': 0,
            'mult_damage': 1,
            'speed_cast': 1.0,
            'front_block': 0,
            'back_block': 0,
            'bonus_hil': 1
        }
        self.times = heapTime.HeapTime()  # Порядок выполнения действий
        self.times.add(self.stats)
        self.SPECIAL_KEY = ('type', 'time', 'name', 'category')
        self.LVL_STATS = ('defense', 'resistance', 'damage', 'chance_krit', 'precision', 'evasion')

    def lvlup(self, lvl:int=1) -> None:
        for i in range(lvl):
            print(self.name, "LVL UP!!!")
            self.exp_to_lvl *= 1.8
            self.lvl += 1
            for key_stat in self.LVL_STATS:
                self.stats[key_stat] = round(self.stats[key_stat] * 1.1)

            for skill in self.skills:
                skill.coldown = round(skill.coldown * 1.1, 1)
                #print(skill.name, skill.coldown)

            self.max_hitpoint = round(self.max_hitpoint * 1.1)
            self.stats['hitpoint'] = self.max_hitpoint

    def get_exp(self, amount_exp):
        self.exp += amount_exp
        while self.exp >= self.exp_to_lvl:
            self.exp -= self.exp_to_lvl
            self.lvlup()

    def live(self) -> bool:
        if not self.stats['hitpoint'] > 0: self.events['die'] = True
        return self.stats['hitpoint'] > 0

    def attack(self) -> float:
        BONUS = self.spray_damage() - self.spray_damage()
        self.events['attack'] = True
        return (self.stats['damage'] + BONUS) * self.stats['mult_damage'] * self.krit_strike()

    def create_shield(self, shield: dict) -> None:
        if self.shield != {}: return
        print(self.name, 'create shield', shield['name'])
        shield['time'] += self.stats['time']
        self.shield = heapTime.copy.copy(shield)
        self.times.add(shield)

    def shield_resist(self, damage: float) -> float:
        result = damage * (100 - self.shield['resist']) / 100
        self.shield['hitpoint'] -= result
        return result

    def die_shield(self) -> object:
        if self.shield['hitpoint'] > 0: return
        print(self.shield['name'], "die")
        result =  self.open_result( self.shield['die']( self.shield['hitpoint'] ))
        self.shield = {}
        return result

    def remove_shield(self) -> object:
        print(self.shield['name'], "the end")
        result =  self.open_result( self.shield['end']( self.shield['hitpoint'] ) )
        self.shield = {}
        return result

    def get_hitpoint(self, get_hil: dict) -> None:
        self.events['get_hitpoint'] = True
        self.stats['hitpoint'] += round(get_hil['damage'] * self.stats['bonus_hil'])
        if self.stats['hitpoint'] > self.max_hitpoint:
            self.stats['hitpoint'] = self.max_hitpoint
        print(self.name, 'hitpoint =', self.stats['hitpoint'])

    def lose_hitpoint(self, get_hit: dict) -> None:
        result = None
        self.events['lose_hitpoint'] = True
        if get_hit['type'] == 'physical':type_defense = 'defense'
        else:type_defense = 'resistance'

        block = 'front_block'
        if 'side' in get_hit:
            block = 'back_block'
            get_hit['damage'] *= 1.5

        final_damage = get_hit['damage'] * self.resist(self.stats[type_defense])
        #ignoring_block...
        if 'ignor_block' in get_hit:
            final_damage *= self.block_resist(self.stats[block] - get_hit['ignor_block'])
            print("Ignoring block", get_hit['ignor_block'])
        else:
            final_damage *= self.block_resist(self.stats[block])

        if self.shield != {}:
            print("Shield! Damage was ", round(final_damage) )
            final_damage = self.shield_resist(final_damage)
            result = self.die_shield()
        final_damage = round(final_damage)
        #print("resist = ", round(1 - self.resist( self.stats[type_defense]), 2) )

        print(self.name, 'get damage', final_damage)
        self.stats['hitpoint'] -= final_damage
        print(self.name, 'hitpoint =', round(self.stats['hitpoint'], 2))
        return result

    def time(self) -> float:
        return self.times.first()['time']

    def create_dot(self, dot: dict) -> None:
        dot['time'] += self.stats['time']
        dot['ignor_block'] = 100
        dot['category'] = 'dot'
        self.times.add(dot)

    def activate_dot(self, dot: dict) -> None:
        dot['stage'] -= 1
        print(dot['name'], "stage lost", dot['stage'])
        if dot['type']=='hil':self.get_hitpoint(dot)
        else:self.lose_hitpoint(dot)
        if dot['stage'] > 0:self.create_dot(dot)

    def create_bonus(self, bonus: dict, effect:str='bonus') -> None:
        print(self.name, 'get', effect, bonus['name'])
        bonus['time'] += self.stats['time']
        bonus['type'] = effect
        bonus['category'] = 'bonus'

        for key in bonus:
            if not key in self.SPECIAL_KEY:
                if effect == 'curse':
                    # Если это проклятие, то статы становятся отрицательными
                    bonus[key] = -bonus[key]
                self.stats[key] += bonus[key]
        self.times.add(bonus)

    def remove_bonus(self, bonus: dict) -> None:
        print(self.name, 'lose bonus', bonus['name'])
        for key, value in bonus.items():
            if not key in self.SPECIAL_KEY:
                self.stats[key] -= value

    def cast_bonus(self, bonus: dict, end: bool=False) -> None:

        for key, value in bonus.items():
            if end: value = -value
            if not key in self.SPECIAL_KEY:
                self.stats[key] += value

    def daze(self, daze_time: float) -> None:
        print(self.name, "was time", round(self.stats['time'], 2) )
        self.stats['time'] += daze_time
        #print("became time", self.stats['time'])
        self.times.change('stats', {'time': self.stats['time']} )

    def stop_cast(self, this_time: float) -> None:
        if self.cast:
            self.cast = False
            for skill in self.skills:
                if skill.active:
                    skill.repeat = 0
                    finish = skill.finish(this_time)
                    skill.repeat = skill.start_repeat
                    #Наверное, стоило как-то поменять метод open_result, но пока и так сойдёт
                    #Дублирование кода ведёт к дублированию багов!
                    if 'end' in finish:
                        self.cast_bonus(finish['end'], end=True)

                    self.stats['time'] = this_time
                    self.times.change('stats', {'time': self.stats['time']})
                    print(self.name, "stop cast", skill.name)
                    break

    def fall(self, this_time:float, fall_time: float) -> None:
        self.stop_cast(this_time)
        self.daze(fall_time)

    def open_result(self, result: dict, skill: object={}) -> dict:

        if 'self' in result:
            for arg_skill in result['self']:
                func = arg_skill['func']
                del arg_skill['func']
                func(arg_skill)

        if 'end' in result:
            self.cast_bonus(result['end'], end=True)

        if 'target' in result:
            result['target']['precision'] = self.stats['precision']
            return result['target']


    def start_skill(self, skill: object) -> None:
        self.cast = True
        print(self.name, 'cast', skill.name)

        self.cast_bonus( skill.start() ) #Здесь БАГ!!! Вроде исправил
        #print("DEBUG_TIME = ", self.stats['time'])
        self.stats['time'] += round(skill.cast * self.stats['speed_cast'], 2) #Тут всё в норме, ошибка в выводе времени
        #print("DEBUG = ", skill.cast * self.stats['speed_cast'] )
        #print("DEBUG_TIME = ", self.stats['time'])
        self.times.add(self.stats)

    def finish_skill(self, skill: object) -> dict:
        self.cast = False
        print(self.name, 'activate', skill.name)
        self.times.add(self.stats)
        result = skill.finish(self.stats['time'], self.attack() )

        if skill.repeat > 0:
            skill.repeat -= 1
            self.times.pop() #Исправить эту фигню. Перенести добавление в heap в else
            # я пока не готов к новым багам, потому отложил на потом
            self.start_skill(skill)
        else:
            skill.repeat = skill.start_repeat
        return self.open_result(result, skill)

    def activate_skill(self) -> dict:
        """Если конец активации"""
        if self.cast:
            #for skill in self.skills:
               #print("DEBUG = ", skill.name, skill.active)

            for skill in self.skills:
                if skill.active:
                    return self.finish_skill(skill)


        if len(self.skills) == 1: return self.start_skill(self.skills[0])
        # Поиск активных скилов

        active_skills = []
        for skill in self.skills[1:]:
            if skill.time_active <= self.stats['time'] and skill.lvl <= self.lvl:
                active_skills.append(skill)

        #Активируем случайный из них
        if active_skills != []:
            myIndex = random.randint(0, len(active_skills) - 1)
            skill = active_skills[myIndex]

            return self.start_skill(skill)

        #Если все скилы в откате - автоатака
        return self.start_skill(self.skills[0])

    def activate(self) -> dict:
        step = self.times.pop()
        print('---------------')
        if step['category'] == 'skills': return self.activate_skill()
        if step['category'] == 'bonus':  return self.remove_bonus(step)
        if step['category'] == 'dot':    return self.activate_dot(step)
        if step['category'] == 'shield': return self.remove_shield()
        self.events = {}

    def get_enemy_skill(self, enemy: dict) -> None:
        if not enemy: return

        if self.evasion(enemy['precision']):
            print(self.name, 'Evalation!')
            self.events['evasion'] = True
            return

        if 'hit' in enemy:
            self.lose_hitpoint(enemy['hit'])
        if 'curse' in enemy:
            self.create_bonus(enemy['curse'], effect='curse')
        if 'dot' in enemy:
            self.create_dot(enemy['dot'])
        if 'daze' in enemy:
            self.daze(enemy['daze'])
        if 'stop' in enemy:
            self.stop_cast(enemy['stop'])
        if 'fall' in enemy:
            self.fall(enemy['fall']['this_time'], enemy['fall']['fall_time'])

        self.events = {}

    def print(self) -> None:
        print(self.name)
        for key, value in self.stats.items():
            print(key,'=', value)
        print('-' * 13)

    def debug_hp(self):
        return str(self.stats['hitpoint'])
