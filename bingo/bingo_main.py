import robot_control as rc


def bingo():
    sirei = [['go_ahead', 'color_yellow'], 'nasi', ['go_ahead', 'jump_left'], ['go_ahead', 'color_blue'], 'front_right', 'hidari', ['go_ahead', 'color_red'], 'has_block', 'hanten', ['go_ahead', 'color_blue'], 'front_right', 'hanten', ['go_ahead', 'color_red'], 'migi', ['go_ahead', 'color_red'], 'hidari', ['go_ahead', 'color_red'], 'has_block', 'turn_left', 'front_left', 'hidari', ['go_ahead', 'color_red'], 'nasi', ['go_ahead', 'color_blue'], 'has_block', 'turn_right', 'front_left', 'nasi', ['go_ahead', 'color_blue'], 'nasi', ['go_ahead', 'color_green'], 'has_block', 'hanten', ['go_ahead', 'color_blue'], 'front_right', 'migi', ['go_ahead', 'color_blue'], 'has_block', 'migi', ['go_ahead', 'color_green'], 'front_right', 'migi', ['go_ahead', 'color_green'], 'nasi', ['go_ahead', 'color_yellow'], 'hidari', ['go_ahead', 'color_yellow'], 'has_block', 'turn_right', 'front_right', 'nasi', ['go_ahead', 'color_green'], 'nasi', ['go_ahead', 'color_green'], 'has_block', 'hanten', ['go_ahead', 'color_green'], 'nasi', ['go_ahead', 'color_yellow'], 'front_right', 'migi', ['go_ahead', 'color_yellow'], 'migi', ['go_ahead', 'color_green'], 'nasi', ['go_ahead', 'color_green']]
    has_block = True
    for i in sirei:
        print(i)
        """if i == "kuro_hidari":
            rc.kuro_hidari()
        elif i == "kuro_migi":
            rc.kuro_migi()
        elif i == "kuro_turn_hidari":
            rc.kuro_turn_hidari()
        elif i == "kuro_turn_migi":
            rc.kuro_turn_migi()"""
        if i == "turn_left":
            rc.turn_left()
        elif i == "turn_right":
            rc.turn_right()
        elif i == "hanten":
            rc.turn(has_block)
        elif i == "front_left":
            rc.front_left2()
            has_block = False
        elif i == "front_right":
            rc.front_right2()
            has_block = False
        """if i[0] == 'black_block':
            rc.black_block(i[1])"""
        if i == "hidari":
            rc.turn_left()
        elif i == "migi":
            rc.turn_right()
        if i[1] == "color_yellow":
            rc.trace(4)
            print("yell")
        elif i[1] == "color_red":
            rc.trace(5)
            print("red")
        elif i[1] == "color_blue":
            rc.trace(2)
            print("blue")
        elif i[1] == "color_green":
            rc.trace(3)
            print("gr")
        if i == "nasi":
            rc.nasi()
        if i == "has_block":
            has_block = True
        if i[1] == "jump":
            rc.jump()
        elif i[1] == "jump_left":
            rc.jump_left()
        elif i[1] == "jump_right":
            rc.jump_right()
        if i == "front_left_jump":
            rc.front_left_jump()
        elif i == "front_right_jump":
            rc.front_right_jump()


if __name__ == "__main__":
    bingo()
