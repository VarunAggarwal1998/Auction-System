'use strict';

function setupWebSocket(auctionId) {
    console.log("Script started"); // Check if the script starts
    var wsStart = 'ws://';
    if (window.location.protocol === 'https:') {
        wsStart = 'wss://';
    }
    var endpoint = wsStart + window.location.host + '/ws/auction/' + auctionId + '/';
    console.log(endpoint);
    var socket = new WebSocket(endpoint);

    // ... rest of your WebSocket code ...
  // Handle WebSocket errors
        socket.onerror = function(e) {
            console.error('WebSocket error observed:', e);
        };

        // Handle WebSocket connection open
        socket.onopen = function(e) {
            console.log('WebSocket connection established');
        };

        // Handle incoming messages
        socket.onmessage = function(e) {
            var data = JSON.parse(e.data);
            var message = data['message'];
            if (message) {
                // Update the bid information on the page
                updateBidInfo(message);
            }
        };

        // Handle WebSocket connection close
        socket.onclose = function(e) {
            console.log('WebSocket connection closed', e);
        };

        function updateBidInfo(message) {
            // Parse the message and update the bid information
            var bidInfo = JSON.parse(message);
            document.querySelector('#current-bid strong').innerText = 'US $ ' + bidInfo.bid;
            // Add any other elements you want to update, like bidder's username
        }
}