<script lang="ts">
  import { goto } from '$app/navigation';
  import { accessToken } from '$lib/stores/authStore';
  import { apiFetch } from '$lib/utils/fetch';

  let username = '';
  let password = '';
  let message = '';
  let isError = false;

  // Redirect if already logged in
  accessToken.subscribe(token => {
    if (token) goto('/');
  });

  async function handleSubmit() {
    message = '';
    isError = false;

    try {
      // Call apiFetch with form encoding
      const data = await apiFetch('/auth/token', {
        method: 'POST',
        auth: false,              // don’t attach JWT yet
        contentType: 'form',      // FastAPI OAuth2 expects form-urlencoded
        body: { username, password }
      });

      // If successful → store token
      localStorage.setItem('access_token', data.access_token);
      accessToken.set(data.access_token);

      message = 'Login successful!';
      isError = false;
      goto('/'); // redirect to home/dashboard
    } catch (err: any) {
      message = `Login failed: ${err.message}`;
      isError = true;
    }
  }
</script>

<form on:submit|preventDefault={handleSubmit} class="flex flex-col gap-4">
  <div class="form-control">
    <label class="label" for="username">
      <span class="label-text">Username</span>
    </label>
    <input
      id="username"
      name="username"
      type="text"
      placeholder="Enter your username"
      bind:value={username}
      class="input input-bordered w-full"
      required
      autocomplete="username"
    />
    </div>
    <div class="form-control">
      <label class="label" for="password">
        <span class="label-text">Password</span>
      </label>
      <input
        id="password"
        name="password"
        type="password"
        placeholder="Enter your password"
        bind:value={password}
        class="input input-bordered w-full"
        required
        autocomplete="current-password"
      />
    </div>
    <button type="submit" class="btn btn-primary mt-4">Login</button>
    <p class="mt-6 text-center text-gray-600 text-sm">
        Don't have an account? <a href="/signup" class="text-blue-600 hover:underline">Sign up here</a>.
    </p>
</form>