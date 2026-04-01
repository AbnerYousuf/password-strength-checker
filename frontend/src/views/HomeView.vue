<template>
  <div class="min-h-screen flex flex-col items-center justify-center p-4">
    <div><PageHeaderComponent /></div>
    <div><FormComponent /></div>
    <div v-if="lastEntry" class="mt-8 text-teal-600">
      <ResultsComponent :password="lastEntry.password" :results="lastEntry.results" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import PageHeaderComponent from '@/components/PageHeaderComponent.vue'
import FormComponent from '@/components/FormComponent.vue'
import ResultsComponent from '@/components/ResultsComponent.vue'
import { usePasswordStore } from '@/stores/passwordStore'

const store = usePasswordStore()
const lastEntry = computed(() => {
  const history = store.passwordHistory
  return history.length > 0 ? history[history.length - 1] : null
})
</script>
