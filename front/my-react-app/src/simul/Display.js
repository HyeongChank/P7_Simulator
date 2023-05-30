import React, { useState, useEffect, useRef } from 'react';
import './simul.css'
function Display(){
    const [mousePos, setMousePos] = useState({x:0, y:0});
    const [trucksData, setTrucksData] = useState([]);
    const [blockA, setBlockA] = useState();
    const [blockB, setBlockB] = useState();
    const [blockC, setBlockC] = useState();
    const [blockD, setBlockD] = useState();
    const [blockE, setBlockE] = useState();
    const [blockQ, setBlockQ] = useState();
    const [blockW, setBlockW] = useState();
    const [blockX, setBlockX] = useState();
    const [blockY, setBlockY] = useState();
    const [blockZ, setBlockZ] = useState();
    const [blockuntotal, setBlockuntotal] = useState();
    const [blocktotal, setBlocktotal] = useState();
    const [blockAt, setBlockAt] = useState();
    const [blockBt, setBlockBt] = useState();
    const [blockCt, setBlockCt] = useState();
    const [blockDt, setBlockDt] = useState();
    const [blockEt, setBlockEt] = useState();
    const [blockQt, setBlockQt] = useState();
    const [blockWt, setBlockWt] = useState();
    const [blockXt, setBlockXt] = useState();
    const [blockYt, setBlockYt] = useState();
    const [blockZt, setBlockZt] = useState();
    const [entryt, setEntryt] = useState();
    const [color, setColor] = useState();

    const [blockAp, setBlockAp] = useState();
    const [blockBp, setBlockBp] = useState();
    const [blockCp, setBlockCp] = useState();
    const [blockDp, setBlockDp] = useState();
    const [blockEp, setBlockEp] = useState();
    const [blockQp, setBlockQp] = useState();
    const [blockWp, setBlockWp] = useState();
    const [blockXp, setBlockXp] = useState();
    const [blockYp, setBlockYp] = useState();
    const [blockZp, setBlockZp] = useState();

    const [outcount, setOutcount] = useState(0);
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
    const out_count = () =>{
        setOutcount(outcount +1)
    }
    
    const createTruck = (number, code, entryTime, arrive_unload_spot,
        start_unload_work, complete_unload_work, arrive_load_spot,
         start_load_work, complete_load_work, out_time,
         unload_count, load_count,
          unload_wait_time, load_wait_time, entry_to_unload,
           entry_to_load, arrive_to_complete_unload, arrive_to_complete_load,
          complete_to_exit_unload, complete_to_exit_load, unload_to_load,
          unload_block, load_block, entry_count, exit_count, color,
          unload_progress_truck_count, load_progress_truck_count, visible) => {
        
        const canvas = canvasRef.current;
       
        const truck = {
            number: number,
            name: 'truck' + number,
            x: 0,
            y: canvas.height - 500,
            width: 50,
            height: 50,
            speed: 2,
            delay: 0,
            state: 0,
            work_code: code,
            entryTime: entryTime,
            arrive_unload_spot : arrive_unload_spot,
            start_unload_work: start_unload_work,
            complete_unload_work:complete_unload_work,
            color:getRandomColor(),
            arrive_load_spot : arrive_load_spot,
            start_load_work : start_load_work,
            complete_load_work : complete_load_work,
            unload_count:unload_count,
            load_count:load_count,
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
            unload_block:unload_block,
            load_block:load_block,
            entry_count:entry_count,
            exit_count:0,
            unload_progress_truck_count:unload_progress_truck_count,
            load_progress_truck_count:load_progress_truck_count,
            visible : visible,
 
        };

        setTrucks(trucks => [...trucks, truck]);
    }
    function getRandomColor() {
        const r = Math.floor(Math.random() * 256); // 랜덤한 빨간색 채널값
        const g = Math.floor(Math.random() * 256); // 랜덤한 초록색 채널값
        const b = Math.floor(Math.random() * 256); // 랜덤한 파란색 채널값
        return `rgb(${r},${g},${b})`;

    }
    const drawTruck = (truck, ctx) => {


        if (truck.visible) {
            ctx.fillStyle = truck.color;
            ctx.fillRect(truck.x, truck.y, truck.width, truck.height);
            ctx.fillStyle = 'black';
            ctx.font = "15px Arial";
            ctx.fillText(`${truck.name} : ${truck.work_code}`, truck.x, truck.y-10);
            if(truck.work_code==='unload' && mousePos.x >= truck.x && mousePos.x <= truck.x + truck.width && mousePos.y >= truck.y && mousePos.y <= truck.y + truck.height){
                ctx.font = "15px Arial";
                ctx.fillText(`반입 대기시간: ${truck.unload_wait_time/1000}m`, truck.x, truck.y - 30); // truck's unload wait time
                ctx.fillText(`반입장: ${truck.unload_block}`, truck.x, truck.y - 50); // truck's unload wait time
             
            }
            else if(truck.work_code==='load' && mousePos.x >= truck.x && mousePos.x <= truck.x + truck.width && mousePos.y >= truck.y && mousePos.y <= truck.y + truck.height){
                ctx.font = "15px Arial";
                ctx.fillText(`반출 대기시간: ${truck.load_wait_time/1000}m`, truck.x, truck.y - 30); // truck's unload wait time
                ctx.fillText(`반출장: ${truck.load_block}`, truck.x, truck.y - 50); // truck's unload wait time
            }
            else if(truck.work_code==='both' && mousePos.x >= truck.x && mousePos.x <= truck.x + truck.width && mousePos.y >= truck.y && mousePos.y <= truck.y + truck.height){
                ctx.font = "15px Arial";
                ctx.fillText(`반출 대기시간: ${truck.load_wait_time/1000}m`, truck.x, truck.y - 30); // truck's unload wait time
                ctx.fillText(`반입 대기시간: ${truck.unload_wait_time/1000}m`, truck.x, truck.y - 50); // truck's unload wait time
                ctx.fillText(`반입장: ${truck.unload_block} 반출장: ${truck.load_block}`, truck.x, truck.y - 70); // truck's unload wait time
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
                setEntryt(truck.entryTime);
                setBlockuntotal(blockA+blockB+blockC+blockD+blockE);
                setBlocktotal(blockQ+blockW+blockX+blockY+blockZ);
                const unloadCountElement = document.getElementById('unload_count');
                const loadCountElement = document.getElementById('load_count');
                const unloadBlockElement = document.getElementById('unload_block');
                const loadBlockElement = document.getElementById('load_block');
                const entryCountElement = document.getElementById('entry_count');
                // const exitCountElement = document.getElementById('exit_count');
                entryCountElement.textContent = `${truck.entry_count}`;
                // exitCountElement.textContent = `${truck.exit_count}`;
                unloadCountElement.textContent = `${truck.unload_count}`;
                loadCountElement.textContent = `${truck.load_count}`;
                unloadBlockElement.textContent = `${truck.unload_block} : `;
                loadBlockElement.textContent = `${truck.load_block} : `;

                if(truck.unload_block ==='A'){
                    setBlockAp(truck.unload_progress_truck_count);
                    setBlockA(truck.unload_count);
                    setBlockAt(truck.unload_wait_time/1000);
                }
                if(truck.unload_block ==='B'){
                    setBlockBp(truck.unload_progress_truck_count);                    
                    setBlockB(truck.unload_count);
                    setBlockBt(truck.unload_wait_time/1000);
                }
                if(truck.unload_block ==='C'){
                    setBlockCp(truck.unload_progress_truck_count);
                    setBlockC(truck.unload_count);
                    setBlockCt(truck.unload_wait_time/1000);
                }
                if(truck.unload_block ==='D'){
                    setBlockDp(truck.unload_progress_truck_count);
                    setBlockD(truck.unload_count);
                    setBlockDt(truck.unload_wait_time/1000);
                }
                if(truck.unload_block ==='E'){
                    setBlockEp(truck.unload_progress_truck_count);
                    setBlockE(truck.unload_count);
                    setBlockEt(truck.unload_wait_time/1000);
                }

                if(truck.load_block ==='Q'){
                    setBlockQp(truck.load_progress_truck_count);
                    setBlockQ(truck.load_count);
                    setBlockQt(truck.load_wait_time/1000);
                }
                if(truck.load_block ==='W'){
                    setBlockWp(truck.load_progress_truck_count);
                    setBlockW(truck.load_count);
                    setBlockWt(truck.load_wait_time/1000);
                }
                if(truck.load_block ==='X'){
                    setBlockXp(truck.load_progress_truck_count);
                    setBlockX(truck.load_count);
                    setBlockXt(truck.load_wait_time/1000);
                }
                if(truck.load_block ==='Y'){
                    setBlockYp(truck.load_progress_truck_count);
                    setBlockY(truck.load_count);
                    setBlockYt(truck.load_wait_time/1000);
                }
                if(truck.load_block ==='Z'){
                    setBlockZp(truck.load_progress_truck_count);
                    setBlockZ(truck.load_count);
                    setBlockZt(truck.load_wait_time/1000);
                }


                if (truck.work_code === 'unload') {
 
                    if (truck.state === 0) {
                        if (truck.x < 400 - truck.width) {
                            truck.x += truck.speed*3.5/truck.entry_to_unload*1000;
                        }
                        else {
                            truck.state = 1;
                        }
                    }
                    else if (truck.state === 1) {
                        truck.delay += 1;
                        // 5초 설정
                        if (truck.delay > truck.arrive_to_complete_unload*50/1000) {
                            truck.x += 50;
                            truck.state = 2;
                        }
                    }
                    else if (truck.state === 2) {
                        if (truck.x < canvas.width - truck.width) {
                            truck.x += truck.speed*3.5/truck.complete_to_exit_unload*1000;
                        }
                        else {
                            truck.visible = false;
                            truck.exit_count +=1;
                            out_count();
                            truck.state = 99;
                        }
                    }
                    
                }

                if(truck.work_code === 'load'){
                    if (truck.state ===0){
                        if (truck.x < 200 - truck.width) {
                            //계산 잘못됨 다시 해보기
                            //truck.x += (truck.speed*truck.entry_to_spot/(400 - truck.width));
                            truck.x += truck.speed*5.0/truck.entry_to_load*1000;
                        }
                        else{
                            truck.state =5;
                        }
                    }
                    else if (truck.state ===5){
                        if(truck.y < 300- truck.height){
                            //truck.y += (truck.speed*truck.entry_to_spot/(400 - truck.width));
                            truck.y +=  truck.speed*5.0/truck.entry_to_load*1000;
                        }
                        else{
                            truck.state =6;
                        }
                    }
                    else if ( truck.state ===6){
                        if (truck.x < 400 - truck.width) {
                            //entry_to_spot 도 서버에서 계산해서 넘어와야 할 듯, 여기서 하니까 제대로 작동 안함
                            truck.x +=  truck.speed*5.0/truck.entry_to_load*1000;
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
                            truck.x +=50;
                            truck.state=4;
                        }
                    }
                    else if (truck.state ===4){
                        if(truck.x<650-truck.width){
                            truck.x += truck.speed*5.0/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.state = 3;
                        }
                    }
                    else if(truck.state ===3){
                        if(truck.y>150-truck.height){
                            truck.y-= truck.speed*5.0/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.state = 2;
                        }
                    }
                    else if (truck.state ===2){
                        if(truck.x < canvas.width - truck.width){
                            truck.x += truck.speed*5.0/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.visible = false;
                            truck.exit_count +=1;
                            out_count();
                            truck.state = 99;
                        }
                    }
                }

                if(truck.work_code === 'both'){
                    // 속도 계산해야 함
                    if (truck.state ===0){
                        // 초당 100px 이동중
                        if (truck.x < 400 - truck.width) {
                            truck.x += truck.speed*3.5/truck.entry_to_unload*1000;
                        }
                        else{
                            truck.state =1;
                        }
                    }
                    else if (truck.state ===5){
                        if(truck.y < 300- truck.height){
                            truck.y += (truck.speed*1.5/truck.unload_to_load)*1000;
                        }
                        else{
                            truck.state =7;
                        }
                    }

                    else if (truck.state === 1){
                        truck.delay += 1;
                        // 5초 설정 250번의 호출(20밀리세컨드 기준)
                        if(truck.delay>truck.arrive_to_complete_unload*50/1000){
                            truck.x +=50;
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
                        if(truck.x<650-truck.width){
                            truck.x += truck.speed*5.0/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.state = 3;
                        }
                    }
                    else if(truck.state ===3){
                        if(truck.y>150-truck.height){
                            truck.y-=truck.speed*5.0/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.state = 2;
                        }
                    }
                    else if (truck.state ===2){
                        if(truck.x < canvas.width - truck.width){
                            truck.x += truck.speed*5.0/truck.complete_to_exit_load*1000;
                        }
                        else{
                            truck.visible = false;
                            truck.exit_count +=1;
                            out_count();
                            truck.state = 99;
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
                     truckData.unload_count, truckData.load_count,
                      truckData.unload_wait_time, truckData.load_wait_time, truckData.entry_to_unload,
                       truckData.entry_to_load, truckData.arrive_to_complete_unload, truckData.arrive_to_complete_load,
                      truckData.complete_to_exit_unload, truckData.complete_to_exit_load, truckData.unload_to_load,
                      truckData.unload_block, truckData.load_block, truckData.entry_count, truckData.exit_count, color,
                      truckData.unload_progress_truck_count, truckData.load_progress_truck_count, truckData.visible);
            }, truckData.entryTime);
        });
    };

    return (
        <div>
            <h1>컨테이너 야드 현황</h1>
            <h2>목표 : Queue 최적화</h2>
            <canvas ref={canvasRef} width={800} height={600}
            onMouseMove={e=>{
                var rect = e.target.getBoundingClientRect();
                setMousePos({x:e.clientX - rect.left, y:e.clientY - rect.top});
            }}  />
            <button onClick={handleClick}>Start</button>
            <div id='dashb'>
            <div id='dashboard'>
                <div id= 'entry_exit_ds'>
                    <p>입차(대) : <span id='entry_count'> 0</span></p>
                    <p>입차시간(초) : {entryt/1000}</p>
                    <span>출차(대) : </span>
                    <span id='exit_count'>{outcount}</span>
                    {/* <span id='exit_count'>출차 : 0</span> */}
                </div>
                <div id='unload5'>
                    <p className='unloadP'>반입장 대기차량 : <span>{blockuntotal}</span></p>
                    
                    
                    <span id='unload_block'>unload_block : </span>
                    <span id='unload_count'>unload_count</span>
                    <p id='unload'>block : 작업 | 대기 | 대기시간</p>
                    <p id='unload'>blockA : {blockAp}대, {blockA}대, {blockAt}</p>
                    <p id='unload'>blockB : {blockBp}대, {blockB}대, {blockBt}</p>
                    <p id='unload'>blockC : {blockCp}대, {blockC}대, {blockCt}</p>
                    <p id='unload'>blockD : {blockDp}대, {blockD}대, {blockDt}</p>
                    <p id='unload'>blockE : {blockEp}대, {blockE}대, {blockEt}</p>
                </div>
                <div id='load5'>
                    <p className='loadP'>반출장 대기차량 : <span>{blocktotal}</span></p>
                    <span id='load_block'>load_block : </span>
                    <span id='load_count'>load_count</span>
                    <p id='unload'>block : 작업 | 대기 | 대기시간</p>
                    <p id='load'>blockQ : {blockQp}대, {blockQ}대, {blockQt}</p>
                    <p id='load'>blockW : {blockWp}대, {blockW}대, {blockWt}</p>
                    <p id='load'>blockX : {blockXp}대, {blockX}대, {blockXt}</p>
                    <p id='load'>blockY : {blockYp}대, {blockY}대, {blockYt}</p>
                    <p id='load'>blockZ : {blockZp}대, {blockZ}대, {blockZt}</p>
                </div>
        

             
            </div>
            </div>

        </div>
    );
}

export default Display

