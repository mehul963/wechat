
const myInput = document.getElementById('text-msg');
myInput && myInput.addEventListener('keydown', function (event) {
    if (event.key === "Enter") {
        send()
        const myDiv = document.getElementById("msg")
        myDiv.scrollTop += (myDiv.scrollHeight)
    }
});


users=document.querySelectorAll('.user')

users && users.forEach((user)=>{
    user.addEventListener('click',()=>{
        document.getElementById('chat-user').innerText=user.innerText
        document.getElementById('user-input').value=user.innerText
        document.getElementById("msg").innerHTML=''

        send_get(user.innerText)
        // const websocketProtocol = location.protocol === 'http:' ? 'ws:' : 'wss:';
        // const ws_chat=new WebSocket(websocketProtocol + window.location.host +'/ws/sendchat')
        // ws_chat.onopen=()=>{
        //     ws_chat.send(JSON.stringify({
        //         'receiver':user.innerText
        //     }))
        // }
    })
})



document.getElementById('md-nav').addEventListener('click',(e)=>{
    const nav=document.getElementById('md-navbar')
    if(nav.classList.contains('hide')){
        nav.classList.remove('hide')
        nav.classList.add('md-flex')
    }else{
        nav.classList.add('hide')
        nav.classList.remove('md-flex')
    }
})
