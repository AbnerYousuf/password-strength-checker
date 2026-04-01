<template>
  <div class="flex flex-col items-start bg-white rounded-lg shadow-lg p-6 w-full max-w-md">
    <h3 class="text-lg font-semibold mb-4">Audit Results For: {{ password }}</h3>

    <!-- Strength Meter -->
    <div class="w-full mb-4">
      <div class="flex justify-between items-center mb-2">
        <span class="text-sm font-medium">Strength</span>
        <span class="text-sm font-semibold" :class="ratingColor[1]">{{ passwordStrength }}</span>
      </div>
      <div class="w-full bg-gray-200 rounded-full h-3 overflow-hidden">
        <div
          class="h-full transition-all duration-300 ease-out"
          :style="{ width: barSize + '%' }"
          :class="ratingColor[0]"
        ></div>
      </div>
    </div>

    <!-- Score Info -->
    <div class="grid grid-cols-2 gap-4 w-full border-t mt-4 pt-4">
      <div>
        <p class="text-teal-600 text-xs">Score</p>
        <p class="font-semibold">{{ props.results.score }}/4</p>
      </div>
      <div>
        <p class="text-teal-600 text-xs">Guesses to crack</p>
        <p class="font-semibold">{{ props.results.guesses }}</p>
      </div>
    </div>

    <!-- Warning -->
    <div v-if="props.results.feedback.warning" class="w-full border-t mt-4 pt-4">
      <p class="text-sm text-red-600 font-medium">{{ props.results.feedback.warning }}</p>
    </div>

    <!-- Suggestions -->
    <div v-if="props.results.feedback.suggestions.length > 0" class="w-full border-t mt-4 pt-4">
      <p class="text-sm font-medium mb-2">Suggestions:</p>
      <ul class="text-sm text-gray-700 space-y-1">
        <li
          v-for="(suggestion, index) in props.results.feedback.suggestions"
          :key="index"
          class="flex items-start"
        >
          <span class="mr-2">•</span>
          <span>{{ suggestion }}</span>
        </li>
      </ul>
    </div>

    <!-- Crack Times -->
    <div class="w-full mt-4 pt-4 border-t">
      <p class="text-sm font-medium mb-2">Time to crack:</p>
      <div class="text-xs text-gray-600 space-y-1">
        <div
          v-for="(time, method) in props.results.crack_times_display"
          :key="method"
          class="flex justify-between"
        >
          <span class="capitalize">{{ fixUnderscores(method) }}:</span>
          <span class="font-medium">{{ time }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { ResultsList } from '@/stores/types'

const props = defineProps<{
  password: string
  results: ResultsList
}>()

// this takes in score and returns a percentage for the meter width (0-4 converted to 0-100%)
const barSize = computed(() => ((props.results.score + 1) / 5) * 100)

// this provides color based on score using tailwidncss
const ratingColor = computed(() => {
  const score = props.results.score
  switch (score) {
    case 0:
      return ['bg-red-600', 'text-red-600']
    case 1:
      return ['bg-orange-600', 'text-orange-600']
    case 2:
      return ['bg-yellow-600', 'text-yellow-600']
    case 3:
      return ['bg-lime-600', 'text-lime-600']
    case 4:
      return ['bg-green-600', 'text-green-600']
    default:
      return ['bg-gray-600', 'text-gray-600']
  }
})

const passwordStrength = computed(() => {
  const score = props.results.score
  switch (score) {
    case 0:
      return 'Very Weak'
    case 1:
      return 'Weak'
    case 2:
      return 'Fair'
    case 3:
      return 'Good'
    case 4:
      return 'Very Strong'
    default:
      return 'Error'
  }
})

// remove the underscores
const fixUnderscores = (stringToReplace: string): string => {
  return stringToReplace.replace(/_/g, ' ')
}
</script>
