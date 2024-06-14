<template>
    <div class="modal fade" id="addTodoModal" tabindex="-1" aria-labelledby="addTodoModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="addTodoModalLabel">Add ToDo</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="addTodo">
              <div class="mb-3">
                <label for="todoBody" class="form-label">ToDo</label>
                <textarea class="form-control" id="todoBody" v-model="todoBody" rows="3" required></textarea>
              </div>
              <div class="mb-3">
                <label for="todoEndDate" class="form-label">End Date</label>
                <input type="date" class="form-control" id="todoEndDate" v-model="todoEndDate" required>
              </div>
              <div class="mb-3">
                <label for="personName" class="form-label">Person Name</label>
                <input type="text" class="form-control" id="personName" v-model="personName" required>
              </div>
              <div class="mb-3">
                <label for="personImage" class="form-label">Person Image</label>
                <input type="file" class="form-control" id="personImage" @change="onImageChange" required>
              </div>
              <button type="submit" class="btn btn-primary">Add ToDo</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        todoBody: '',
        todoEndDate: '',
        personName: '',
        personImage: null
      };
    },
    methods: {
      addTodo() {
        // Handle adding the ToDo item
      },
      onImageChange(event) {
        this.personImage = event.target.files[0];
      }
    }
  };
  </script>
  