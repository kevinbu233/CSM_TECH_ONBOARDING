import { HashRouter as Router, Route, Routes } from "react-router-dom";
import React from "react";
import ReactDOM from "react-dom";
import App from '../components/App'
import Section from '../components/Section'
import Student from '../components/Student'

function Routers() {
    return (<div>Temp</div>
      // <Router>
      //   <Routes>
      //       <Route path="/" element={<App />} />
      //       <Route path="Section" element={<Student />} />
      //       <Route path="Student" element={<Section />} />
      //   </Routes>
      // </Router>
    );
  }
  
  export default Routers;