<template>
  test
</template>

<script setup lang="ts">
import axios from 'axios'

const response = await axios.post('http://localhost:8000/print', {
  password: 'test123'
})
console.log(response.data) // Should print: {"message": "printed: test123"}
</script>
