import {useEffect} from 'react';
import socket from '../services/socket.js';

function useSocket(eventName,callback){
    useEffect(() =>{
        socket.on(eventName,callback);
        return () => socket.off(eventName, callback);
    }, [eventName, callback]);
}

export default useSocket;