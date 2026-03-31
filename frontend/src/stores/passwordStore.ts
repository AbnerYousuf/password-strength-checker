import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { ResultsList } from './types'

export interface PasswordEntry {
  password: string
  results: ResultsList
}

export const usePasswordStore = defineStore('password', () => {
  const passwordHistory = ref<PasswordEntry[]>([])

  const addPasswordEntry = (password: string, results: ResultsList) => {
    passwordHistory.value.push({
      password,
      results,
    })
  }

  const clearHistory = () => {
    passwordHistory.value = []
  }

  return {
    passwordHistory,
    addPasswordEntry,
    clearHistory,
  }
})
