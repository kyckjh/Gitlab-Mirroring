<template>
  <div>
    <h1>로또</h1>
    <button @click="PickLotto">Get Lucky Numbers</button>
    <h4 v-show="numbers.length != 0">{{ numbers }}</h4>
  </div>

</template>

<script>


export default {
  name: 'TheLotto',
  data() {
    return {
      numbers: [],
    }
  },
  methods: {
    PickLotto() {
      this.numbers = []
      let numArray = [...Array(45).keys()]
      for (let i=0; i<6; i++) { 
        let randomValue = Math.floor(Math.random()*numArray.length)
        this.numbers.push(numArray[randomValue]+1)
        numArray.splice(randomValue, 1)
      }
      
    }
  }
}
</script>

<style>

</style>