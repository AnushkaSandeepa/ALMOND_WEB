var canvas = document.getElementById("imgCanvas1");
    var context = canvas.getContext("2d");
    let counter = 0;
    var counter2 = 0;
    let X1 = 0,Y1 = 0,X2 = 0,Y2 = 0,result = 0;

    //section to get the coordinates of the circle
    function getMousePosition(canvas, event) {
        if(counter == 1){
        context.clearRect(0,0,640,480);
        let rect = canvas.getBoundingClientRect();
        X1 = Math.round(event.clientX - rect.left);
        Y1 = Math.round(event.clientY - rect.top);

        console.log("x1: " + X1,"&&", "y1: " + Y1);

        }
        else if(counter == 2){
        let rect = canvas.getBoundingClientRect();
        X2 = Math.round(event.clientX - rect.left - X1);
        Y2 = Math.round(event.clientY - rect.top - Y1);
        X2=X2+X1;
        Y2=Y2+Y1;
        console.log("x2: " + X2,"&&","y2: " + Y2);
                    $.ajax({
                    method: "POST",
                    url: "{% url 'Insertmeasure' %}",
                    headers: {'X-CSRFToken': '{{ csrf_token }}'},
                    contentType: "application/json",
                    dataType: 'json',
                    data: JSON.stringify({X1:X1,Y1:Y1,X2:X2,Y2:Y2,R:result}),
                    success: function(data) {
                        console.log('success!!!')
                        console.log(data)
                        result = data

                        context.font = "30px Comic Sans MS";
                        console.log("result = "+result);
                        context.fillText(result,30,50);
                        addRow(X1,Y1,X2,Y2,result)

                    },
                    error: function(jqXhr, textStatus, errorMessage){
                    console.log("Error: ", errorMessage);},
                    })




        DrawDottedLine(X1,X2,Y1,Y2,result);

        }else if(counter == 3){


            context.clearRect(0,0,640,480);
               //clears the previous circle


            return false;
        }
    }

    let canvasElem = document.querySelector("canvas");

    canvasElem.addEventListener("mousedown", function (e) {
        counter++;
        getMousePosition(canvasElem, e);
    });



//section to draw dashed line
function DrawDottedLine(a1,a2,b1,b2,result){
  var c = document.getElementById("imgCanvas1");
  var ctx = c.getContext("2d");

    if (ctx.setLineDash !== undefined) {
        ctx.setLineDash([5, 10]);
    }
    if (ctx.mozDash !== undefined) {
        ctx.mozDash = [5, 10];
    }
    ctx.beginPath();
    ctx.lineWidth = "2";
    ctx.strokeStyle = "blue";
    ctx.moveTo(a1, b1);
    ctx.lineTo(a2, b2);
    ctx.stroke();
}


//section to draw the circle
   function draw(e) {

    var canvas = document.getElementById("imgCanvas1");
    var context = canvas.getContext("2d");

    var rect = canvas.getBoundingClientRect();
    var posx = e.clientX - rect.left;
    var posy = e.clientY - rect.top;
    if(counter!=3){
    context.fillStyle = "#0000FF"; // to change colour of circle
    context.beginPath();
    context.arc(posx, posy, 10, 0, 2 * Math.PI);  // to change size of circle
    context.fill();
    }else if(counter == 3){
        counter = 0;
    }
    console.log("counter = "+counter);
}

    function drawcircle(x,y) {

    context.fillStyle = "#0000FF"; // to change colour of circle
    context.beginPath();
    context.arc(x, y, 10, 0, 2 * Math.PI);  // to change size of circle
    context.fill();
}

