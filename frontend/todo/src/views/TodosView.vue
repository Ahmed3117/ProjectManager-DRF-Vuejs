<template>
  <div class="container my-5">
    <h1 class="text-center mb-4">ToDo App</h1>
    <todo-list></todo-list>
  </div>
</template>

<script>
import TodoList from '../components/TodoList.vue';

export default {
  components: {
    TodoList
  }
};
</script>
