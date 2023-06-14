import { useNavigate } from "react-router-dom";
import './simul.css'
import { useState } from "react";
import simulatorinput from './imageTerminal/simulatorinput.png'
import canvasimage from './imageTerminal/canvasimage.png'
import dashboard2 from './imageTerminal/dashboard2.png'
import chart3 from './imageTerminal/chart3.png'
import { ClipLoader } from 'react-spinners'

const DescribePage = () =>{
    const navigate = useNavigate();
    const [trucknum, setTrucknum] = useState();
    const [processtime, setProcesstime] = useState();
    const [blocknum, setBlocknum] = useState();
    const [isLoading, setIsLoading] = useState(false);
    
    const EnterQueuePage =async(event)=>{
        event.preventDefault();

        try{
            setIsLoading(true);
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
            setIsLoading(false);
        }
        catch(error){
            setIsLoading(false);
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
    let rightArrow = "\u2192";
    let leftArrow = "\u2190";
    let upArrow = "\u2191";
    let downArrow = "\u2193";
    return(

        <div className="describeOuter">
            <h1>Queue Predict Simulator</h1>
            <h4>본 서비스는 컨테이너 야드 내 컨테이너 반출입 트럭의 Queue를 Simulation하여 차량수, 블록수, 시간에 따른 대기차량 현황를 확인할 수 있습니다.</h4>
            <h4>또한, 시뮬레이터로 생성된 데이터를 이용한 딥러닝 예측모델의 결과값을 확인할 수 있습니다.</h4>
            <h3>구성</h3>
            <div className="describeInner">
                <div className="inner01">
                    <div className="desText">
                        <p id="describeInTitle">시뮬레이션 화면1</p>
                        <div className="textleft">
                            <p id="describeIncont">- 컨테이너 터미널 차량 이동 및 대기 시각화(CANVAS)</p>
                            <p id="describeIncont">- 입력값(차량수, 블록수, 시간)반영한 시뮬레이션 생성</p>
                            <p id="describeIncont">- 야드 내 트럭 입차 {rightArrow} 작업장 {rightArrow} 출차 이동</p>
                            <p id="describeIncont">- 초당 화면 50회 호출을 통한 이동 구현</p>
                        </div>
                    </div>
                    <div className="desgif">
                        <img id='img01' src={canvasimage} alt="canvas image"/>
                    </div>
                </div>
                <div className="inner01">
                    <div className="desText">
                        <p id="describeInTitle">시뮬레이션 화면2</p>
                        <div className="textleft">
                            <p id="describeIncont">- 컨테이너 터미널 블록별 대기차량 현황(DASHBOARD)</p>
                            <p id="describeIncont">- 총 입∙출차한 차량 수, 반입장 대기차량, 반출장 대기차량</p>
                        </div>
                    </div>
                    <div className="desgif">
                        <img id='img01' src={dashboard2} alt="dashboard image"/>
                    </div>
                </div>

                <div className="inner01">
                    <div className="desText">
                        <p id="describeInTitle">시뮬레이션 화면3</p>
                        <div className="textleft">
                            <p id="describeIncont">- 컨테이너 터미널 내 차량수 예측(CHART)</p>
                            <p id="describeIncont">- 딥러닝 모델(LSTM, CNN)을 통한 예측</p>
                            <p id="describeIncont">- 모델 학습 동안 손실함수를 최소화하는 방향으로 요인 간의 가중치를 업데이트하여 예측치 산출</p>
                        </div>
                    </div>
                    <div className="desgif">
                        <img id='img01' src={chart3} alt="chart image"/>
                    </div>
                </div>

                <div className="inner01">
                    <div className="desText">
                        <p id="describeInTitle">시뮬레이션 기본값 설정</p>
                        <p>시뮬레이션 및 예측 시작</p>
                        <div className="textleft">
                            <p id="describeIncont">- 차량수(대), 반출입 블록수, 실행시간(초) 입력</p>
                            <p id="describeIncont">- Queue 시작 버튼 클릭</p>
                        </div>
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
            {isLoading ? <ClipLoader size={100} color={'#123abc'} loading={isLoading} /> : null}
        </div>
    )
}
export default DescribePage;