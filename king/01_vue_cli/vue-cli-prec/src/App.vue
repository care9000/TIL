<template>
  <div id="app">
    <todo-list category="취업준비"></todo-list>
    <TodoList category="취업준비"></TodoList>
    <todo-list category="취업준비"></todo-list>
  </div>

</template>

<script>
import TodoList from './components/TodoList.vue'
import GetDog from './components/GetDog.vue'

export default {
  name: 'app',
  components: {
    TodoList,
    GetDog,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
