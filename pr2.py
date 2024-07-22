class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []

    def insert_text(self, new_text):
        self.undo_stack.append(self.text)
        self.text += new_text

    def delete_text(self, num_chars):
        self.undo_stack.append(self.text)
        self.text = self.text[:-num_chars]

    def undo(self):
        if self.undo_stack:
            self.text = self.undo_stack.pop()

    def get_undo_list(self):
        return self.undo_stack

    def get_current_text(self):
        return self.text

# Example usage:
editor = TextEditor()

editor.insert_text("Hello, ")
print(editor.get_current_text())  # Output: Hello,
editor.insert_text("world!")
print(editor.get_current_text())  # Output: Hello, world!
editor.undo()
print(editor.get_current_text())  # Output: Hello,
editor.undo()
print(editor.get_current_text())  # Output: (empty string)

print("Undo list:")
for i, text in enumerate(editor.get_undo_list()):
    print(f"{i+1}. {text}")
