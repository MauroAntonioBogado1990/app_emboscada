<script lang="ts">

	import chipatradicional from '$lib/images/chipatradicional.jpg';
	import chipachedar from '$lib/images/chipachedar.jpg';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcomeFallback from '$lib/images/svelte-welcome.png';
	import logo from '$lib/images/logo.png';
	let countTradicional = 0;
	let countCheddar = 0;
	let precioTradicional = 1600;
	let precioCheddar = 1700;
    let nombreRetira = '';
	let metodoPago = '';

	/*Agregado de funcion de envío por whatsapp*/
	function enviarPedidoPorWhatsApp() {
	const total = countTradicional * precioTradicional + countCheddar * precioCheddar;

	const mensaje = `Hola! Quiero hacer un pedido:\n
    Chipa Tradicional: ${countTradicional} unidad(es)\n
    Chipa Dorada: ${countCheddar} unidad(es)\n
    Total: $${total}\n
    Retira: ${nombreRetira}\n
    Método de pago: ${metodoPago}`;

	const numero = '549345'; // Reemplazá con el número de WhatsApp de la chipería
	const url = `https://wa.me/${numero}?text=${encodeURIComponent(mensaje)}`;

	window.open(url, '_blank');
}

</script>

<svelte:head>
	<title>Tu Ronda de Chipas</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="text-column">
    <span class="welcome">
			<picture>
				<!-- <source srcset={welcome} type="image/webp" /> -->
				<!-- <img src={welcomeFallback} alt="Welcome" /> -->
				<img src={logo} alt="Chipería Emboscada" />
			</picture>
		</span>


	
    <h1>Variedades</h1>
	<h1><strong>Chipa tradicional</strong></h1>
	
	<picture>
			<img src={chipatradicional} alt="Chipería Tradicional" />
	</picture>
	<h3>Receta clásica, con fécula de mandioca, y queso  </h3>
	<strong>Por unidad de 100 gr cada una</strong>
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
	<h3>Chipa con fécula de mandioca y queso cheddar</h3>
	<strong>Por unidad de 100 gr cada una</strong>
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
		<div class="datos-retiro">
			<label>
				👤 Nombre de quien retira:
				<input type="text" bind:value={nombreRetira} placeholder="Ej. Mauro" /><br/>
			</label>

			<label>
				💰 Método de pago:
				<select bind:value={metodoPago}>
					<option value="" disabled selected>Seleccionar</option>
					<option value="debito">Débito</option>
					<option value="efectivo">Efectivo</option>
					<option value="qr">QR</option>
					<option value="transferencia">Transferencia</option>
				</select>
			</label>
		</div>

		<!-- <button class="confirmar" disabled={!nombreRetira || !metodoPago}>
			Confirmar pedido
		</button> -->
		<button class="confirmar" disabled={!nombreRetira || !metodoPago} on:click={enviarPedidoPorWhatsApp}>
			Confirmar pedido
		</button>

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

.resumen-pedido {
		padding: 1rem;
		background: #fff8f0;
		border-radius: 8px;
		max-width: 400px;
		margin: auto;
	}
	.datos-retiro {
		margin-top: 1rem;
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
	}
	label {
		display: flex;
		flex-direction: column;
		font-weight: bold;
	}
	input, select {
		padding: 0.5rem;
		border-radius: 4px;
		border: 1px solid #ccc;
	}
	.confirmar {
		margin-top: 1rem;
		padding: 0.75rem;
		background-color: #ffcc00;
		border: none;
		border-radius: 6px;
		cursor: pointer;
		font-weight: bold;
	}
	.confirmar:disabled {
		background-color: #ddd;
		cursor: not-allowed;
	}
}
</style>