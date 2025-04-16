import Button from '../components/Button/Button.jsx'
import Tile from '../components/Tile/Tile.jsx';
import Hand from '../components/Hand/Hand.jsx';

function Play() {
    const tiles = [
        { number: 1, revealed: true, color: "black" },
        { number: 3, revealed: false, color: "white" },
        { number: 5, revealed: true, color: "black" },
        { number: 3, revealed: true, color: "white" },
        { number: 3, revealed: true, color: "white" },
        
    ];
    const tiles1 = [];
    const tiles2 = [];
    const tiles3 = [];
    const tiles4 = [];

    return(
        <div style={{}}>
            {/*타일 위치 설정*/}
            <div style={{ position: "absolute", bottom: "0px", transform: "translateX(-50%)", width: "700px" }}>
                <Hand tiles={tiles} style={{transform: "rotate(0deg)"}}/>
            </div>
            <div style={{ position: "absolute", left: "-130px", transform: "translateY(-50%)", width: "700px"}}>
                <Hand tiles={tiles} style={{ transform: "rotate(90deg)" }} />
            </div>
            <div style={{ position: "absolute", top: "0px", transform: "translateX(-50%)", width: "700px" }} >
                <Hand tiles={tiles} style={{ transform: " rotate(180deg)" }}/>
            </div>
            <div style={{ position: "absolute", right: "-130px", transform: "translateY(-50%)", width: "700px"}} >
                <Hand tiles={tiles} style={{ transform: "rotate(270deg)" }}/>
            </div>
            
        </div>
    );
};

export default Play;