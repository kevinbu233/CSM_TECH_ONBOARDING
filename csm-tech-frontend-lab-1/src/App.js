import './App.css';
import {useEffect} from 'react';
import Resources from './components/Resources.js'

const App = () => {
  useEffect(() => {
    document.title = "CSM Tech Lab 1";
  }, [])

  return (
    <div className="App">
      <Resources />
    </div>
  );


}

export default App;
