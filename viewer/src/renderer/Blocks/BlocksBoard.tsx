import { useEffect, useState } from 'react'
import { DataGrid, GridColDef, GridRenderCellParams } from '@mui/x-data-grid';
import redPiece from "../../../assets/icons/redblock.png"
import bluePiece from "../../../assets/icons/blueblock.png"
import piece1 from "../../../assets/icons/A.png"
import piece2 from "../../../assets/icons/B.png"
import piece3 from "../../../assets/icons/C.png"
import piece4 from "../../../assets/icons/D.png"
import piece5 from "../../../assets/icons/E.png"
import piece6 from "../../../assets/icons/F.png"
import piece7 from "../../../assets/icons/G.png"
import piece8 from "../../../assets/icons/H.png"
import piece9 from "../../../assets/icons/I.png"
import piece10 from "../../../assets/icons/J.png"
import piece11 from "../../../assets/icons/K.png"
import piece12 from "../../../assets/icons/L.png"
import piece13 from "../../../assets/icons/M.png"
import piece14 from "../../../assets/icons/N.png"
import piece15 from "../../../assets/icons/O.png"
import piece16 from "../../../assets/icons/P.png"
import piece17 from "../../../assets/icons/Q.png"
import piece18 from "../../../assets/icons/R.png"
import piece19 from "../../../assets/icons/S.png"
import piece20 from "../../../assets/icons/T.png"
import piece21 from "../../../assets/icons/U.png"

