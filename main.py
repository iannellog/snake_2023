"""
Created on Sept. 29, 2023
by Giulio Iannello
"""

from snake import Snake
from play_field import Play_field

from json import load
import gestione_input as gi



def play(game_file: str) -> int:

    # Snake game

    # get layout and moves
    # with open(game_file, 'r') as file:
    #     game_info = load(file)
    #     file.close()
    # with open(game_info["field_in"], 'r') as file:
    #     field_info = load(file)
    #     file.close()
    start, mosse, food, blocks, righe, colonne, field_out = gi.carico_dati(game_file)
    game_info = {
        "start": start,
        "moves": mosse
    }
    field_info = {
        "rows": righe,
        "cols": colonne,
        "blocks": blocks,
        "food": food
    }

    # create snake object (including an empty initial tail)
    snake = Snake()
    # create play field object
    play_field = Play_field(field_info["rows"], field_info["cols"], field_info["blocks"], field_info["food"])
    # put snake in start position
    snake.place_in_start_position(game_info["start"], [field_info["rows"], field_info["cols"]])

    # start the game
    for m in game_info["moves"].split(' '):
        #    check if move is valid for play filed; if it is, return the new head position and if it contains food
        valid_move, new_head_position, food = play_field.check_move(snake.get_head_position(), m)
        if valid_move:
            # check if new position is valid for the snake, taking into account if it eats food
            valid_move = snake.check_move(new_head_position, food)
            if valid_move:
                # update play field
                play_field.update(new_head_position)
                # update snake (including its tail)
                snake.update(new_head_position, food)
        if not valid_move:
            break

    # return len(snake.body)
    lunghezza_serpente = gi.restituisco_dati(
        snake.body,
        snake.tail,
        play_field.food,
        play_field.obstacles,
        righe,
        colonne,
        field_out
    )
    # print(f"La lunghezza del serpente alla fine del gioco è: {lunghezza_serpente}")
    return lunghezza_serpente


if __name__ == "__main__":
    print('Snake body length: ', play('data/gamefile_02.json'))
    # display play field and snake (including its path)
    # print('moves:', game_info["moves"])
    # print('snake body:', snake.body)
    # print('snake tail:', snake.tail)
    print('End')
