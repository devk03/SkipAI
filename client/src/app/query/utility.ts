import { withCookies, Cookies } from 'react-cookie';

function extactKey(url : string){
    let key = url.split("/").pop();
    return key;
}

async function postLecture(lectureKey: string) {
    const url = `http://127.0.0.1:5000/fetchLecture?lectureKey=${lectureKey}`;
    const response = await fetch(url);
    return response;
}


export {extactKey, postLecture};