import React, { useEffect, useState, useRef } from "react";
import { Student as StudentType, Attendance as AttendanceType } from "../utils/types";
import { useParams } from "react-router";

interface StudentProps {}

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

export const Student = ({}: StudentProps) => {
  const [student, setStudent] = useState<StudentType>(undefined as never);
  const [attendances, setAttendances] = useState<AttendanceType[]>(undefined as never);
  const { id } = useParams<string>();

  useEffect(() => {
    let cancel = true;
    
      fetch(`/api/attendances/${id}`)
      .then((res) => res.json())
      .then((data) => {
        //if(cancel = false) {
          data.sort((a, b) => (a.date > b.date) ? 1 : -1)
          setAttendances(data);
        //}



      });
      fetch(`/api/students/${id}/details`)
      .then((res) => res.json())
      .then((data) => {
        setStudent(data);
      });

  }, []);

  if (attendances == null) 
    return <p>Loading</p>;
 
  return (
      <div>
        <h1>Student</h1>
        {student && (
          <div>
            <p>
              {student.user.first_name} {student.user.last_name} (id: {id})
            </p>
            <p>
              Course: {student.course.name} (id: {student.course.id})
            </p>
            <p>
              Mentor: {student.section.mentor.user.first_name}{" "}
              {student.section.mentor.user.last_name}
            </p>
              Attendance:
              {attendances.map((attendance) => (
                <li key={attendance.id}>
                  <label >{attendance.date}:</label>
              <form>
              
                <select name="cars" id="cars" 
                onChange={(event) => {
                let value = event.target.value;
                const data = {
                  attendance_id: attendance.id,
                  value: value,
                }
                fetch(`/api/attendances/${attendance.id}/details/`, {
                  method: "POST",
                  headers: {'Content-Type': 'application/json', 'X-CSRFToken':`${csrftoken}`}, 
                  body: JSON.stringify(data)
                }).then(res => {
                  console.log("Request complete! response:", res);
                });
              }}>
                  <option value="UN">Unexcaused Absent</option>
                  <option value="PR">Present</option>
                  <option value="EX">Excused Absent</option>
                </select>
              </form>
            </li>
          ))}
              
          </div>
        )}
      </div>
    );
  
  
};
