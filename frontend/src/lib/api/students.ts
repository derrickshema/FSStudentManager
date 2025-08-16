import { apiFetch } from '../utils/fetch';

export async function getStudents() {
  return apiFetch('/students');
}

export async function getStudent(id: string | number) {
  return apiFetch(`/students/${id}`);
}

export async function createStudent(data: any) {
  return apiFetch('/students', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

export async function updateStudent(id: string | number, data: any) {
  return apiFetch(`/students/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  });
}

export async function deleteStudent(id: string | number) {
  return apiFetch(`/students/${id}`, {
    method: 'DELETE',
  });
}