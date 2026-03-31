<template>
<div class="flex flex-col flex-center items-start bg-white rounded-lg shadow-lg p-4 w-full max-w-md">
  <div>Auditing Password: {{props.password}}</div>
  <div>Score: {{props.results.score}}</div>
  <div>Guesses: {{ props.results.guesses }}</div>
  <div>Suggestions: {{props.results.feedback.suggestions}}</div>
  <div>Warning: {{props.results.feedback.warning}}</div>
  <div>Crack Times: {{ props.results.crack_times_display}}</div>
</div>
</template>

<script setup lang="ts">
import type { ResultsList } from '@/stores/types'

const props = defineProps<{
  password: string
  results: ResultsList
}>()
</script>