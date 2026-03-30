<template>
  test
</template>

<script setup lang="ts">
import axios from 'axios'

const response = await axios.post('http://localhost:8000/audit', {
  password: 'IDontIntendOnCommittingActualPasswordsToGithubIn2026!'
})
console.log(response.data)
</script>
