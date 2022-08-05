import React, { useState, useEffect } from "react";
import { Section as SectionType, Student } from "../utils/types";
import { Link, useParams } from "react-router-dom";

function getCookie(name) {
  let cookieValue;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');
let changed:boolean = true;
export const Section = () => {
  const [section, setSection] = useState<SectionType>(undefined as never);
  const [students, setStudents] = useState<Student[]>([]);
  const [change, setChange] = useState<Boolean>(false)
  const { id } = useParams<string>();

  
  useEffect(() => {
    fetch(`/api/sections/${id}/details/`)
      .then((res) => res.json())
      .then((data) => {
        setSection(data);
      });
    fetch(`/api/sections/${id}/students/`)
      .then((res) => res.json())
      .then((data) => {
        setStudents(data);
      });
      
  }, []);
  
  useEffect(() => {
    fetch(`/api/sections/${id}/students/`)
      .then((res) => res.json())
      .then((data) => {
        
          setStudents(data);
          setChange(false)
        
      });
      
  }, [change]);


  return (
    <div>
      <h1>Section</h1>
      {section && (
        <div>
          <p>
            {section.mentor.course.name} (id: {id})
          </p>
          <p>
            Mentor: {section.mentor.user.first_name}{" "}
            {section.mentor.user.last_name}
          </p>
        </div>
      )}
      <p>Students:</p>
      <ul>
        {students.map((student) => (
          <li key={student.id}>
            <Link to={`/students/${student.id}`}>
              {student.user.first_name} {student.user.last_name} (id:{" "}
              {student.id})
            </Link> <button type="submit" value={student.id} onClick={(event) => {
                const data = {
                  value: student.id,
                }
                fetch(`/api/sections/${section.id}/students/`, {
                  
                  method: "DELETE",
                  headers: {'Content-Type': 'application/json', 'X-CSRFToken':`${csrftoken}`}, 
                  body: JSON.stringify(data)
                }).then(res => {
                  console.log("Request complete! response:", res);
                });
                setChange(true);
              }}>Drop</button>
          </li>
        ))}
      </ul>
    </div>
  );
};
