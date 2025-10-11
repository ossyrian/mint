<script lang="ts">
  import { link } from 'svelte-spa-router';

  // Mock data for demo purposes
  const mockListings = [
    { id: 1, name: 'Zakum Helmet', price: '100,000,000', seller: 'Player1' },
    { id: 2, name: 'Dragon Khanjar', price: '50,000,000', seller: 'Player2' },
    { id: 3, name: 'Red Snowboard', price: '25,000,000', seller: 'Player3' },
  ];
</script>

<div class="container mx-auto px-4 py-8">
  <div class="mb-8">
    <h1 class="h1 mb-4">Item Listings</h1>
    <p class="text-surface-400">Browse available items on the marketplace</p>
  </div>

  <div class="mb-6 flex gap-4">
    <input
      type="text"
      placeholder="Search items..."
      class="input flex-1"
    />
    <button class="btn variant-filled-primary">Search</button>
  </div>

  <div class="grid gap-4">
    {#each mockListings as listing}
      <a use:link href="/mogul/item/{listing.id}" class="card card-hover p-6 flex justify-between items-center">
        <div>
          <h3 class="h4 mb-1">{listing.name}</h3>
          <p class="text-surface-400">Seller: {listing.seller}</p>
        </div>
        <div class="text-right">
          <p class="text-2xl font-bold text-primary-500">{listing.price}</p>
          <p class="text-sm text-surface-400">mesos</p>
        </div>
      </a>
    {/each}
  </div>

  {#if mockListings.length === 0}
    <div class="card p-8 text-center">
      <p class="text-surface-400">No listings found. Check back later!</p>
    </div>
  {/if}
</div>
