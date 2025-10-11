<script lang="ts">
  import { link } from "svelte-spa-router";
</script>

<div class="container mx-auto px-4 py-8">
  <div class="text-center mb-12">
    <h1 class="h1 mb-4">Welcome to Mint</h1>
    <p class="text-xl text-surface-400">
      Your MapleStory community hub
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
    <!-- MintyMogul -->
    <div class="card p-8 variant-ghost-primary">
      <div class="mb-6">
        <h2 class="h2 mb-2">MintyMogul</h2>
        <p class="text-surface-300 text-lg">
          Auction House Marketplace
        </p>
      </div>
      <p class="text-surface-400 mb-6">
        Buy and sell items, equipment, and rare collectibles. Find the perfect gear for your character or turn your inventory into mesos.
      </p>
      <a use:link href="/mogul" class="btn variant-filled-primary w-full">
        Browse Marketplace
      </a>
    </div>

    <!-- MintyHQ -->
    <div class="card p-8 variant-ghost-secondary">
      <div class="mb-6">
        <h2 class="h2 mb-2">MintyHQ</h2>
        <p class="text-surface-300 text-lg">
          Guild Registry
        </p>
      </div>
      <p class="text-surface-400 mb-6">
        Discover guilds, manage your guild roster, and connect with other players. Build your community in MapleStory.
      </p>
      <a use:link href="/guilds" class="btn variant-filled-secondary w-full">
        View Guilds
      </a>
    </div>
  </div>
</div>
