async function sendMessage(event) {
    event.preventDefault();
    const messageInput = document.getElementById('message-input');
    const messageText = messageInput.value;
    const chatMessages = document.getElementById('chat-messages');
    const newMessage = document.createElement('div');
    newMessage.classList.add('bg-gray-200', 'rounded-lg', 'p-4', 'mb-4');
    newMessage.innerHTML = `<p>You: ${messageText}</p>`;
    chatMessages.appendChild(newMessage);
    messageInput.value = '';
    const response = await fetch('/api/chatbot/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: messageText,
      }),
    });
    if (!response.ok) {
      const errorText = await response.text();
      console.error(`Error: ${errorText}`);
      return;
    }
    const responseData = await response.json();
    const botMessage = responseData.message;
    const botMessageElement = document.createElement('div');
    botMessageElement.classList.add('bg-gray-200', 'rounded-lg', 'p-4', 'mb-4');
    botMessageElement.innerHTML = `<p>Bot: ${botMessage}</p>`;
    chatMessages.appendChild(botMessageElement);
  }
  