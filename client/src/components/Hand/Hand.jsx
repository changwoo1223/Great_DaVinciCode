import Tile from "../Tile/Tile";
import './Hand.css';

function Hand({tiles, style}){
    return(
        <div className="hand" style={style} >
            {tiles.map((tile, index) => (
                <Tile
                    key={index}
                    number={tile.number}
                    revealed={tile.revealed}
                    color={tile.color}
                />
            ))}
        </div>
    )
}

export default Hand;