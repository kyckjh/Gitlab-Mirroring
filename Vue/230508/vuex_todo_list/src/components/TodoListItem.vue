<template>
  <li>
    <input type="checkbox" 
    :checked="todo.isCompleted"
    @click="onClickCheckBox"
    >
    <span :class="{done:todo.isCompleted}">{{ todo.content }}</span>
  </li>
</template>

<script>
export default {
  name : 'TodoListItem',
  props : {
    todo : Object,
  },
  methods : {
    onClickCheckBox(){
      //현재 todo 요소의 isCompleted 속성 toggle
      // store 의 todoList 변경을 요청
      // todo의 상태값을 바꿔서 새로운 todo 생성
      const new_todo = {
        ...this.todo,
        isCompleted : !this.todo.isCompleted
      } 
      this.$store.dispatch('updateTodo', new_todo)
    }
  }
}
</script>

<style>
  .done{
    text-decoration: line-through;
    color: gray;
  }
</style>