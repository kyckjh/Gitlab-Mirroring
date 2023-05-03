<template>
  <div id="app">
    <h1>오늘의 할 일</h1>
    <p>
      <input type="text" v-model="content">
      <button @click="addTodo">+</button>
    </p>
    <TodoList
      :todo-list="todoList" 
      @click-check-box="handleCheckEvent"     
    />
    <p>
      <button @click="deleteDone">완료 목록 삭제</button>
    </p>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  data() {
    return {
      todoList: [],
      content: '',
    }
  },
  components: {
    TodoList,
  },
  methods: {
    deleteDone() {
      this.todoList = this.todoList.filter((element)=> {
        return !element.isCompleted
      })
    },
    addTodo() {
      const todo = {
        isCompleted: false,
        content: this.content,
        date: new Date().getTime(),
      }
      this.todoList.push(todo)
      this.content = ''
    },
    handleCheckEvent(todo) {
      this.todoList.forEach((element)=>{
        if(element == todo) {
          element.isCompleted = !element.isCompleted
        }
      })      
    }
  },
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
