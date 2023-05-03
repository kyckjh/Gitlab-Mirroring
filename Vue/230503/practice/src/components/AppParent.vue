<template>
  <div>
    <h1>AppParent</h1>
      <input type="text" v-model="parentData"
    @keyup.enter="emitParentInputEvent">
    <p>App Data : {{ app }}</p>
    <p>Child Data : {{ childData }}</p>
    <AppChild :app="app" :parent="parentData" 
    @child-input="handleChildInput"/>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'

export default {
  name: "AppParent",
  props: {
    app: String,
  },
  data() {
    return {
      parentData: '',
      childData: '',
    }
  },
  components: {
    AppChild,
  },
  methods: {
    handleChildInput(childData) {
      this.childData = childData
      this.$emit('child-input',childData)
    },
    emitParentInputEvent(){
      this.$emit('parent-input',this.parentData)
    }
  }
}
</script>

<style>

</style>