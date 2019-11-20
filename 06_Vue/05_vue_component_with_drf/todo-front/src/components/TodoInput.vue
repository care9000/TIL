<template>
  <div class="tudo-input">
    <form class="input-group mb-3" @submit.prevent="createTodo">
      <input type="text" class="form-control" v-model="title">
      <button type="submit" class="btn btn-warning">+</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: '',
    }
  },
  methods: {
    createTodo() {
      this.$emit('createTodo', this.title),
      this.title = ''
    }
  }
}
</script>

<style>

</style>