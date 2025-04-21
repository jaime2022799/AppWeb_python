const chatInput =  document.querySelector(".chat-input textarea");
const sendChatBtn =  document.querySelector(".chat-input span");


const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = className === "outgoing" ? `<p>${message}</p>` : `   <span class="material-symbols-outlined">smart_toy</span><p>${message}</p>`
    chatLi.innerHTML = chatContent;
    return chatLi;
}

const generateResponde = (incomingChatLi) => {
    
    const messageElement = incomingChatLi.querySelector("p")

    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "applications/json",
           
        },
        body: JSON.stringify({
            model: "gpt-4.1",
            message: [{role: "user", content: userMessage}]
        })
    }

    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        messageElement.textContent = data.choises[0].message.content;
    }).catch((error) => {
        messageElement.textContent = "Oops! something went wrong. Please try again";
    }).finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
}

const handleChat = () => {
    userMessage = chatInput.value.trim();
    if(!userMessage) return;

    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);

   setTimeout(() =>{
    const incomingChatLi = createChatLi("thinking.....", "incoming")
    chatbox.appendChild(incomingChatLi);
    chatbox.scrollTo(0, chatbox.scrollHeight);
    generateResponde(incomingChatLi);
   }, 600)
}

sendChatBtn.addEventListener("click", handleChat);