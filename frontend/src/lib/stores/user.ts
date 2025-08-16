import { writable } from 'svelte/store';

export const user = writable(null);

export function setUser(userData: any) {
  user.set(userData);
  if (userData?.token) {
    localStorage.setItem('token', userData.token);
  } else {
    localStorage.removeItem('token');
  }
}