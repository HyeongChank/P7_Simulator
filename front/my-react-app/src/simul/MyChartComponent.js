import React, { useEffect, useRef } from 'react';
import { Chart, LineController, LinearScale, CategoryScale, LineElement, PointElement } from 'chart.js';

Chart.register(LineController, LinearScale, CategoryScale, LineElement, PointElement);

const MyChartComponent = ({data, truckcount, prediction}) => {

  const chartRef = useRef(null); // 차트를 그릴 캔버스의 ref를 생성
  // spot_wait_time, entryTime  둘 다 1000 나누기
  // useRef 로 렌더링마다 재선언 방지
  const trucklist = useRef([]);
  const predictionlist = useRef([]);
  useEffect(() => {
    if(truckcount !== undefined){
    console.log('truckcount', truckcount)
    console.log('prediction', prediction)
    // list .current로 해야 함
    trucklist.current.push(truckcount)
    predictionlist.current.push(prediction)
    console.log(predictionlist)

    const xValues = data.map(i => i.entryTime/1000);
    const yValues = data.map(i => i.in_yard_count);
    const keyValues = trucklist.current
    const predictpoint = predictionlist.current

    const chart = new Chart(chartRef.current, { // 생성한 ref를 이용해서 차트를 생성
      type: 'line',
      data: {
        labels: xValues,
        datasets: [{
          fill: false,
          tension: 0, // lineTension을 tension으로 변경
          backgroundColor: 'rgba(0,0,255,1.0)',
          borderColor: 'rgba(0,0,255,0.1)',
          data: yValues,
          hidden:true
        },
      {
        fill:false,
        tension:0,
        backgroundColor: 'rgba(100,100,0,1.0)',
        borderColor: 'rgba(255,0,0,0.1)',
        data: predictpoint,
        pointRadius: 2
      },  
      {
        fill:false,
        tension:0,
        backgroundColor: 'rgba(255,0,0,1.0)',
        borderColor: 'rgba(255,0,0,0.1)',
        data: keyValues,
        pointRadius: 2
      }]
      },
      options: {
        plugins: {
          legend: { display: false } // legend는 plugins 하위로 이동
        },
        scales: {
        
          y: { // yAxes를 y로 변경
            ticks: {
              min: 6,
              max: 30
            }
          }
        }
      }
    });

    return () => chart.destroy(); // 컴포넌트가 unmount될 때 차트 인스턴스를 파괴
  }}, [truckcount]);

  return (
    <canvas id='cv' ref={chartRef} ></canvas> // 생성한 ref를 캔버스에 연결
  );
}

export default MyChartComponent;
