<template>
{{props.password}}
{{props.results.score}}
{{ props.results.guesses }}
{{props.results.feedback.suggestions}}
{{props.results.feedback.warning}}
{{ props.results.crack_times_display}} }}
</template>

<script setup lang="ts">
import type { ResultsList } from '@/stores/types'

const props = defineProps<{
  password: string
  results: ResultsList
}>()
</script>