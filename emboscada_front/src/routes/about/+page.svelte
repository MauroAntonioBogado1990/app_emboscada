<script lang="ts">
	
	import chipatradicional from '$lib/images/chipatradicional.jpg';
	import chipachedar from '$lib/images/chipachedar.jpg';
	let countTradicional = 0;
	let countCheddar = 0;

</script>

<svelte:head>
	<title>Tu Ronda de Chipas</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="text-column">
	<h1>Nuestras Chipas</h1>

	<p>
		En la herencia que hemos recibido de mis abuelos y padres, es el amor por el terruños y nuestras tradiciones litoraleñas, <br/>
		de ese amor nace este empredimiento de poder mostrar nuestra querencia en sabores y poder traer un pedacito de nuestra tierra
		,recuerdos de nuestros seres queridos a cada uno de ustedes.
	</p>
    <h1>Variedades</h1>
	<h1><strong>Chipa tradicional</strong></h1>
	<picture>
			<img src={chipatradicional} alt="Chipería Tradicional" />
	</picture>
	<h3>Receta clásica, con almidón, queso </h3>
	<div class="contador">
	<button on:click={() => countTradicional--} disabled={countTradicional === 0}>-</button>
	<span>{countTradicional}</span>
	<button on:click={() => countTradicional++}>+</button>
    </div>
	
	<!---->
	<h1><strong>Chipa dorada</strong></h1>
	<picture>
		<img src={chipachedar} alt="Chipería Chedar" />
	</picture>
	<h3>Chipa con Queso Chedar</h3>	
    <div class="contador">
		<button on:click={() => countCheddar--} disabled={countCheddar === 0}>-</button>
		<span>{countCheddar}</span>
		<button on:click={() => countCheddar++}>+</button>
   </div>
  

		

	

	
</div>
<style>
	picture {
		display: flex;
		justify-content: center;
		align-items: center;
	}
    img {
		
		max-width: 50%;
		height: auto;
		border-radius: 10%	;
	}	
	.contador {
		display: flex;
		align-items: center;
		gap: 1rem;
		margin-bottom: 2rem;
	}

	button {
		background-color: #d4a373;
		color: white;
		border: none;
		padding: 0.5rem 1rem;
		font-size: 1.2rem;
		cursor: pointer;
		border-radius: 5px;
	}

	button:disabled {
		opacity: 0.5;
		cursor: not-allowed;
	}

	span {
		font-size: 1.5rem;
		font-weight: bold;
	}

</style>