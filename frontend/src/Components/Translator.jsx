const columns = ["a", "b", "c", "d", "e", "f", "g", "h"];

const tuple_to_square = (x, y) => {
  return columns[x] + (8 - y).toString();
};
const square_to_tuple = (square) => {
  const lst = Array.from(square);

  for (let i = 0; i < lst.length; i++) {
    if (columns.includes(lst[i])) {
      lst[0] = columns.indexOf(lst[i]);
    } else {
      lst[1] = 8 - parseInt(lst[i], 10);
    }
  }

  return [lst[0], lst[1]];
};

const dict = {
  1: "w_pawn",
  2: "b_pawn",
  3: "w_rook",
  4: "b_rook",
  5: "w_knight",
  6: "b_knight",
  7: "w_bishop",
  8: "b_bishop",
  9: "w_queen",
  10: "b_queen",
  11: "w_king",
  12: "b_king",
};

const piece_to_url = (piece) => {
  const url = new URL(`./assets/${dict[piece]}.png`, import.meta.url).href;
  return url;
};

const Translator = {
  tuple_to_square,
  square_to_tuple,
  dict,
  piece_to_url,
};

export default Translator;
