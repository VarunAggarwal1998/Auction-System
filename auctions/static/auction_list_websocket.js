'use strict';



function setupWebSocketForAuction(auctionId) {
    var auctionSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/auction/' + auctionId + '/'
    );

auctionSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var messageData = JSON.parse(data.message);
    document.querySelector('#current-bid-' + auctionId).innerText = 'US $ ' + messageData.bid;
};


    auctionSocket.onclose = function(e) {
        console.error('Auction socket closed unexpectedly');
    };
}
