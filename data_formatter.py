

def parse_pgn(path):
    with open(path) as file:
        games = file.read().strip().split('\n\n\n')
        formatted_games = []

        for game in games:
            # Check if the game has a moves section
            if '\n\n' in game:
                moves_section = game.split('\n\n')[1]
                moves = moves_section.split(' ')
                # Filter out non-move elements
                moves_filtered = [move for move in moves if move and not move[0].isdigit(
                ) and '{' not in move and '}' not in move and '-' not in move]
                # Pair the moves
                paired_moves = [moves_filtered[i:i+2] for i in range(
                    0, len(moves_filtered), 2) if len(moves_filtered[i:i+2]) == 2]
                formatted_games.append(paired_moves)
            else:
                # Handle cases where there is no moves section
                formatted_games.append([])

    return formatted_games


# Correct file path
file_path = 'data/master_games.pgn'
formatted_games = parse_pgn(file_path)

# Display the paired moves of the first few games for verification
print(formatted_games[0])
