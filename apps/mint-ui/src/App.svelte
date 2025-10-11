<script lang="ts">
  import Router from 'svelte-spa-router';
  import Layout from './lib/components/Layout.svelte';
  import Landing from './routes/Landing.svelte';
  import MogulHome from './routes/MogulHome.svelte';
  import Listings from './routes/Listings.svelte';
  import ItemView from './routes/ItemView.svelte';
  import GuildsHome from './routes/GuildsHome.svelte';

  const routes = {
    '/': Landing,
    '/mogul': MogulHome,
    '/mogul/listings': Listings,
    '/mogul/item/:id': ItemView,
    '/guilds': GuildsHome,
  };
</script>

<Layout>
  <Router {routes} />
</Layout>