const columns: GridColDef[] = [
    {field:'id',    headerName:'',    width:40 , minWidth:40, disableColumnMenu: true, sortable:false, resizable:false, cellClassName:"id_col"},
    {field:'col1',  headerName:'1',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col2',  headerName:'2',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col3',  headerName:'3',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col4',  headerName:'4',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col5',  headerName:'5',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col6',  headerName:'6',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col7',  headerName:'7',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col8',  headerName:'8',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col9',  headerName:'9',   width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col10', headerName:'A',  width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col11', headerName:'B',  width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col12', headerName:'C',  width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col13', headerName:'D',  width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
    {field:'col14', headerName:'E',  width:40 , minWidth:40 ,disableColumnMenu: true, sortable:false, resizable:false, valueFormatter: ({ value }) => ( '' ),renderCell:(params:GridRenderCellParams)=>{return renderCellParams(params)}, cellClassName:(params)=>{return getCellClassName(params)}},
]

function getCellClassName(params:any):any{
    if (params.value === "1" ){
        return "red-cell"
    }
    if (params.value === "2" ){
        return "blue-cell"
    }
    return 'default-cell'
}
function renderCellParams(params:GridRenderCellParams){
    const value = params.value;
      return value === "1" ? (
        <img src={redPiece} alt="Image" style={{ width: '100%', height: '100%', objectFit: 'cover', padding: 0}}/>
      ) : value === "2" ? (
        <img src={bluePiece} alt="Image" style={{ width: '100%', height: '100%', objectFit: 'cover', padding: 0 }}/>
      ) : null;
}


var isLoop:boolean = false;

function viewaction(loopcount:number, beforeBoard:Function, afterBoard:Function){
    var counter = 0;
    isLoop = true;
    var id = setInterval(function() {
        counter++;
        if (counter < loopcount){
            if(counter % 2 == 0){
                afterBoard();
            }else{
                beforeBoard();
            }
        }else{
            clearInterval(id);
            isLoop = false;
            afterBoard();
        }
    },
    200
    )
}

export default function BlocksBoard(prop:any){
    const [p1Name, setP1Name] = useState(prop.p1Name);
    const [p2Name, setP2Name] = useState(prop.p2Name);
//    const [winName, setWinName] = useState(prop.winName);
    const [board, setBoard] = useState(prop.board);
    const [p1piece, setP1piece] = useState(prop.p1piece);
    const [p2piece, setP2piece] = useState(prop.p2piece);
    if (board != prop.board && !isLoop){
        var tempBoard = board;

        viewaction(10, ()=>{setBoard(tempBoard);}, ()=>{setBoard(prop.board)})
        

    }

    const getWinNameString = () => {
        return prop.winName;
    }

    return(
            <div className='blocks-view' style={{ display:'flex', textAlign:'center', justifyContent:'center'}}>
                <div className="playerArea"><h3>先手：{prop.p1Name}</h3>
                <div style={{width:200}}>
                    <img className='img-1' src={piece1} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("A")}/>
                    <img className='img-1' src={piece2} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("B")}/>
                    <img className='img-1' src={piece3} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("C")}/>
                    <img className='img-1' src={piece4} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("D")}/>
                    <img className='img-1' src={piece5} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("E")}/>
                    <img className='img-1' src={piece6} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("F")}/>
                    <img className='img-1' src={piece7} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("G")}/>
                    <img className='img-1' src={piece8} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("H")}/>
                    <img className='img-1' src={piece9} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("I")}/>
                    <img className='img-1' src={piece10} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("J")}/>
                    <img className='img-1' src={piece11} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("K")}/>
                    <img className='img-1' src={piece12} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("L")}/>
                    <img className='img-1' src={piece13} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("M")}/>
                    <img className='img-1' src={piece14} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("N")}/>
                    <img className='img-1' src={piece15} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("O")}/>
                    <img className='img-1' src={piece16} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("P")}/>
                    <img className='img-1' src={piece17} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("Q")}/>
                    <img className='img-1' src={piece18} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("R")}/>
                    <img className='img-1' src={piece19} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("S")}/>
                    <img className='img-1' src={piece20} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("T")}/>
                    <img className='img-1' src={piece21} alt='picture' style={{width:50}} hidden={!prop.p1piece.includes("U")}/>
                </div></div>
                
                <div>
                    <div><h3>　{getWinNameString()}　</h3></div>
                    <DataGrid
                        rows={board}
                        columns={columns}
                        rowHeight={58}
                        hideFooter
                        autoHeight
                        scrollbarSize={0}
                        showCellVerticalBorder
                        density='compact'
                        sx={{
                            '& .MuiDataGrid-columnHeader': {
                            backgroundColor: 'aliceblue', // ヘッダーの背景色を変更
                            },
                        }}
                        
                    />
                </div>
                <div className="playerArea"><h3>後手：{prop.p2Name}</h3>
                <div style={{width:200}}>
                    <img className='img-1' src={piece1} alt='picture' hidden={!prop.p2piece.includes("A")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece2} alt='picture' hidden={!prop.p2piece.includes("B")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece3} alt='picture' hidden={!prop.p2piece.includes("C")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece4} alt='picture' hidden={!prop.p2piece.includes("D")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece5} alt='picture' hidden={!prop.p2piece.includes("E")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece6} alt='picture' hidden={!prop.p2piece.includes("F")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece7} alt='picture' hidden={!prop.p2piece.includes("G")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece8} alt='picture' hidden={!prop.p2piece.includes("H")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece9} alt='picture' hidden={!prop.p2piece.includes("I")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece10} alt='picture' hidden={!prop.p2piece.includes("J")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece11} alt='picture' hidden={!prop.p2piece.includes("K")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece12} alt='picture' hidden={!prop.p2piece.includes("L")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece13} alt='picture' hidden={!prop.p2piece.includes("M")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece14} alt='picture' hidden={!prop.p2piece.includes("N")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece15} alt='picture' hidden={!prop.p2piece.includes("O")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece16} alt='picture' hidden={!prop.p2piece.includes("P")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece17} alt='picture' hidden={!prop.p2piece.includes("Q")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece18} alt='picture' hidden={!prop.p2piece.includes("R")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece19} alt='picture' hidden={!prop.p2piece.includes("S")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece20} alt='picture' hidden={!prop.p2piece.includes("T")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                    <img className='img-1' src={piece21} alt='picture' hidden={!prop.p2piece.includes("U")} style={{width:50, filter:"invert(0%) sepia(0%) saturate(100%) hue-rotate(225deg)"}}/>
                </div></div>
            </div>
    )

}
