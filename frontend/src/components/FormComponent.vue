<template>
  <form @submit.prevent="checkPassword">
    <input v-model="password" type="text" placeholder="Enter password" />
    <!--it's text because you want to actually see the password you're testing-->
    <div>
      <button
        class="rounded bg-teal-300 hover:bg-teal-400 text-white hover:cursor-pointer px-4 py-2"
        type="submit"
      >
        Check Strength
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const password = ref('')

const checkPassword = async () => {
  try {
    const response = await axios.post('http://localhost:8000/audit', {
      password: password.value,
    })
    console.log(response.data)
  } catch (error) {
    console.error('Error checking password strength:', error)
  }
}
</script>
