function sendMessage() {
    const messageInput = document.getElementById("message");
    const message = messageInput.value.trim();
    if (!message) return;

    const chatBox = document.getElementById("chat-box");

    // User message
    chatBox.innerHTML += `<div class="user"><b>You:</b> ${message}</div>`;
    messageInput.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot"><b>Bot:</b> ${data.reply}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
