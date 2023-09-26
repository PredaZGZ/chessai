import { useEffect, useState } from "react";
import a from "./Translator";

export default function Chessboard() {
  const [board, setBoard] = useState([]);
  const [possibleMoves, setPossibleMoves] = useState([]);
  const [selectedPiece, setSelectedPiece] = useState(null);
  const [randomMove, setRandomMove] = useState(true);
  const [turn, setTurn] = useState("white");

  useEffect(() => {
    fetch("http://localhost:4002/", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((res) => {
        setBoard(res.board);
      })
      .catch((err) => console.log(err));
  }, [turn]);

  const notify = (noti) => {
    console.log(noti);
  };

  const getPossibleMoves = (square) => {
    fetch(`http://localhost:4002/possible-moves?square=${square}`)
      .then((res) => res.json())
      .then((res) => {
        setPossibleMoves(res.board);
        setSelectedPiece(square);
      })
      .catch((err) => notify(err));
    return square;
  };
  const getRandomMove = (newturn) => {
    setTimeout(() => {
      fetch(`http://localhost:4002/random-move?color=${newturn}`, {
        method: "POST",
      })
        .then((res) => res.json())
        .then((res) => {
          setTurn(turn === "white" ? "black" : "white");
          setBoard(res.board);
        })
        .catch((err) => notify(err));
    }, 1000);
  };

  const makeMove = (sq1, sq2) => {
    fetch(
      `http://localhost:4002/make-move?starting_square=${sq1}&ending_square=${sq2}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
      .then((res) => res.json())
      .then((res) => {
        setTurn(turn === "white" ? "black" : "white");
        if (res.board) {
          setBoard(res.board);
        }
        setPossibleMoves([]);
        setSelectedPiece(null);
        notify(res.message);
      })
      .catch((err) => notify(err));
  };

  // HANDLES

  const handleCellClick = (square) => {
    if (selectedPiece) {
      makeMove(selectedPiece, square);
      if (randomMove) {
        getRandomMove("black");
      }
    } else {
      getPossibleMoves(square);
    }
  };

  const handleRandomMovButton = () => {
    setRandomMove(!randomMove);
  };

  return (
    <div>
      <h1>Chessboard {turn}</h1>
      <button onClick={handleRandomMovButton}>
        Random {randomMove ? "On" : "Off"}
      </button>
      <table className="border border-collapse mx-auto">
        <tbody>
          {board.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((piece, colIndex) => (
                <td
                  key={colIndex}
                  className={`w-20 h-20 text-center ${
                    (rowIndex + colIndex) % 2 === 0
                      ? "bg-gray-300"
                      : "bg-gray-600"
                  } ${
                    possibleMoves[rowIndex]?.[colIndex] === 1
                      ? (rowIndex + colIndex) % 2 === 0
                        ? "bg-highlight-light"
                        : "bg-highlight-dark"
                      : ""
                  }`}
                >
                  <button
                    className="w-20 h-20 flex justify-center items-center"
                    onClick={() =>
                      handleCellClick(a.tuple_to_square(colIndex, rowIndex))
                    }
                  >
                    {piece === 0 ? null : (
                      <img
                        className="w-12 h-14"
                        src={a.piece_to_url(piece)}
                        alt={`Piece ${piece}`}
                      />
                    )}
                  </button>
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
