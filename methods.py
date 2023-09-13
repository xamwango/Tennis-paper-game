# methods to be used/applied within the game:


def ball_position(player1s_draw, player2s_draw, b_t):
    if player1s_draw > player2s_draw:
        if b_t >= 0:
            b_t += 1
        else:
            b_t = 1
    elif player2s_draw > player1s_draw:
        if b_t <= 0:
            b_t -= 1
        else:
            b_t = -1
    else:
        b_t = b_t
    return b_t


class WinningDecision:
    def by_position(self, b_t):
        win_outcome = ""
        if b_t < -2:
            print("Player2 wins game")
            win_outcome = "player2"
        elif b_t > 2:
            print("Player1 wins game")
            win_outcome = "player1"

    def by_points(self, b_t):
        win_outcome = ""
        if b_t > 0:
            print("Player1 wins game")
            win_outcome = "player1"
        elif b_t < 0:
            print("Player2 wins game")
            win_outcome = "player2"
        else:
            print("Game ends as a draw")
            win_outcome = "draw"
