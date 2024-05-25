import { MemoryRouter as Router, Routes, Route } from 'react-router-dom';
import icon from '../../assets/icon.svg';
import './App.css';
import BlocksBoard from './Blocks/BlocksBoard';
import { useState } from 'react';
import { GridColDef, GridRowsProp, GridValidRowModel } from '@mui/x-data-grid';
import { BoardData, default_data, default_pieces } from './Blocks/BoadData';

let defaultData :GridRowsProp = default_data;
let defaultPiece = default_pieces;

function BlocksView() {
  const [p1Name, setP1Name] = useState("");
  const [p2Name, setP2Name] = useState("");
  const [winName, setWinName] = useState("");
  const [board, setBoard] = useState(defaultData);
  const [p1piece, setP1Piece] = useState(defaultPiece);
  const [p2piece, setP2Piece] = useState(defaultPiece);
  const [score, setScore] = useState("");

  window.electron.ipcRenderer.review('view-message', (json:any) => {
    var boardData = convertBoadData(json.board)
    setP1Name(json.p1Name)
    setP2Name(json.p2Name)
    setBoard(boardData)//受け取った情報で最新へ更新
    
    //setBoard(json.board)
    setP1Piece(json.p1piece)
    setP2Piece(json.p2piece)
    setScore(json.p1Name + ":" + json.score[json.p1Name] + "勝　　" + json.p2Name + ":" + json.score[json.p2Name] + "勝")
  });
  window.electron.ipcRenderer.resultView('result-message', (json:any) => {
    setWinName(json.winName)
  });

  return (
    <div>
      <div>
        <h2 style={{textAlign:'center', padding:"0px", margin: "0px"}}>　{score}　</h2>
        <BlocksBoard p1Name={p1Name} p2Name={p2Name} board={board} p1piece={p1piece} p2piece={p2piece} winName={winName}/>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<BlocksView />} />
      </Routes>
    </Router>
  );
}
function convertBoadData(board: any[][]) :GridValidRowModel[] {

  var i = 1;
  var result:BoardData[] = [];
  for (var row = 0; row < board.length; row++){
    var data:BoardData = {
      id:i.toString(16).toUpperCase(),
      col1:board[row][0].toString(),
      col2:board[row][1].toString(),
      col3:board[row][2].toString(),
      col4:board[row][3].toString(),
      col5:board[row][4].toString(),
      col6:board[row][5].toString(),
      col7:board[row][6].toString(),
      col8:board[row][7].toString(),
      col9:board[row][8].toString(),
      col10:board[row][9].toString(),
      col11:board[row][10].toString(),
      col12:board[row][11].toString(),
      col13:board[row][12].toString(),
      col14:board[row][13].toString()
    }
    result.push(data);
    i++;
  }
  return result;
}

