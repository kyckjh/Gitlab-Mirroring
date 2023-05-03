<template>
  <div id="app">
    <h1>App</h1>
      <input type="text" v-model="appData">
    <p>Parent Data : {{ parentData }}</p>
    <p>Child Data : {{ childData }}</p>
    <AppParent :app="appData"
      @child-input="handleChildInput"
      @parent-input="handleParentInput"
    />
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  data() {
    return {
      appData: '',
      childData : '',
      parentData : '',
    }
  },
  components: {
    AppParent,
  },
  methods:{
    handleChildInput(childData){
      this.childData = childData
    },
    handleParentInput(parentData){
      this.parentData = parentData
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
