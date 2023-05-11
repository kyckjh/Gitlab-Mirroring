<template>
  <div>
    <h1>MyComponent1</h1>
    <h1>Number : {{ number }}</h1>
    <button @click="onClick">+</button>
  </div>
</template>

<script>
export default {
  name: 'MyComponent',
  computed: {
    number() {
      return this.$store.state.number
    }
  },
  methods: {
    onClick(){
      //this.$store.state.number++
      this.$store.commit('ADD_NUMBER', 2)
    }
  }
}
</script>

<style>

</style>