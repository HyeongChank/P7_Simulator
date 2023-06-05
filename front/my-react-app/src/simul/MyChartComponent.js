import React, { useEffect, useRef } from 'react';
import { Chart, LineController, LinearScale, CategoryScale, LineElement, PointElement } from 'chart.js';

Chart.register(LineController, LinearScale, CategoryScale, LineElement, PointElement);

const MyChartComponent = () => {
  const chartRef = useRef(null); // 차트를 그릴 캔버스의 ref를 생성

  useEffect(() => {
    const xValues = [50,60,70,80,90,100,110,120,130,140,150,80,50,30];
    const yValues = [7,8,8,9,9,9,10,11,14,14,15,16,17,10];

    const chart = new Chart(chartRef.current, { // 생성한 ref를 이용해서 차트를 생성
      type: 'line',
      data: {
        labels: xValues,
        datasets: [{
          fill: false,
          tension: 0, // lineTension을 tension으로 변경
          backgroundColor: 'rgba(0,0,255,1.0)',
          borderColor: 'rgba(0,0,255,0.1)',
          data: yValues
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
              max: 16
            }
          }
        }
      }
    });

    return () => chart.destroy(); // 컴포넌트가 unmount될 때 차트 인스턴스를 파괴
  }, []);

  return (
    <canvas ref={chartRef} style={{width: '100%', maxWidth: '600px'}}></canvas> // 생성한 ref를 캔버스에 연결
  );
}

export default MyChartComponent;
