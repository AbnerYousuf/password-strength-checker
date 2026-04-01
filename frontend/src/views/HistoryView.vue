<template>
  <div class="p-4 max-w-4xl mx-auto">
    <h2 class="text-2xl font-semibold mb-6">Password Audit History</h2>

    <div v-if="passwordHistory.length === 0">
      No passwords audited yet. Try out the
      <RouterLink :to="{ name: 'home' }">Home</RouterLink> page!
    </div>

    <div v-else class="flex flex-col gap-4">
      <div
        v-for="(entry, index) in [...passwordHistory].reverse()"
        :key="index"
        class="bg-white rounded-lg shadow p-4"
      >
        {{ entry.password }} - {{ entry.results.score }}/4 - {{ entry.results.guesses }} guesses
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { usePasswordStore } from '@/stores/passwordStore'

const store = usePasswordStore()

const passwordHistory = store.passwordHistory
</script>
