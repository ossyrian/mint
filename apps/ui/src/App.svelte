<script lang="ts">
  import Router from 'svelte-spa-router';
  import Layout from './lib/components/Layout.svelte';
  import Home from './routes/Home.svelte';
  import Listings from './routes/Listings.svelte';
  import ItemView from './routes/ItemView.svelte';

  const routes = {
    '/': Home,
    '/listings': Listings,
    '/item/:id': ItemView,
  };
</script>

<Layout>
  <Router {routes} />
</Layout>
