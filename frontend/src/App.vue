<template>

  <div class="min-h-screen bg-linear-to-br from-white to-teal-200">
    <div> <header>
    <nav class="flex items-center justify-between text-teal-800">
      <ul class="flex space-x-4">
        <li><RouterLink :to="{ name: 'home' }">Home</RouterLink></li>
        <li><RouterLink :to="{ name: 'history' }">History</RouterLink></li>
      </ul>
    </nav>
  </header>
  </div> 
    <div class="flex items-center justify-center p-4"><RouterView /></div>
  </div>
</template>

<script setup lang="ts">
</script>
