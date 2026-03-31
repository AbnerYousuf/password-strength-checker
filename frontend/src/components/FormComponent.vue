<template>
  <form @submit.prevent="checkPassword">
    <div
      class="border-2 border-black bg-white rounded-lg w-full max-w-md shadow-lg mb-2 flex flex-col"
    >
      <input v-model="password" type="text" placeholder="Enter password" />
    </div>
    <!--it's text because you want to actually see the password you're testing-->
    <div>
      <button
        class="rounded bg-teal-300 hover:bg-teal-400 text-white hover:cursor-pointer px-4 py-2 border-teal-600 border-2 w-full max-w-md"
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
