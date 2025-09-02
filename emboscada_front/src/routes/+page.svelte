<script lang="ts">
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcomeFallback from '$lib/images/svelte-welcome.png';
	import logo from '$lib/images/logo.png';
</script>

<svelte:head>
	<title>Fogón</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>
		Chipería Emboscada
		
		<span class="welcome">
			<picture>
				<!-- <source srcset={welcome} type="image/webp" /> -->
				<!-- <img src={welcomeFallback} alt="Welcome" /> -->
				<img src={logo} alt="Chipería Emboscada" />
			</picture>
		</span>

		
	</h1>

	<!-- <h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2> -->

	<!-- <Counter /> -->
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
	    padding: 0 0 calc(100% * 495 / 2048) 0;
		
		
	}
    
	

	.welcome img {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
		z-index: -1;
		}
</style>
