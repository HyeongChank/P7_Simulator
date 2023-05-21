import React, { useState, useEffect, useRef } from 'react';

function Display(){

    const [trucksData, setTrucksData] = useState([]);
    useEffect(() => {
        fetch('http://localhost:8080/api/truckData')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => setTrucksData(data))
            .catch(error => {
                console.error('There has been a problem with your fetch operation: ', error);
            });
    }, []);   

    const canvasRef = useRef(null);
    const [trucks, setTrucks] = useState([]);
    const drawEntry = (Entry, ctx) => { 
        ctx.fillStyle = 'blue';
        ctx.fillRect(Entry.x, Entry.y, Entry.width, Entry.height);
        ctx.fillStyle = 'black'; 
        ctx.font = '20px Arial'; 
        ctx.fillText('Entry gate', Entry.x, Entry.y);
    }
    const drawExit = (Exit, ctx) => {
        ctx.fillStyle = 'blue';
        ctx.fillRect(Exit.x, Exit.y, Exit.width, Exit.height);
        ctx.fillStyle = 'black'; 
        ctx.font = '20px Arial'; 
        ctx.fillText('Exit gate', Exit.x, Exit.y); 
    }
    const drawPort = (port, ctx) => {
        ctx.fillStyle = 'blue';
        ctx.fillRect(port.x, port.y, port.width, port.height);
        ctx.fillStyle = 'black'; 
        ctx.font = '20px Arial'; 
        ctx.fillText('Port', port.x, port.y); 
    }
    const drawIn_Container = (in_container, ctx) => {
        ctx.fillStyle = 'red';
        ctx.fillRect(in_container.x, in_container.y, in_container.width, in_container.height);
        ctx.fillStyle = 'black'; 
        ctx.font = '20px Arial'; 
        ctx.fillText('unload_work', in_container.x, in_container.y); 
    }
    const drawOut_Container = (out_container, ctx) => {
        ctx.fillStyle = 'red';
        ctx.fillRect(out_container.x, out_container.y, out_container.width, out_container.height);
        ctx.fillStyle = 'black'; 
        ctx.font = '20px Arial'; 
        ctx.fillText('load_work', out_container.x, out_container.y); 
    }
    
    const createTruck = (number, code, visible) => {
        const canvas = canvasRef.current;
        const truck = {
            number: number,
            name: 'truck' + number,
            x: 0,
            y: canvas.height - 500,
            width: 80,
            height: 50,
            speed: 2,
            delay: 0,
            state: 0,
            work_code: code,
            visible : visible
        };
        setTrucks(trucks => [...trucks, truck]);
    }

    const drawTruck = (truck, ctx) => {
        if (truck.visible) {
            ctx.fillStyle = 'orange';
            ctx.fillRect(truck.x, truck.y, truck.width, truck.height);
            ctx.fillStyle = 'black';
            ctx.fillText(truck.name, truck.x, truck.y);
        }
    }
    

    useEffect(() => {
        const canvas = canvasRef.current;
        if (canvas === null) {  // canvas가 null인지 확인합니다.
            return;
        }
        const ctx = canvas.getContext('2d');
        
        if (ctx === null) {  // ctx가 null인지 확인합니다.
            return;
        }


        const createEntry = () => {
            const canvas = canvasRef.current;
            return {
                x: 0,
                y: canvas.height - 500,
                width: 20,
                height: 50,
            }
        }
        const Entry = createEntry();

        const createExit =() => {
            const canvas = canvasRef.current;
            return {
                x : 780,
                y : canvas.height - 500,
                width : 20,
                height : 50
            }
        }
        const Exit = createExit();

        const createPort = () => {
            const canvas = canvasRef.current;
            return {
                x: 0,
                y: canvas.height -150,
                width: 800,
                height: 150
            }
        }
        const port = createPort();

        const createIn_Container = ()=> {
            const canvas = canvasRef.current;
            return {
                x : 350,
                y : canvas.height - 500,
                width : 100,
                height : 50
            }
        }
        const in_container = createIn_Container();

        const createOut_Container = () => {
            const canvas = canvasRef.current;
            return {
                x : 350,
                y : canvas.height - 350,
                width : 100,
                height : 50
            }
        }
        const out_container = createOut_Container();


        const animate = () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.beginPath();
            ctx.rect(0, 0, canvas.width, canvas.height);
            ctx.lineWidth = 2;
            ctx.strokeStyle = 'black';
            ctx.stroke();

            drawEntry(Entry, ctx);
            drawExit(Exit, ctx);
            drawPort(port, ctx);
            drawIn_Container(in_container, ctx);
            drawOut_Container(out_container, ctx);
            let updatedTrucks = trucks.map(truck => {
                if (truck.work_code === 'in') {
                    if (truck.state === 0) {
                        if (truck.x < 400 - truck.width) {
                            truck.x += truck.speed;
                        }
                        else {
                            truck.state = 1;
                        }
                    }
                    else if (truck.state === 1) {
                        truck.delay += 1;
                        // 5초 설정
                        if (truck.delay > 300) {
                            truck.x += 80;
                            truck.state = 2;
                        }
                    }
                    else if (truck.state === 2) {
                        if (truck.x < canvas.width - truck.width) {
                            truck.x += truck.speed;
                        }
                        else {
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
                        // 5초 설정 250번의 호출(20밀리세컨드 기준)
                        if(truck.delay>250){
                            truck.x +=80;
                            truck.state=5;
                        }
                    }
                    else if (truck.state === 7){
                        truck.delay += 1;
                        // 5초 설정
                        if(truck.delay>500){
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
                return truck;
            });
        setTrucks(updatedTrucks);
        
        trucks.forEach(truck => drawTruck(truck, ctx));
        // requestAnimationFrame(animate);
        }
        // 호출 사이의 간격 0.02초
        const intervalId = setInterval(animate, 20); // 20 milliseconds between each frame

        return () => {
            clearInterval(intervalId); // Clean up on unmount
        }
    }, [trucks]);

    const handleClick = () => {
        trucksData.forEach((truckData, i) => {
            setTimeout(() => {
                createTruck(truckData.number, truckData.code, truckData.visible);
            }, truckData.entryTime);
        });
    };

    return (
        <div>
            <canvas ref={canvasRef} width={800} height={600}  />
            <button onClick={handleClick}>Start</button>
        </div>
    );
}

export default Display

