<script lang="ts">
  import { link } from "svelte-spa-router";
</script>

<div class="container mx-auto px-4 py-8">
  <div class="text-center mb-12">
    <h1 class="h1 mb-4">MintyHQ</h1>
    <p class="text-xl text-surface-400">
      Guild registry for MapleStory
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
    <div class="card p-6 variant-ghost-primary">
      <h2 class="h3 mb-2">Browse Guilds</h2>
      <p class="text-surface-300 mb-4">
        Discover guilds and find the perfect community
      </p>
      <button class="btn variant-filled-primary" disabled>
        Coming Soon
      </button>
    </div>

    <div class="card p-6 variant-ghost-secondary">
      <h2 class="h3 mb-2">Register Guild</h2>
      <p class="text-surface-300 mb-4">Create and manage your guild profile</p>
      <button class="btn variant-filled-secondary" disabled>
        Coming Soon
      </button>
    </div>
  </div>

  <div class="mt-12 text-center">
    <h2 class="h2 mb-6">Featured Guilds</h2>
    <div class="card p-6 max-w-2xl mx-auto">
      <p class="text-surface-400">No guilds registered yet. Check back soon!</p>
    </div>
  </div>
</div>
