<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<nav class="flex items-center justify-between p-4 bg-gray-800 text-white">
	<h1>FS Student Manager</h1>
	<ul class="flex space-x-4">
		<li><a href="/">Home</a></li>
		<li><a href="/students">Students</a></li>
	</ul>
</nav>

{@render children?.()}
