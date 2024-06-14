import { createRouter, createWebHistory } from 'vue-router';
import TodosView from '../views/TodosView.vue';
import EditTodoView from '../views/EditTodoView.vue';

const routes = [
  {
    path: '/',
    name: 'Todos',
    component: TodosView
  },
  {
    path: '/todo/:id',
    name: 'EditTodo',
    component: EditTodoView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
