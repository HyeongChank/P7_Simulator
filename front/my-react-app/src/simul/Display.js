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
    
    const createTruck = (number, code, entryTime, arrive_unload_spot,
        start_unload_work, complete_unload_work, arrive_load_spot,
         start_load_work, complete_load_work, out_time,
          unload_wait_time, load_wait_time, entry_to_unload,
           entry_to_load, arrive_to_complete_unload, arrive_to_complete_load,
          complete_to_exit_unload, complete_to_exit_load, unload_to_load, visible) => {
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
            entryTime: entryTime,
            arrive_unload_spot : arrive_unload_spot,
            start_unload_work: start_unload_work,
            complete_unload_work:complete_unload_work,

            arrive_load_spot : arrive_load_spot,
            start_load_work : start_load_work,
            complete_load_work : complete_load_work,
            
            entry_to_unload:entry_to_unload,
            entry_to_load:entry_to_load,
            arrive_to_complete_unload:arrive_to_complete_unload,
            arrive_to_complete_load:arrive_to_complete_load,
            complete_to_exit_unload:complete_to_exit_unload,
            complete_to_exit_load:complete_to_exit_load,
            unload_to_load:unload_to_load,
            out_time : out_time,
            //계산 제대로 안됨 계산은 다 서버에서 하고 넘어와야 할 듯함
            
            unload_wait_time: unload_wait_time,
            load_wait_time: load_wait_time,
            visible : visible
        };
        setTrucks(trucks => [...trucks, truck]);
    }
   
    const drawTruck = (truck, ctx) => {
        if (truck.visible) {
            ctx.fillStyle = 'orange';
            ctx.fillRect(truck.x, truck.y, truck.width, truck.height);
            ctx.fillStyle = 'black';
            ctx.fillText(`${truck.name} : ${truck.work_code}`, truck.x, truck.y-10);
            if(truck.work_code==='in'){
                ctx.font = "15px Arial";
                ctx.fillText(`unload_wait_time: ${truck.unload_wait_time}`, truck.x, truck.y - 30); // truck's unload wait time
            }
            else if(truck.work_code==='out'){
                ctx.font = "15px Arial";
                ctx.fillText(`load_wait_time: ${truck.load_wait_time}`, truck.x, truck.y - 30); // truck's unload wait time
            }
            else{
                ctx.font = "15px Arial";
                ctx.fillText(`unload_wait_time: ${truck.unload_wait_time}`, truck.x, truck.y - 30); // truck's unload wait time
                ctx.fillText(`load_wait_time: ${truck.load_wait_time}`, truck.x, truck.y - 50); // truck's unload wait time
            }

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
                            truck.x += truck.speed*3.2/truck.entry_to_unload*1000;
                        }
                        else {
                            truck.state = 1;
                        }
                    }
                    else if (truck.state === 1) {
                        truck.delay += 1;
                        // 5초 설정
                        if (truck.delay > truck.arrive_to_complete_unload*50/1000) {
                            truck.x += 80;
                            truck.state = 2;
                        }
                    }
                    else if (truck.state === 2) {
                        if (truck.x < canvas.width - truck.width) {
                            truck.x += truck.speed*3.2/truck.complete_to_exit_unload*1000;
                        }
                        else {
                            truck.visible = false;
                        }
                    }
                }

                if(truck.work_code === 'out'){
                    if (truck.state ===0){
                        if (truck.x < 200 - truck.width) {
                            //계산 잘못됨 다시 해보기
                            //truck.x += (truck.speed*truck.entry_to_spot/(400 - truck.width));
                            truck.x += truck.speed*4.7/truck.entry_to_load*1000;
                        }
                        else{
                            truck.state =5;
                        }
                    }
                    else if (truck.state ===5){
                        if(truck.y < 300- truck.height){
                            //truck.y += (truck.speed*truck.entry_to_spot/(400 - truck.width));
                            truck.y +=  truck.speed*4.7/truck.entry_to_load*1000;
                        }
                        else{
                            truck.state =6;
                        }
                    }
                    else if ( truck.state ===6){
                        if (truck.x < 400 - truck.width) {
                            //entry_to_spot 도 서버에서 계산해서 넘어와야 할 듯, 여기서 하니까 제대로 작동 안함
                            truck.x +=  truck.speed*4.7/truck.entry_to_load*1000;
                            //truck.x += truck.speed;
            
                        }
                        else{
                            truck.state = 1;
                        }
                    }
                    else if (truck.state === 1){
                        truck.delay += 1;
                        // 5초 설정
                        if(truck.delay>truck.arrive_to_complete_load*50/1000){
                            truck.x +=80;
                            truck.state=4;
                        }
                    }
                    else if (truck.state ===4){
                        if(truck.x<680-truck.width){
                            truck.x += truck.speed*4.7/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.state = 3;
                        }
                    }
                    else if(truck.state ===3){
                        if(truck.y>150-truck.height){
                            truck.y-= truck.speed*4.7/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.state = 2;
                        }
                    }
                    else if (truck.state ===2){
                        if(truck.x < canvas.width - truck.width){
                            truck.x += truck.speed*4.7/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.visible = false;
                        }
                    }
                }

                if(truck.work_code === 'in_out'){
                    // 속도 계산해야 함
                    if (truck.state ===0){
                        // 초당 100px 이동중
                        if (truck.x < 400 - truck.width) {
                            truck.x += truck.speed*3.2/truck.entry_to_unload*1000;
                        }
                        else{
                            truck.state =1;
                        }
                    }
                    else if (truck.state ===5){
                        if(truck.y < 300- truck.height){
                            truck.y += truck.speed*2.5/truck.unload_to_load*1000;
                        }
                        else{
                            truck.state =7;
                        }
                    }

                    else if (truck.state === 1){
                        truck.delay += 1;
                        // 5초 설정 250번의 호출(20밀리세컨드 기준)
                        if(truck.delay>truck.arrive_to_complete_unload*50/1000){
                            truck.x +=80;
                            truck.state=5;
                            truck.delay=0;
                        }
                    }
                    else if (truck.state === 7){
                        truck.delay += 1;
                        // 5초 설정
                        if(truck.delay>truck.arrive_to_complete_load*50/1000){
                            truck.state=4;
                        }
                    }
                    else if (truck.state ===4){
                        if(truck.x<680-truck.width){
                            truck.x += truck.speed*4.7/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.state = 3;
                        }
                    }
                    else if(truck.state ===3){
                        if(truck.y>150-truck.height){
                            truck.y-=truck.speed*4.7/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.state = 2;
                        }
                    }
                    else if (truck.state ===2){
                        if(truck.x < canvas.width - truck.width){
                            truck.x += truck.speed*4.7/truck.complete_to_exit_load*1000;
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
                createTruck(truckData.number, truckData.code, truckData.entryTime, truckData.arrive_unload_spot,
                    truckData.start_unload_work, truckData.complete_unload_work, truckData.arrive_load_spot,
                     truckData.start_load_work, truckData.complete_load_work, truckData.out_time,
                      truckData.unload_wait_time, truckData.load_wait_time, truckData.entry_to_unload,
                       truckData.entry_to_load, truckData.arrive_to_complete_unload, truckData.arrive_to_complete_load,
                      truckData.complete_to_exit_unload, truckData.complete_to_exit_load, truckData.unload_to_load,truckData.visible);
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

