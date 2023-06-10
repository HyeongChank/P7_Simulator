import {BrowserRouter, Route, Routes} from 'react-router-dom'
import './App.css';
import Display from './simul/Display';
import Mainpage from './simul/Mainpage';
import DescribePage from './simul/DescribePage';

function App() {

  return (
   
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path = "/" element = {<Mainpage/>}/>
        <Route path = "/display" element = {<Display/>}/>
        <Route path = "/describe" element = {<DescribePage/>}/>
      </Routes>
      </BrowserRouter>
     </div>
     
  );
};

export default App;
