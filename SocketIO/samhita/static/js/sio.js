/*
Source https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d
*/
var socket = io.connect('http://' + document.domain + ':' + location.port);
assign_socket_params (socket);
//-----------------------------------------------------------------------------
function sioDisconnect () {
	try {
		socket.disconnect();
		document.getElementById("socket_disconnect").disabled = true;
        document.getElementById("socket_connect").disabled    = false;
    }
	catch (err) {
		console.log(err.message);
		alert(err.message);
	}
}
//-----------------------------------------------------------------------------
function sioConnect () {
	try {
        var server = $('#remote_server').val();
        var port = $('#remote_port').val();
        //socket.disconnect();
        socket = io.connect('http://' + server + ':' + port);
        assign_socket_params (socket);
		document.getElementById("socket_disconnect").disabled = false;
        document.getElementById("socket_connect").disabled    = true;
    }
	catch (err) {
		console.log(err.message);
		alert(err.message);
	}
}
//-----------------------------------------------------------------------------
function assign_socket_params (socket) {
    socket.on( 'connect', function() {
        socket.emit( 'my event', {
          data: 'User Connected'
        });
        var form = $( 'form' ).on( 'submit', function( e ) {
            e.preventDefault()
            var user_name = $( 'input.username' ).val();
            var user_input = $( 'input.message' ).val();
            socket.emit( 'my event', {
                user_name : user_name,
                message : user_input
            })
            $( 'input.message' ).val( '' ).focus()
        } )
    });
//-----------------------------------------------------------------------------
    socket.on( 'my response', function( msg ) {
        var divMessage = document.getElementById("incomming_message");
        console.log( msg )
        if (msg.user_name != null) {
            var f = $('#msg_flag');
            if (f.html() == "no_message") {
                divMessage.innerText="";
                f.text("yes_message");
                divMessage.style.fontSize = "12px";
            }
            if(divMessage.style.fontSize == "12px") {
                $("#incomming_message").append('<b>' + msg.user_name + '</b>' + msg.message + '<br>');
            }
        }
    });
}
/**/
