import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";
import { Outlet, NavLink } from 'react-router-dom';
import { BrowserRouter as Router, Route, Routes, BrowserRouter } from "react-router-dom";
import SectionDetail from '../components/Section'
import StudentDetail from '../components/Student'
import Routers from '../routes/routes';
//import {Section} from "../utils/types"

 async function getSections() {
  const data = fetch("/api/sections/")
	.then((res) => res.json());
  return await data
}

function App() {
  const [data, setData] = useState<Array<any>>([]);

  useEffect(()=> {
//     const temp = async () => {
//       await fetch("/api/sections/")
//     .then((res) => res.json()).then((data) => {
//       //do whatever you'd like here with the returned json data
//       console.log(data)
//  //     setData(data);
      
//     });
//     }
//     temp()
    const loadAsyncStuff = async () => {
        const response = await fetch("/api/sections/");
        const json = await response.json();
        setData(json);
        console.log(json)
    };
    loadAsyncStuff();

  }, []) 
  // const data = await getSections();

  return (
    <div>
      <h1>Home</h1>
      <nav>
        {data.map((section) => (
          <li style={{paddingLeft: "10px"}}>
            <NavLink
          style={{ margin: "1rem 0" }}
          to={`/sections/${section.id}`}
          key={section.id}
        >
          {section.id}
        </NavLink>
          </li>

        ))}
      </nav>
      <Outlet/>
    </div>
  )
};

export default App;

const wrapper: HTMLElement | null = document.getElementById("app");
wrapper ? ReactDOM.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      {/* <Route path="section" element={<Section />} />
      <Route path="student" element={<Student />} /> */}
      <Route>
          <Route path="sections/:sectionId" element={<SectionDetail />} />
          <Route path="students/:studentId" element={<StudentDetail />} />
            
        </Route>
    </Routes>
  </BrowserRouter>, wrapper) : null;

