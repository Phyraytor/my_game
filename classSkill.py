class Skill:

    def __init__(self, name: str,  cast: float, coldown: float,
                 finish, lvl, bonus: dict={}, mult: float=0, repeat:int=0) -> None:
        self.name = name
        self.mult = mult
        self.cast = cast
        self.coldown = coldown
        self.time_active = 0
        self.active = False
        self.start_repeat = repeat
        self.repeat = repeat
        self.bonus = bonus
        self.finish_effect = finish
        self.lvl = lvl

    def get_time(self) -> float:
        return self.time_active

    def start(self) -> dict:
        self.active = True
        result = self.bonus
        result['time'] = self.cast
        return result

    def finish(self, time: float, my_damage: float=0) -> dict:
        self.active = False
        if not self.repeat:
            self.time_active = self.coldown + time
            print(self.name, "time active", round(self.time_active, 2) )
        result = {}
        result = self.finish_effect(self.name, my_damage * self.mult)
        result['end'] = self.bonus
        return result

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name