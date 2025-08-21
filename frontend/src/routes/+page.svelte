<script lang="ts">
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import { accessToken } from '$lib/stores/authStore';
  import { apiFetch } from '$lib/utils/fetch';
  import type { Student } from '$lib/types/student';
	import { browser } from '$app/environment';

  let students: Student[] = [];
  let message = '';
  let isError = false;
  let isLoading = true;

  // Auto-redirect if not authenticated
  if (browser) {
    accessToken.subscribe(async (token) => {
    if (!token) {
      goto('/login');
    } else {
      await loadStudents();
    }
  });
  }
  

  async function loadStudents() {
    isLoading = true;
    message = '';
    isError = false;

    try {
      const res = await apiFetch('/students/'); // calls backend
      students = res.map((s: any) => ({
        id: s.id,
        firstName: s.first_name,
        lastName: s.last_name
        // map other fields as needed
      }));
      message = 'Students loaded successfully';
    } catch (err: any) {
      isError = true;
      message = err.message || 'Failed to load students';
    } finally {
      isLoading = false;
    }
  }

  onMount(() => {
    // If already logged in, load students immediately
    if (localStorage.getItem('access_token')) {
      loadStudents();
    }
  });
</script>

<h2 class="text-xl font-bold mb-4">Home Page</h2>

{#if isLoading}
  <p>Loading students...</p>
{:else if isError}
  <p class="text-red-600">{message}</p>
{:else}
  {#if students.length > 0}
    <ul class="space-y-2">
      {#each students as student}
        <li class="border p-2 rounded shadow">
          {student.firstName} — {student.lastName}
        </li>
      {/each}
    </ul>
  {:else}
    <p>No students found.</p>
  {/if}
{/if}
