import Button from '../components/Button/Button.jsx'

function Lobby({content,setPage}) {
    return (
    <div>
        <h1>멋진 {content}!</h1>
        <h2>0/4</h2>
        <Button label="시작하기" onClick={() => setPage("play")} />
        <a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
        <Button label="참여하기" onClick="join()" />
        
    </div>
    );
}

export default Lobby;
