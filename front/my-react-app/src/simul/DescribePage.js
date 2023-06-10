import { useNavigate } from "react-router-dom";
import './simul.css'
import { useState } from "react";
import simulatorinput from './imageTerminal/simulatorinput.png'
import canvasimage from './imageTerminal/canvasimage.png'
import dashboard2 from './imageTerminal/dashboard2.png'
import chart3 from './imageTerminal/chart3.png'

const DescribePage = () =>{
    const navigate = useNavigate();
    const [trucknum, setTrucknum] = useState();
    const [processtime, setProcesstime] = useState();
    const [blocknum, setBlocknum] = useState();
    
    const EnterQueuePage =async(event)=>{
        event.preventDefault();

        try{
            const response = await fetch('http://localhost:8081/api/inputDataPost',{
                method: 'POST',
                headers:{
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({
                    trucknum: trucknum,
                    processtime:processtime,
                    blocknum:blocknum
                }),
            });
            if(!response.ok){
                throw new Error('postdata error');
            }
            // ResponseEntity 받을 때 text
            const result = await response.text();
            console.log(result);
            if(result ==='success'){
                navigate('/display')
            }
        }
        catch(error){

        }
    }
    const handleOnchange = (e) =>{
        if(e.target.name === "tn"){
            setTrucknum(e.target.value);
        }
        else if(e.target.name === "bn"){
            setBlocknum(e.target.value);
        }
        else if(e.target.name ==="pt"){
            setProcesstime(e.target.value);
        }
    }
    return(

        <div className="describeOuter">
            <h1>Queue Predict Simulator</h1>
            <h4>본 서비스는 컨테이너 야적장의 컨테이너 반출입 트럭의 Queue를 Simulation하여 차량수, 블록수, 시간에 따른 Queue를 확인할 수 있습니다.</h4>
            <h4>또한, ~~~데이터를 이용하여 딥러닝한 예측모델의 결과값을 확인할 수 있습니다.</h4>
            <h3>내용</h3>
            <div className="describeInner">
                <div className="inner01">
                    <div className="desText">
                        <p id="describeInTitle">시뮬레이션 화면1</p>
                        <p id="describeIncont">- 컨테이너 터미널 차량 이동 및 대기 시각화(CANVAS)</p>
                    </div>
                    <div className="desgif">
                        <img id='img01' src={canvasimage} alt="canvas image"/>
                    </div>
                </div>
                <div className="inner01">
                    <div className="desText">
                        <p id="describeInTitle">시뮬레이션 화면2</p>
                        <p id="describeIncont">- 컨테이너 터미널 블록별 대기차량 현황(DASHBOARD)</p>
                    </div>
                    <div className="desgif">
                        <img id='img01' src={dashboard2} alt="dashboard image"/>
                    </div>
                </div>

                <div className="inner01">
                    <div className="desText">
                        <p id="describeInTitle">시뮬레이션 화면3</p>
                        <p id="describeIncont">- 컨테이너 터미널 내 차량수 예측(CHART)</p>
                        <p id="describeIncont">- 딥러닝 예측모델(LSTM, CNN) 사용</p>
                    </div>
                    <div className="desgif">
                        <img id='img01' src={chart3} alt="chart image"/>
                    </div>
                </div>

                <div className="inner01">
                    <div className="desText">
                        <p id="describeInTitle">시뮬레이션 기본값 설정</p>
                        <p id="describeIncont">- 차량수(대), 반출입 블록수, 실행시간(초) 입력</p>
                        <p id="describeInTitle">시뮬레이션 및 예측 시작</p>
                        <p id="describeIncont">- Queue 시작 버튼 클릭</p>
                    </div>
                    <div className="desgif">
                        <img id='img01' src={simulatorinput} alt="simulator input"/>
                    </div>
                </div>

            </div>
            <div className="inputSpace">
                <p>시뮬레이션 설정</p>
                <form onSubmit={EnterQueuePage}>
                    <label>
                        <span id="inputText">트럭수(대)</span>
                        <input id="inputTrucknum" type="text" name="tn" onChange={handleOnchange}></input>        
                    </label>
                    <label>
                        <span id="inputText">블록수(개)</span>
                        <input id="inputBlocknum" type="text" name="bn" onChange={handleOnchange}></input>        
                    </label>
                    <label>
                        <span id="inputText">실행시간(초)</span>
                        <input id="inputTime" type="text" name="pt" onChange={handleOnchange}></input>        
                    </label>
                    <div className="describeBt">
                        <button id="queueGo" type="submit">Queue 시작</button>
                    </div>
                </form>

                
            </div>
           
        </div>
    )
}
export default DescribePage;