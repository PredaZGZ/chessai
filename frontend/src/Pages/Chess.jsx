//Components
import Chessboard from "../Components/Chessboard.jsx";

export default function Chess() {
  const handleButton = () => {
    fetch("http://localhost:4002/reset", {
      method: "GET",
    })
      .then((res) => res.json())
      .then(() => location.reload()) // DEBUG
      .catch((err) => console.log(err));
  };
  return (
    <div className="flex justify-center">
      <button onClick={handleButton}>Reset Game</button>
      <Chessboard />
    </div>
  );
}
