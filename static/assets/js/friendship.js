function addFriend(profileId) {
    $.ajax({
        type: 'POST',
        url: '{% url "app:add_friend" profileId %}',
        success: function(response) {
            // Handle success, e.g., update UI
            console.log(response);
        },
        error: function(error) {
            // Handle error
            console.error(error);
        }
    });
}

function unfriend(profileId) {
    $.ajax({
        type: 'POST',
        url: '{% url "app:unfriend" profileId %}',
        success: function(response) {
            // Handle success, e.g., update UI
            console.log(response);
        },
        error: function(error) {
            // Handle error
            console.error(error);
        }
    });
}
