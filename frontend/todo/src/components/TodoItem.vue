<template>
  <div class="col-md-4 mb-4">
    <div class="card">
      <div class="card-body">
        <p>{{ todo.body }}</p>
        <p><strong>End Date:</strong> {{ todo.endDate }}</p>
        <p><strong>Person:</strong> {{ todo.personName }}</p>
        <img :src="todo.personImage" class="todo-img" :alt="todo.personName">
        <p><strong>Status:</strong> {{ todo.status }}</p>
        <p><strong>Date Created:</strong> {{ todo.dateCreated }}</p>
        <button class="btn btn-success btn-sm" @click="markAsDone(todo.id)">Mark as Done</button>
        <router-link :to="{ name: 'EditTodo', params: { id: todo.id }}" class="btn btn-warning btn-sm">Edit</router-link>
        <button class="btn btn-danger btn-sm" @click="deleteTodo(todo.id)">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['todo'],
  methods: {
    markAsDone(id) {
      // Handle marking the ToDo item as done
    },
    deleteTodo(id) {
      // Handle deleting the ToDo item
    }
  }
};
</script>

<style scoped>
.todo-img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
</style>
