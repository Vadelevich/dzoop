class TodoList:
    tasks = []
    def add_task(self, add):
        self.tasks.append(add)

todo_list = TodoList()
todo_list.add_task('Купить лампочку')
todo_list.add_task('Поменять лампочку')
todo_list.add_task('Выкинуть лампочку')

print("\n".join(todo_list.tasks))