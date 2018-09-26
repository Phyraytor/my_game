import mag
import knight

Percon_one = mag.Mag("Mag")
Percon_two = knight.Knight("Knight")
Percon_one.lvlup(10)
Percon_two.lvlup(10)
Percon_one.print()
Percon_two.print()

while Percon_one.live() and Percon_two.live():
    if Percon_two.time() <= Percon_one.time():
        Percon_two.get_enemy_skill( Percon_one.get_enemy_skill( Percon_two.activate() ) )
        print(Percon_two.name, "time = ", round(Percon_two.time(), 2))
    else:
        Percon_one.get_enemy_skill( Percon_two.get_enemy_skill( Percon_one.activate() ) )
        print(Percon_one.name, "time = ", round(Percon_one.time(), 2))


if Percon_one.live():
    print(Percon_one.name, "WIN!")
elif Percon_two.live():
    print(Percon_two.name, "WIN!")
else:
    print("DRAW!")

Percon_one.print()
Percon_two.print()

