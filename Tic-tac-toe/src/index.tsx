import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function Square(props) {
  if(props.value === "O") {
    return (
      <button className="Osquare"  onClick={props.onClick}>
        {props.value}
      </button>
    );
  } else if (props.value === "X") {
    return (
      <button className="Xsquare" onClick={props.onClick}>
        {props.value}
      </button>
    );
  } else return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
  }
    interface BoardProps {
        squares: Array<number>;
        onClick: Function;
    };  

  function Board(props:BoardProps) {

    function renderSquare(i: number) {
      return (<Square value={props.squares[i]} squares={props.squares}
      onClick={() => props.onClick(i)}/>);
    }

    return (
        <div className = "board">
          <div className="board-row">
            {renderSquare(0)}
            {renderSquare(1)}
            {renderSquare(2)}
          </div>
          <div className="board-row">
            {renderSquare(3)}
            {renderSquare(4)}
            {renderSquare(5)}
          </div>
          <div className="board-row">
            {renderSquare(6)}
            {renderSquare(7)}
            {renderSquare(8)}
          </div>
        </div>
      );
  }


function Game(){
        const [history, setHistory] = useState<Array<any>>([{squares: Array(9).fill(null)}]);
        const [stepNumber, setStepNumber] = useState(0);
        const [xIsNext, setXIsNext] = useState(true);

        function handleClick(i:number) {
            const temphistory = history.slice(0, stepNumber + 1);
            const current = temphistory[temphistory.length - 1];
            const squares = current.squares.slice();
            if (calculateWinner(squares) || squares[i]) {
                return;
              }
            squares[i] = xIsNext ? 'X' : 'O';
            setHistory(temphistory.concat([{
                squares: squares,
                  }]))
            setStepNumber(temphistory.length)
            setXIsNext(!xIsNext)
          }

          function jumpTo(step: number) {
            setStepNumber(step)
            setXIsNext((step % 2) === 0)
          }
          const tempHistory = history;
          const current = history[stepNumber];
          const winner = calculateWinner(current.squares);
          const moves = tempHistory.map((step, move) => {
                const desc = move ?
                  'Go to move #' + move :
                  'Go to game start';
                return (
                    <li key={move}>
                    <button onClick={() => jumpTo(move)}>{desc}</button>
                  </li>
                );
              });
        let status:string;
        if (winner) {
                status = 'Winner: ' + winner;
            } else {
                status = 'Next player: ' + (xIsNext ? 'X' : 'O');
            }

        return(
            <div className="game">
              <div className="game-board">
                <Board  squares={current.squares} onClick={(i: number) => handleClick(i)}/>
              </div>
              <div className="game-info">
                <div>{status}</div>
                <ol>{moves}</ol>
              </div>
            </div>
          );
    }
    
  
  // ========================================
  
  const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement) ;
  root.render(<Game />);

  function calculateWinner(squares) {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i];
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
        return squares[a];
      }
    }
    return null;
  }
  