<script lang="ts">
  import { link } from "svelte-spa-router";

  export let params: { id: string } = { id: "1" };

  // Mock data for demo purposes
  const itemDetails = {
    id: params.id,
    name: "Zakum Helmet",
    price: "100,000,000",
    seller: "Player1",
    description:
      "A powerful helmet dropped by Zakum. Provides excellent defense and stat bonuses.",
    stats: [
      { name: "DEF", value: "+100" },
      { name: "STR", value: "+10" },
      { name: "DEX", value: "+10" },
      { name: "INT", value: "+10" },
      { name: "LUK", value: "+10" },
    ],
    postedDate: "2 days ago",
  };
</script>

<div class="container mx-auto px-4 py-8">
  <div class="mb-4">
    <a
      use:link
      href="/mogul/listings"
      class="text-primary-500 hover:text-primary-400"
    >
      ← Back to Listings
    </a>
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
    <div class="card p-6">
      <div
        class="aspect-square bg-surface-600 rounded-lg flex items-center justify-center mb-4"
      >
        <p class="text-surface-400">Item Image</p>
      </div>
      <h1 class="h2 mb-2">{itemDetails.name}</h1>
      <p class="text-surface-400 mb-4">
        Posted {itemDetails.postedDate} by {itemDetails.seller}
      </p>
      <p class="text-surface-300">{itemDetails.description}</p>
    </div>

    <div class="space-y-6">
      <div class="card p-6">
        <h2 class="h3 mb-4">Item Stats</h2>
        <div class="space-y-2">
          {#each itemDetails.stats as stat}
            <div
              class="flex justify-between items-center p-2 rounded bg-surface-700"
            >
              <span class="font-semibold">{stat.name}</span>
              <span class="text-primary-400">{stat.value}</span>
            </div>
          {/each}
        </div>
      </div>

      <div class="card p-6">
        <h2 class="h3 mb-4">Purchase</h2>
        <div class="flex items-baseline gap-2 mb-4">
          <span class="text-4xl font-bold text-primary-500"
            >{itemDetails.price}</span
          >
          <span class="text-surface-400">mesos</span>
        </div>
        <button class="btn variant-filled-primary w-full" disabled>
          Buy Now (Coming Soon)
        </button>
      </div>

      <div class="card p-6">
        <h2 class="h3 mb-4">Seller Information</h2>
        <p class="text-surface-300">Username: {itemDetails.seller}</p>
        <p class="text-surface-400 text-sm mt-2">
          More seller details coming soon
        </p>
      </div>
    </div>
  </div>
</div>
