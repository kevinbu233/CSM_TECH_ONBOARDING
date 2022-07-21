export interface User {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
}

//add Course interface
export interface Course {
  id: number;
  name: string;
}

export interface Mentor {
  id: number;
  user: User;
  course: Course;
}

//add Section interface
export interface Section {
  id: number;
  mentor?: Mentor;
  capacity: number;
  description?: string;
}

//add Student interface
export interface Student {
  id: number;
  user?: User;
  section?: Section;
  course?: Course;
  active?: boolean;
  banned?: boolean;
}
