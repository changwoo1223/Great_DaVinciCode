import './Tile.css';


function Tile({ number, revealed, color }) {
    return (
        <div className={`tile ${revealed ? "revealed" : "blind"} ${color}`}>
            {revealed ? <span>{number}</span> : null}
        </div>
    );
}

export default Tile;
