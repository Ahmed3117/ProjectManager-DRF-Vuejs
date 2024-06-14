<template>
  <div class="row mb-3">
    <div class="col">
      <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addTodoModal">Add ToDo</button>
    </div>
    <div class="col">
      <select id="filterStatus" class="form-select" v-model="filterStatus">
        <option value="">Filter by Status</option>
        <option value="pending">Pending</option>
        <option value="done">Done</option>
      </select>
    </div>
    <div class="col">
      <input type="date" id="filterEndDate" class="form-control" v-model="filterEndDate" placeholder="Filter by End Date">
    </div>
  </div>
  <div id="todoList" class="row">
    <todo-item v-for="todo in filteredTodos" :key="todo.id" :todo="todo"></todo-item>
  </div>
  <add-todo-modal></add-todo-modal>
</template>

<script>
import TodoItem from './TodoItem.vue';
import AddTodoModal from './AddTodoModal.vue';

export default {
  components: {
    TodoItem,
    AddTodoModal
  },
  data() {
    return {
      todos: [{
        "id": 1,
        "body": "Complete the project documentation.",
        "end_date": "2023-06-20",
        "person": {
            "id": 1,
            "name": "John Doe",
            "image": "/media/person_images/johndoe.jpg"
        },
        "status": "pending",
        "date_created": "2023-06-13"
    }],
      filterStatus: '',
      filterEndDate: ''
    };
  },
  computed: {
    filteredTodos() {
      // Apply filters and return filtered ToDo list
      return this.todos.filter(todo => {
        return (this.filterStatus ? todo.status === this.filterStatus : true) &&
              (this.filterEndDate ? todo.endDate === this.filterEndDate : true);
      });
    }
  },
  created() {
    // Fetch initial ToDo list
  }
};
</script>
