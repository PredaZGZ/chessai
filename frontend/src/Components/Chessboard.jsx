import { useEffect, useState } from "react";
import a from "./Translator";

export default function Chessboard() {
  const [board, setBoard] = useState([]);
  const [possibleMoves, setPossibleMoves] = useState([]);
  const [selectedPiece, setSelectedPiece] = useState(null);

  useEffect(() => {
    fetch("http://localhost:4002/", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((res) => {
        setBoard(res.board);
      })
      .catch((err) => console.log(err));
  }, []);

  const notify = (noti) => {
    console.log(noti);
  };

  const handleCellClick = (square) => {
    if (selectedPiece) {
      fetch(
        `http://localhost:4002/make-move?starting_square=${selectedPiece}&ending_square=${square}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
        .then((res) => res.json())
        .then((res) => {
          if (res.board) {
            setBoard(res.board);
          }
          setPossibleMoves([]);
          setSelectedPiece(null);
          console.log(res.message);
        })
        .catch((err) => notify(err));
    } else {
      fetch(`http://localhost:4002/possible-moves?square=${square}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((res) => {
          if (res.board) {
            setPossibleMoves(res.board);
          }
          setSelectedPiece(square);
        })
        .catch((err) => notify(err));
    }
  };

  return (
    <div>
      <h1>Chessboard</h1>
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
