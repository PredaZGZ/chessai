from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Board import Board
from Translator import *

app = FastAPI()
board = Board()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


board.fillNaturalBoard()


@app.get("/")
async def read_board():
    return {"board": board.getBoard()}


@app.post("/make-move")
async def make_move(starting_square: str, ending_square: str):
    if board.isEmpty(starting_square):
        return {"message": "Starting square is empty"}
    elif (len(board.moves) == 0) or (board.moves[-1][0] != board.isWhite(starting_square)):
        moves = board.getMovesOfPiece(starting_square)
        if ending_square not in moves:
            return {"message": "Invalid move"}
        board.move(starting_square, ending_square)
        return {"message": "OK", "board": board.getBoard()}
    else:
        return {"message": "It's not your piece"}


@app.get("/moves")
async def get_moves():
    return {"moves": board.moves}


@app.get("/reset")
async def reset():
    board.fillNaturalBoard()
    return {"board": board.getBoard()}


@app.get("/possible-moves")
async def possible_moves(square: str):
    moves = board.getMovesOfPiece(square)
    return {"possible_moves": moves, "board": board.getBoardOfMoves(moves)}


@app.post("/random-move")
async def random_move(color: str):
    moves = board.makeRandomMove(color)
    board.move(moves[0], moves[1])
    return {"sq1": moves[0], "sq2": moves[1], "board": board.getBoard()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=4002, reload=True)
