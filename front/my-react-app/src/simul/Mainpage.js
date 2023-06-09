
import { useNavigate } from 'react-router-dom'
import './simul.css'
import { useEffect, useState } from 'react';
import imageterminal5 from '../simul/imageTerminal/terminal5.jpg'
import imageterminal2 from '../simul/imageTerminal/terminal2.jpg'
import imageterminal3 from '../simul/imageTerminal/terminal3.jpg'
import imageterminal6 from '../simul/imageTerminal/terminal6.png'

const Mainpage = () =>{
    const navigate = useNavigate();
    
    const simulpageGo = () =>{
        navigate('/display');
    }

    const getRandomColor=()=>{
        const r = Math.floor(Math.random() * 256); // 랜덤한 빨간색 채널값
        const g = Math.floor(Math.random() * 256); // 랜덤한 초록색 채널값
        const b = Math.floor(Math.random() * 256); // 랜덤한 파란색 채널값
        return `rgb(${r},${g},${b})`;
    }
    const [bgcolor, setBgcolor] = useState(getRandomColor());
    const [bgImage, setBgImage] = useState('');
    const images = [imageterminal5, imageterminal2, imageterminal3, imageterminal6];
    const [imageIndex, setImageIndex] = useState(0);

    useEffect(()=>{
        const interval = setInterval(()=>{
            setBgcolor(getRandomColor());
        },1000);
        return () => clearInterval(interval);
    }, []);
    useEffect(() => {
        const imageInterval = setInterval(() => {
            setImageIndex((prevIndex) => (prevIndex + 1) % images.length);
        }, 2000); // 2초마다 이미지를 변경합니다.

        return () => clearInterval(imageInterval);
    }, []);



    // useEffect(() => {
    //     setBgImage(`url(${images[imageIndex]})`);
    // }, [imageIndex]);

    const handleMouseEnter = () => {
        setBgImage(`url(${images[imageIndex]})`);
    }

    const handleMouseLeave = () => {
        setBgImage('');
    }

    return(

        <div className='mainP' style = {{backgroundColor:bgcolor, backgroundImage:bgImage}}>
            <div>
                <h1><span id='terminal' onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>컨테이너 터미널 현황</span></h1>
                <h2>목표 : 트럭 대기(Queue) 최적화</h2>
            </div>
            <button className="startBt" onClick={simulpageGo}>시작하기</button>
        </div>

    )
}
export default Mainpage;