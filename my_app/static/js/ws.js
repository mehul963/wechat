const websocketProtocol = location.protocol === 'http:' ? 'ws:' : 'wss:';
ws = new WebSocket(websocketProtocol + window.location.host + "/ws/connect")
ws.onmessage = (event) => {
    const data = JSON.parse(event.data)
    const div = document.createElement("div")
    div.innerText = data['msg']
    if (data['user'] !== data['sender']) {
        div.className = 'left';
    }

    const user = document.getElementById("user-input")
    console.log(data)
    if(user.value===''){
        user.value=data['sender']
        document.getElementById('chat-user').innerText=data['sender']
    }
    else if(data['sender']===undefined){
        div.innerText = `${data['msg']}`
    }
    else if(user.value!==data['sender']){
        div.innerText = `${data['sender']} -> ${data['msg']}`
    }
    document.getElementById("msg").appendChild(div)
    const myDiv = document.getElementById("msg")
    myDiv.scrollTop += (myDiv.scrollHeight)
}
const send = () => {
    const user = document.getElementById("user-input").value
    const msg = document.getElementById("text-msg")
    if(user==='' || msg.value===''){
        return
    }
    if (msg.value) {
        ws.send(JSON.stringify({
            "msg": msg.value,
            'user': `${user}`,
            'sender':`${sender}`,
        }))
    }

    const div = document.createElement("div")
    div.innerText = msg.value
    div.className = 'right'
    document.getElementById("msg").appendChild(div)
    msg.value = ''
    const myDiv = document.getElementById("msg")
    myDiv.scrollTop += (myDiv.scrollHeight)

}
