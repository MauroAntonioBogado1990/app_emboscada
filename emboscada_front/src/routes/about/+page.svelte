<script lang="ts">
	
	import chipatradicional from '$lib/images/chipatradicional.jpg';
	import chipachedar from '$lib/images/chipachedar.jpg';
	let countTradicional = 0;
	let countCheddar = 0;
	let precioTradicional = 3000;
	let precioCheddar = 3500;

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
	<h3>Precio: ${precioTradicional}</h3>
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
	<h3>Precio: ${precioCheddar}</h3>
    <div class="contador">
		<button on:click={() => countCheddar--} disabled={countCheddar === 0}>-</button>
		<span>{countCheddar}</span>
		<button on:click={() => countCheddar++}>+</button>
   </div>
    

   <div class="resumen-pedido">
	<h2>🧺 Tu Canasta</h2>
	<ul>
		{#if countTradicional > 0}
			<li>Chipa Tradicional: {countTradicional} unidad(es) — ${countTradicional * precioTradicional}</li>
		{/if}
		{#if countCheddar > 0}
			<li>Chipa Dorada: {countCheddar} unidad(es) — ${countCheddar * precioCheddar}</li>
		{/if}
	</ul>

	<h3>Total: ${countTradicional * precioTradicional + countCheddar * precioCheddar}</h3>

	{#if countTradicional + countCheddar > 0}
		<button class="confirmar">Confirmar pedido</button>
	{/if}
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
    .resumen-pedido {
	background-color: #fefae0;
	padding: 1.5rem;
	border-radius: 10px;
	margin-top: 2rem;
	box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.resumen-pedido h2 {
	color: #bc6c25;
	margin-bottom: 1rem;
}

.resumen-pedido ul {
	list-style: none;
	padding: 0;
	margin-bottom: 1rem;
}

.resumen-pedido li {
	font-size: 1.2rem;
	margin-bottom: 0.5rem;
}

.resumen-pedido h3 {
	font-size: 1.5rem;
	color: #283618;
}

.confirmar {
	background-color: #606c38;
	color: white;
	border: none;
	padding: 0.7rem 1.2rem;
	font-size: 1.1rem;
	border-radius: 5px;
	cursor: pointer;
}
</style>