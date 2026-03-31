<template>
  <div
    class="min-h-screen bg-linear-to-br from-white to-teal-200 flex flex-col items-center justify-center p-4"
  >
    <div><PageHeaderComponent /></div>
    <div><FormComponent /></div>
  </div>
</template>

<script setup lang="ts">
import PageHeaderComponent from '@/components/PageHeaderComponent.vue'
import FormComponent from '@/components/FormComponent.vue'
</script>
