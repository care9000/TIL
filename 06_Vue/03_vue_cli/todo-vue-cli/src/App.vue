<template>
  <div>
    <h1>여기는 최상위 컴포넌트</h1>
    <TodoList category="스타벅스"></TodoList>
    <TodoList category="다이어트"></TodoList>
    <TodoList category="요가"></TodoList>
  </div>
</template>



<script>
import TodoList from './components/TodoList.vue'
export default {
  components: {
    TodoList,
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
