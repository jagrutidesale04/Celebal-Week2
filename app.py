from flask import Flask, render_template, request, redirect, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return result

    def delete_nth_node(self, n):
        if not self.head:
            raise IndexError("Cannot delete from empty list.")
        if n <= 0:
            raise IndexError("Index must be a positive integer.")
        if n == 1:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(n - 2):
            if not current.next:
                raise IndexError("Index out of range.")
            current = current.next
        if not current.next:
            raise IndexError("Index out of range.")
        current.next = current.next.next

    def delete_middle_node(self):
        elements = self.print_list()
        if not elements:
            raise IndexError("Cannot delete from empty list.")
        middle_index = (len(elements) + 1) // 2
        self.delete_nth_node(middle_index)


# Global LinkedList object
ll = LinkedList()


@app.route('/')
def index():
    elements = ll.print_list()
    return render_template('index.html', elements=" → ".join(elements) if elements else "List is empty.")


@app.route('/add', methods=['POST'])
def add_node():
    data = request.form['data']
    ll.add_node(escape(data))
    flash(f"Added node: {data}", "success")
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete_node():
    try:
        index = int(request.form['index'])
        ll.delete_nth_node(index)
        flash(f"Deleted node at index {index}", "success")
    except (ValueError, IndexError) as e:
        flash(str(e), "danger")
    return redirect('/')


@app.route('/delete-middle', methods=['POST'])
def delete_middle():
    try:
        ll.delete_middle_node()
        flash("Deleted the middle node.", "success")
    except IndexError as e:
        flash(str(e), "danger")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
