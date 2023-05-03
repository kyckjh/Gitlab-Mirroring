<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild static-props="components(부모) 에서 child로"
    :my-props="dynamicProps" 
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  data: function() {
    return {
      dynamicProps: "It is a data.."
    }
  },
  methods: {
    parentGetEvent(inputData) {
      alert('자식컴포넌트에서 발생한 이벤트!')
      alert(`child에서 보낸 ${inputData}를 받음`)
    },
    getDynamicData(input) {
      alert(`child에서 입력한 ${input}을 출력`)
    }
  }
}

</script>

<style>
  .border {
    border: solid;
  }
</style>
