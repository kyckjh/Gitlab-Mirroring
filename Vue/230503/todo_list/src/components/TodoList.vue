<template>
  <div id="app">
    <ul>
      <TodoListItem v-for="todo in todoList" :key="todo.date"
        :todo="todo"
        @click-check-box="handleCheckEvent(todo)" 
      />

    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  props: {
    todoList: Array,
  },
  methods: {
    handleCheckEvent(todo) {
      this.$emit('click-check-box', todo)
    }
  }
}
</script>

<style>

</style>
