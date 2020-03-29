import berserk
import chess
import chess.engine
import screen_utils.field


def process_curent_game(session):
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("engine/stockfish")

    limit = chess.engine.Limit(time=2)
    local_opponents_last_move = None
    while True:
        try:
            cur_games = berserk.clients.Games(session).get_ongoing()
        except:
            continue

        if not cur_games:
            break
        else:
            cur_game = cur_games[0]

        if cur_game['isMyTurn']:
            remote_last_move = cur_game['lastMove']
            if not remote_last_move:
                my_move = engine.play(board, limit).move.uci()
                board.push_uci(my_move)
                screen_utils.field.move(my_move, cur_game['color'])
            elif remote_last_move != local_opponents_last_move:
                local_opponents_last_move = remote_last_move
                board.push_uci(remote_last_move)
                my_move = engine.play(board, limit).move.uci()
                board.push_uci(my_move)
                screen_utils.field.move(my_move, cur_game['color'])

    engine.quit()


def main():
    with open('resources/.token') as f:
        token = f.read()
        f.close()

    session = berserk.TokenSession(token)
    process_curent_game(session)


if __name__ == '__main__':
    main()
