# The following program implements the Tennis paper game
from methods import ball_position, WinningDecision

initial_points = int(input("Enter the initial number of points you want to play for: "))
player1_points = initial_points
player2_points = initial_points
B_t = 0  # ball position at time t
t = 0  # shows time/period/round
WinningOutcome = ""

while B_t > -3 and B_t < 3:
    player1s_draw = int(input("Player1 make draw for the round: "))
    while player1s_draw < 0:
        print("Enter the valid number of point(s).")
        player1s_draw = int(input("Player1 make draw again for the round: "))
    else:
        while player1_points < player1s_draw:
            if player1_points == 0:
                print("No point(s) left, you get zero points by default.")
                player1s_draw = 0
                break
            else:
                print("Enter the valid number of point(s).")
                player1s_draw = int(input("Player1 make draw again for the round: "))
                while player1s_draw < 0:
                    print("Enter the valid number of point(s).")
                    player1s_draw = int(input("Player1 make draw again for the round: "))
    player2s_draw = int(input("Player2 make draw for the round: "))
    while player2s_draw < 0:
        print("Enter the valid number of point(s).")
        player2s_draw = int(input("Player2 make draw again for the round: "))
    else:
        while player2_points < player2s_draw:
            if player2_points == 0:
                print("No point(s) left, you get zero points by default.")
                player2s_draw = 0
                break
            else:
                print("Enter the valid number of point(s).")
                player2s_draw = int(input("Player2 make draw again for the round: "))
                while player2s_draw < 0:
                    print("Enter the valid number of point(s).")
                    player2s_draw = int(input("Player2 make draw again for the round: "))
    B_t = ball_position(player1s_draw, player2s_draw, B_t)
    t += 1
    print(f"The ball is in position {B_t} of the field at time {t}.")
    player1_points -= player1s_draw
    player2_points -= player2s_draw
    if player1_points == 0 and player2_points ==0:
        winning_player = WinningDecision()
        winning_player.by_points(B_t)
        break
winning_player = WinningDecision()
winning_player.by_position(B_t)
