<template>
  <div class="container my-5">
    <h1 class="text-center mb-4">Edit ToDo</h1>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <form @submit.prevent="saveChanges">
          <div class="mb-3">
            <label for="editTodoBody" class="form-label">ToDo</label>
            <textarea class="form-control" id="editTodoBody" v-model="todo.body" rows="3" required></textarea>
          </div>
          <div class="mb-3">
            <label for="editTodoEndDate" class="form-label">End Date</label>
            <input type="date" class="form-control" id="editTodoEndDate" v-model="todo.endDate" required>
          </div>
          <div class="mb-3">
            <label for="editPersonName" class="form-label">Person Name</label>
            <input type="text" class="form-control" id="editPersonName" v-model="todo.personName" required>
          </div>
          <div class="mb-3">
            <label for="editPersonImage" class="form-label">Person Image</label>
            <input type="file" class="form-control" id="editPersonImage" @change="onImageChange" required>
          </div>
          <button type="submit" class="btn btn-primary">Save Changes</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todo: {
        body: '',
        endDate: '',
        personName: '',
        personImage: null
      }
    };
  },
  created() {
    // Fetch ToDo item based on route param (id)
  },
  methods: {
    saveChanges() {
      // Handle saving the changes to the ToDo item
    },
    onImageChange(event) {
      this.todo.personImage = event.target.files[0];
    }
  }
};
</script>
