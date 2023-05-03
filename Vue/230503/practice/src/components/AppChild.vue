<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" v-model="childData" 
      @keyup.enter="emitChildInputEvent">
    <p>App Data : {{ app }}</p>
    <p>Parent Data : {{ parent }}</p>
    <p>Child Data : {{ childData }}</p>
  </div>  
</template>

<script>
export default {
  name: "AppChild",
  props: {
    app: String,
    parent: String,
  },  
  data() {
    return {
      childData: '',
    }
  },
  methods: {
    emitChildInputEvent() {
      this.$emit('child-input',this.childData)
    }
  }
}
</script>

<style>

</style>