import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";
import {Section, Student} from "../utils/types"
import { useParams, NavLink } from "react-router-dom";

function StudentDetail() {
    const [data, setData] = useState<Student>({id:0});
    let params = useParams();
    useEffect(()=> {
      const loadAsyncStuff = async () => {
          const response = await fetch(`/api/students/${params.studentId}/details`);
          const json = await response.json();
          console.log(json)
          setData(json);
      };
      loadAsyncStuff();
    }, []) 

    
  return (
    
    <div>
        <h1>Student</h1>
        <p>
        {data.user?.first_name} {data.user?.last_name} (id:{data.id})
        </p>
        <p>
            Course: {data.course?.name} (id:{data.section?.id})
        </p>
        <p>
            Mentor: {data.section?.mentor?.user.first_name} {data.section?.mentor?.user.last_name}
      
        </p>
    </div>
  );
}

export default StudentDetail;