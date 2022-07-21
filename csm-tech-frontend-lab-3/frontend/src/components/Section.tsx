import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";
import {Section, Student} from "../utils/types"
import { useParams, NavLink, Route, Routes } from "react-router-dom";
import StudentDetail from "./Student";

function SectionDetail() {
    const [data, setData] = useState<Section>({id:0, capacity:10});
    const [students, setStudents] = useState<Array<Student>>([{id:0}])
    let params = useParams();
    useEffect(()=> {
      const loadAsyncStuff = async () => {
          const response = await fetch(`/api/sections/${params.sectionId}/details`);
          const studentData = await fetch(`/api/sections/${params.sectionId}/students`);
          const json = await response.json();
          const studentJson = await studentData.json();
          console.log(studentJson)
          setData(json);
          setStudents(studentJson)
      };
      loadAsyncStuff();
    }, []) 

    
  return (
    
    <div>
        <h1>Section</h1>
        <p>
            {data.mentor?.course.name} (id:{data.id})
        </p>
        <p>
            Mentor: {data.mentor?.user.first_name} {data.mentor?.user.last_name}
        </p>
        <p>
            Students:
            {students.map((student) => (
                <li style={{paddingLeft: "10px"}}>
                    <NavLink
                style={{ margin: "1rem 0" }}
                to={`/students/${student.id}`}
                    key={student.id}
                >
            {student.user?.first_name} {student.user?.last_name} (id:{student.user?.id})
            <Routes>
                <Route path="students/:studentId" element={<StudentDetail />} />
            </Routes>
            </NavLink>
            

          </li>))}
        </p>
    </div>
  );
}

export default SectionDetail;