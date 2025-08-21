export type Student = {
  id: number;
  firstName: string;
  lastName: string;
  dateOfBirth: string; // ISO date string
  gender: string; // '
  enrollmentDate: string; // ISO date string
  grade: string;
  major: string;
  gpa: number; // GPA as a number
  active: boolean; // true if the student is currently enrolled
}