<template>
  <div v-if="passwordHistory.length === 0">
    No passwords audited yet. Try out the <RouterLink :to="{ name: 'home' }">Home</RouterLink> page!
  </div>
  <div v-else>To be implemented</div>
</template>

<script setup lang="ts">
import { usePasswordStore } from '@/stores/passwordStore'

const store = usePasswordStore()

const passwordHistory = store.passwordHistory
</script>
