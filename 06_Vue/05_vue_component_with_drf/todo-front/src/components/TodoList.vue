<template>
  <div class="todo-list">
    <div class="card" v-for="todo in todos" :key="todo.id">
      <div class="card-body" d-flex justify-content-between>
        <span @click="updateTodo(todo)" v-bind:class="{ complete: todo.completed }">{{ todo.title }}</span>
        <span @click="deleteTodo(todo)">[⚾]</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  computed: {
    requestHeader: function() {
      return this.$store.getters.requestHeader
    }
  },
  methods: {
    deleteTodo(todo) {
    //   this.$session.start()
    //   const token = this.$session.get('jwt')
    //   const requestHeader = {
    //     headers: {
    //       Authorization: 'JWT ' + token
    //     }
    //   } 다지움 ㅠㅠ
      axios.delete(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, this.requestHeader)
      .then(res =>{
        console.log(res)
        const targetTodo = this.todos.find(function(el) {
          return el === todo
        })
        const idx = this.todos.indexOf(targetTodo)
        if (idx > -1) {
          this.todos.splice(idx, 1)
        }
      })
      .catch(err => {
        console.log(err)
      })
    },
    updateTodo(todo) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // } 지움 ㅠㅠ
      const requestForm = new FormData()
      requestForm.append('completed', !todo.completed)
      requestForm.append('user', todo.user)
      requestForm.append('id', todo.id)
      requestForm.append('title', todo.title)
      // console.log(!todo.completed, todo.user, todo.id, todo.title)
      axios.put(`http://127.0.0.1:8000/api/v1/todos/${todo.id}/`, requestForm, this.requestHeader)
      .then(res => {
        console.log(res)
        todo.completed = !todo.completed
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
  .complete {
    text-decoration: line-through;
    color: rgb(123,0,255);
  }
</style>