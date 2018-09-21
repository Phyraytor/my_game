import mag
import knight

Knight = knight.Knight("Knight")
Mag = mag.Mag("Mag")

Mag.print()
Knight.print()

while Mag.live() and Knight.live():
    if Knight.time() <= Mag.time():
        #print( round( Knight.time(), 2) )
        Knight.get_enemy_skill( Mag.get_enemy_skill( Knight.activate() ) )

    else:
        #print( round(Mag.time(), 2) )
        Mag.get_enemy_skill( Knight.get_enemy_skill( Mag.activate() ) )


if Mag.live():
    print("Mag WIN!")
elif Knight.live():
    print("Knight WIN!")
else:
    print("DRAW!")

Mag.print()
Knight.print()

