const socket = io("/app")

const inpform = document.getElementById('inpform')
const inpbox = document.getElementById('inpbox')
const chatbox = document.getElementById('chatbox')


let name =""
let previnp=""

if (localStorage.getItem("name")==null){

name = prompt("What is Your name?")
localStorage.setItem("name" , `${name}`)

}

    name = localStorage.getItem("name")
    
    socket.emit("Connection", name)






    appendMsg(`<span class="usrjoin">${name}</span> Joined`,"joined")



socket.on("response", res => {
    appendMsg(`<span class="bot">Bot</span> :  ${res}`,"botres")
    console.log(`username: ${name}, input: ${previnp}, response: ${res}`)
    chatbox.scrollTop = chatbox.scrollHeight;
})



inpform.addEventListener("submit", e => {

    e.preventDefault()
    var inptxt = inpbox.value || ""

    if (inptxt!=""){
 

    socket.emit("sendinp", inptxt)

    appendMsg(`<span class="usr">${name}</span> : ${inptxt}`,"usrinp")
    previnp=inptxt
    inpbox.value=""
    chatbox.scrollTop = chatbox.scrollHeight;
    
    }
    
})


function appendMsg(chat,cname){
    const chatEl = document.createElement("div")
    chatEl.className="chatl"
    chatEl.className=cname
    chatEl.innerHTML= chat
    chatbox.append(chatEl)
}