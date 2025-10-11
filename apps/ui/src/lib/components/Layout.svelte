<script lang="ts">
  import { link } from 'svelte-spa-router';
</script>

<div class="flex flex-col h-full">
  <!-- Header -->
  <header class="bg-surface-700 border-b border-surface-500">
    <div class="container mx-auto px-4 py-4">
      <div class="flex items-center justify-between">
        <a use:link href="/" class="text-2xl font-bold text-primary-500 hover:text-primary-400">
          Mint
        </a>
        <nav class="flex gap-6">
          <a use:link href="/" class="text-surface-100 hover:text-primary-400">Home</a>
          <a use:link href="/listings" class="text-surface-100 hover:text-primary-400">Listings</a>
        </nav>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main class="flex-1 overflow-auto">
    <slot />
  </main>

  <!-- Footer -->
  <footer class="bg-surface-700 border-t border-surface-500 py-4">
    <div class="container mx-auto px-4 text-center text-surface-400">
      <p>Mint - MapleStory Auction House</p>
    </div>
  </footer>
</div>
