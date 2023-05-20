
var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

var trucksData;

async function fetchData() {
  try {
    const response = await fetch('http://localhost:8080/api/truckData');
    const data = await response.json();
    console.log(data);
    trucksData = data;
    // fetch가 완료되면 여기에 이어서 로직을 추가하면 됩니다.
    // 예를 들면, 그림을 그리는 함수를 호출하는 등의 작업이 이어질 수 있습니다.
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();

// 나머지 코드

// var trucksData = [
//     {number: 1, code: 'out', entryTime: 1000, visible: true},
//     {number: 2, code: 'in', entryTime: 2000, visible: true},
//     {number: 3, code: 'out', entryTime: 3000, visible: true},
//     {number: 4, code: 'in_out',entryTime: 4000, visible: true},
//     {number: 5, code: 'in_out',entryTime: 5000, visible: true}
// ];



var trucks = [];

function createEntry(){
    return {
        x : 0,
        y : canvas.height - 500,
        width : 20,
        height : 50
    }
}
var Entry = createEntry();
drawEntry(Entry);

function drawEntry(Entry){
    ctx.fillStyle = 'blue';
    ctx.fillRect(Entry.x, Entry.y, Entry.width, Entry.height);
    ctx.fillStyle = 'black'; 
    ctx.font = '20px Arial'; 
    ctx.fillText('Entry gate', Entry.x, Entry.y); 
}

function createExit(){
    return {
        x : 780,
        y : canvas.height - 500,
        width : 20,
        height : 50
    }
}
var Exit = createExit();
drawExit(Exit);

function drawExit(Exit){
    ctx.fillStyle = 'blue';
    ctx.fillRect(Exit.x, Exit.y, Exit.width, Exit.height);
    ctx.fillStyle = 'black'; 
    ctx.font = '20px Arial'; 
    ctx.fillText('Exit gate', Exit.x, Exit.y); 
}

function createPort(){
    return {
        x: 0,
        y: canvas.height -150,
        width: 800,
        height: 150
    }
}
var port = createPort();
drawPort(port);
function drawPort(port){
    ctx.fillStyle = 'blue';
    ctx.fillRect(port.x, port.y, port.width, port.height);

    ctx.fillStyle = 'black'; // 텍스트 색상을 지정합니다. 여기서는 흰색으로 지정했습니다.
    ctx.font = '20px Arial'; // 텍스트의 크기와 폰트를 지정합니다.
    ctx.fillText('Text', port.x, port.y); // 'Text' 문자열을 thing의 위치에 그립니다.    
}

function createTruck(number, code, visible) {
    return {
        number: number,
        name: 'truck' + number,
        x: 0,
        y: canvas.height - 500,
        width: 80,
        height: 50,
        speed: 2,
        delay: 0,
        state:0,
        work_code: code,
        visible : visible
    };
}

function drawTruck(truck) {
    if(truck.visible){
        ctx.fillStyle = 'orange';
        ctx.fillRect(truck.x, truck.y, truck.width, truck.height, truck.delay, truck.state);
        ctx.fillStyle = 'black';
        ctx.fillText(truck.name, truck.x, truck.y);
    }

}


function createIn_Container(){
    return {
        x : 350,
        y : canvas.height - 500,
        width : 100,
        height : 50
    }
}
var in_container = createIn_Container();
drawIn_Container(in_container);

function drawIn_Container(in_container){
    ctx.fillStyle = 'red';
    ctx.fillRect(in_container.x, in_container.y, in_container.width, in_container.height);
    ctx.fillStyle = 'black'; 
    ctx.font = '20px Arial'; 
    ctx.fillText('unload_work', in_container.x, in_container.y); 
}

function createOut_Container(){
    return {
        x : 350,
        y : canvas.height - 350,
        width : 100,
        height : 50
    }
}
var out_container = createOut_Container();
drawOut_Container(out_container);

function drawOut_Container(out_container){
    ctx.fillStyle = 'red';
    ctx.fillRect(out_container.x, out_container.y, out_container.width, out_container.height);
    ctx.fillStyle = 'black'; 
    ctx.font = '20px Arial'; 
    ctx.fillText('load_work', out_container.x, out_container.y); 
}


function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawEntry(Entry);
    drawExit(Exit);
    drawPort(port);
    drawIn_Container(in_container)
    drawOut_Container(out_container)

    for (var i = 0; i < trucks.length; i++) {
        var truck = trucks[i];
        if(truck.work_code === 'in'){
            if (truck.state ===0){
                if (truck.x < 400 - truck.width) {
                    truck.x += truck.speed;
    
                }
                else{
                    truck.state =1;
                }
            }
            else if (truck.state === 1){
                truck.delay += 1;
                // 5초 설정
                if(truck.delay>300){
                    truck.x +=80;
                    truck.state=2;
                }
            }
            else if (truck.state ===2){
                if(truck.x < canvas.width - truck.width){
                    truck.x += truck.speed;
                }
                else{
                    truck.visible = false;
                }
        
            }
        }

        if(truck.work_code === 'out'){
            if (truck.state ===0){
                if (truck.x < 200 - truck.width) {
                    truck.x += truck.speed;
                }
                else{
                    truck.state =5;
                }
            }
            else if (truck.state ===5){
                if(truck.y < 300- truck.height){
                    truck.y += truck.speed;
                }
                else{
                    truck.state =6;
                }
            }
            else if ( truck.state ===6){
                if (truck.x < 400 - truck.width) {
                    truck.x += truck.speed;
    
                }
                else{
                    truck.state = 1;
                }
            }
            else if (truck.state === 1){
                truck.delay += 1;
                // 5초 설정
                if(truck.delay>300){
                    truck.x +=80;
                    truck.state=4;
                }
            }
            else if (truck.state ===4){
                if(truck.x<680-truck.width){
                    truck.x += truck.speed;
                }
                else{
                    truck.state = 3;
                }
            }
            else if(truck.state ===3){
                if(truck.y>150-truck.height){
                    truck.y-= truck.speed;
                }
                else{
                    truck.state = 2;
                }
            }
            else if (truck.state ===2){
                if(truck.x < canvas.width - truck.width){
                    truck.x += truck.speed;
                }
                else{
                    truck.visible = false;
                }
            }
        }

        if(truck.work_code === 'in_out'){
    
            if (truck.state ===0){
                if (truck.x < 400 - truck.width) {
                    truck.x += truck.speed;
                }
                else{
                    truck.state =1;
                }
            }
            else if (truck.state ===5){
                if(truck.y < 300- truck.height){
                    truck.y += truck.speed;
                }
                else{
                    truck.state =7;
                }
            }

            else if (truck.state === 1){
                truck.delay += 1;
                // 5초 설정
                if(truck.delay>300){
                    truck.x +=80;
                    truck.state=5;
                }
            }
            else if (truck.state === 7){
                truck.delay += 1;
                // 5초 설정
                if(truck.delay>600){
                    truck.state=4;
                }
            }
            else if (truck.state ===4){
                if(truck.x<680-truck.width){
                    truck.x += truck.speed;
                }
                else{
                    truck.state = 3;
                }
            }
            else if(truck.state ===3){
                if(truck.y>150-truck.height){
                    truck.y-= truck.speed;
                }
                else{
                    truck.state = 2;
                }
            }
            else if (truck.state ===2){
                if(truck.x < canvas.width - truck.width){
                    truck.x += truck.speed;
                }
                else{
                    truck.visible = false;
                }
            }
        }
        drawTruck(truck);
    }
    requestAnimationFrame(animate);
}

var startButton = document.getElementById('startButton');
startButton.addEventListener('click', function() {
    for (var i = 0; i < trucksData.length; i++) {
        (function(i) {
            setTimeout(function() {
                trucks.push(createTruck(trucksData[i].number, trucksData[i].code, trucksData[i].visible));
            }, trucksData[i].entryTime);
        })(i);
    }
    animate();
});
