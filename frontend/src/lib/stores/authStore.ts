import { writable, type Writable } from 'svelte/store';

// Define and export your access token store
export const accessToken: Writable<string | null> = writable<string | null>(null);