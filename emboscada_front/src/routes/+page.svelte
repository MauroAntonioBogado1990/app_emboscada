<script lang="ts">

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
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100%;
	max-width: 300px; /* ajustá según el tamaño que querés */
	margin: 0 auto;
}

.welcome img {
	width: 100%;
	height: auto;
	object-fit: contain;
}

	

</style>
