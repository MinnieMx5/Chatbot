const apiEndpoint = 'http://127.0.0.1:5000/chatbot';
const contentType = 'application/json';

const messagesElement = document.getElementById("messages");
const userInputElement = document.getElementById("userinput");
const sendButtonElement = document.getElementById("sendbutton");

function createMessageElement(text, className) {
  const messageElement = document.createElement("div");
  messageElement.classList.add("message", className);
  messageElement.textContent = text;
  return messageElement;
}

function displayMessage(messageElement) {
  messagesElement.appendChild(messageElement);
  messagesElement.scrollTop = messagesElement.scrollHeight;
}

function sendMessageToBackend(message) {
  fetch(apiEndpoint, {
    method: 'POST',
    headers: {
      'Content-Type': contentType
    },
    body: JSON.stringify({ message: message })
  })
 .then(response => response.json())
 .then(data => {
    if (data && data.response) {
      const chatbotResponseElement = createMessageElement(data.response, "chatbot");
      displayMessage(chatbotResponseElement);
    } else {
      console.error('Invalid chatbot response:', data);
    }
  })
 .catch(error => {
    console.error('Error:', error);
  });
}

function handleSendMessage() {
  const message = userInputElement.value.trim();
  if (message) {
    const userMessageElement = createMessageElement(message, "user");
    displayMessage(userMessageElement);
    sendMessageToBackend(message);
    userInputElement.value = ""; 
  }
}

sendButtonElement.addEventListener("click", handleSendMessage);

userInputElement.addEventListener("keypress", event => {
  if (event.key === "Enter") {
    handleSendMessage();
  }
});