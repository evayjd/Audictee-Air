<script setup>
import { ref } from "vue"
import axios from "axios"

const url = ref("")
const sentences = ref([])
const loading = ref(false)

const fetchTranscript = async () => {
  if (!url.value) return

  loading.value = true
  sentences.value = []

  try {
    const res = await axios.post("http://localhost:8000/api/transcript", {
      url: url.value,
    })

    sentences.value = res.data.sentences
  } catch (err) {
    console.error(err)
    alert("API Error")
  }

  loading.value = false
}
</script>

<template>
  <div style="padding: 40px">
    <h1>AI Language Player</h1>

    <input
      v-model="url"
      placeholder="Colle un lien YouTube"
      style="width: 400px; padding: 8px"
    />

    <button @click="fetchTranscript" style="margin-left: 10px">
      Charger
    </button>

    <p v-if="loading">Chargement...</p>

    <div v-for="(s, index) in sentences" :key="index" style="margin-top: 20px">
      {{ s.text }}
    </div>
  </div>
</template>