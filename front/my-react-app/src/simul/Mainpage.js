
import { useNavigate } from 'react-router-dom'
import './simul.css'

const Mainpage = () =>{
    const navigate = useNavigate();
    const simulpageGo = () =>{
        navigate('/display');
    }
    return(
        <div>
            <button className="startBt" onClick={simulpageGo}>시작하기</button>
        </div>
    )
}
export default Mainpage;