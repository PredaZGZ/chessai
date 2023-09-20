import { useEffect, useState } from "react";

export default function Chessboard() {
  const [board, setBoard] = useState([]);
  const [possibleMoves, setPossibleMoves] = useState([]);

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

  const handleCellClick = (rowIndex, colIndex) => {
    fetch(`http://localhost:4002/possible-moves?x=${rowIndex}&y=${colIndex}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((res) => {
        setPossibleMoves(res.board);
      })
      .catch((err) => console.log(err));
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
                    className="w-20 h-20"
                    onClick={() => handleCellClick(rowIndex, colIndex)}
                  >
                    {piece === 0 ? null : piece}
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
