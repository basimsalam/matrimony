// client.js
function longPolling() {
    const url = '/get-messages/';

    // Function to handle the response
    function handleResponse(response) {
        if (response.timeout) {
            // Handle timeout (optional)
            console.log('Long polling timeout');
        } else {
            // Handle new messages
            console.log('Received new messages:', response.messages);
            // Update UI or perform actions with new messages
            response.messages.forEach(message => {
                // Example: Append message to chat window
                const messageElement = document.createElement('div');
                messageElement.textContent = `${message.sender}: ${message.content}`;
                document.getElementById('chat-window').appendChild(messageElement);
            });
        }

        // Restart long polling
        longPolling();
    }

    // Make long polling request
    fetch(url)
        .then(response => response.json())
        .then(data => handleResponse(data))
        .catch(error => {
            console.error('Error during long polling:', error);
            // Retry or handle error as needed
            longPolling();
        });
}

// Start long polling when the page is ready
document.addEventListener('DOMContentLoaded', function() {
    longPolling();
});
