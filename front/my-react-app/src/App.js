import {BrowserRouter, Route, Routes} from 'react-router-dom'
import './App.css';
import Display from './simul/Display';
import Mainpage from './simul/Mainpage';

function App() {

  return (
   
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path = "/" element = {<Mainpage/>}/>
        <Route path = "/display" element = {<Display/>}/>
      </Routes>
      </BrowserRouter>
     </div>
     
  );
};

export default App;
