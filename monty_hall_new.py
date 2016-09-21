#monty hall dillema
import random

class Door:
    def __init__(self):
        self.behind_door = 'Empty'
        self.player_pick = False
        self.reveal = False

def monty_hall_test(trials):
    switch_wins = 0
    switch_losses = 0
    stay_wins = 0
    stay_losses = 0

    while trials > 0:

        random_number = random.randint(1,3)



        door_1 = Door()
        door_2 = Door()
        door_3 = Door()

        if random_number == 1:
            door_1.behind_door = 'Car'
            door_2.behind_door = 'Goat'
            door_3.behind_door = 'Goat'
        elif random_number == 2:
            door_1.behind_door = 'Goat'
            door_2.behind_door = 'Car'
            door_3.behind_door = 'Goat'
        else:
            door_1.behind_door = 'Goat'
            door_2.behind_door = 'Goat'
            door_3.behind_door = 'Car'

        player_pick = random.randint(1,3)

        if player_pick == 1:
            door_1.player_pick = True
        elif player_pick == 2:
            door_2.player_pick = True
        else:
            door_3.player_pick = True

        #reveal

        door_list = [door_1, door_2, door_3]

        two_doors = []

        for door in door_list:
            if door.player_pick == False:
                two_doors.append(door)

        goat_count =0
        for door in two_doors:
            if door.behind_door == 'Goat':
                goat_count += 1

        if goat_count == 1:
            for door in two_doors:
                if door.behind_door == 'Goat':
                    door.reveal = True

        elif goat_count == 2:
            random_door_reveal = random.randint(1,2)
            if random_door_reveal == 1:
                two_doors[0].reveal = True
            else:
                two_doors[1].reveal = True

        # print(door_1.reveal)
        # print(door_2.reveal)
        # print(door_3.reveal)

        #switch or stay

        switch_or_stay = random.randint(1,2)
        #switch is 1, stay is 2

        #switch

        if switch_or_stay == 1:
            for door in door_list:
                if door.reveal == False and door.player_pick == False:
                    door.player_pick = True
                    continue

                elif door.player_pick == True:
                    door.player_pick = False

        # test

        for door in door_list:
            if switch_or_stay == 1:

                if door.player_pick == True and door.behind_door == 'Car':
                    # print('You win the car!!!!!')
                    switch_wins += 1

                elif door.player_pick == True and door.behind_door == 'Goat':
                    # print('Sorry, you Lose')
                    switch_losses += 1
            if switch_or_stay == 2:
                if door.player_pick == True and door.behind_door == 'Car':
                    # print('You win the car!!!!!')
                    stay_wins += 1

                elif door.player_pick == True and door.behind_door == 'Goat':
                    # print('Sorry, you Lose')
                    stay_losses += 1





        # print(door_1.player_pick, door_1.behind_door, door_1.reveal)
        # print(door_2.player_pick, door_2.behind_door, door_2.reveal)
        # print(door_3.player_pick, door_3.behind_door, door_3.reveal)

        trials -= 1
    print('Stay Wins:', stay_wins,'Stay Losses:', stay_losses)
    print('Switch win:', switch_wins,'Switch Losses:', switch_losses)
    print('Stay Win Percent', stay_wins/(stay_losses + stay_wins))
    print('Switch Loss Percent', switch_wins/(switch_losses + switch_wins))

monty_hall_test(2000)
