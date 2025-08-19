<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import web_logo from '/public/web_logo.png'
</script>

<main>
  <div>
    
    <a href="/tu-ronda" class="nav-btn">Tatakua</a>
    <a href="/tu-ronda" class="nav-btn">Tu ronda de chipás</a>
  </div>
  <h1>Chiperia Emboscada</h1>
    <img src={web_logo} alt="Logo Chipería Emboscada" class="web-logo" />

 


  



</main>

<style>
 .web-logo {
    display: block;
    margin: 1rem auto;
    max-width: 500px;
    height: auto;
  }

  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
  .basket {
    display: flex;
    gap: 0.5em;
  }
  .chipa {
    font-size: 2em;
  }

</style>
