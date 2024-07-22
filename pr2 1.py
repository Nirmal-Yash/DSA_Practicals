def create_text_editor():
    text = ""
    undo_stack = []
    return text, undo_stack

def insert_text(text, undo_stack, new_text):
    undo_stack.append(text)
    text += new_text
    return text, undo_stack

def delete_text(text, undo_stack, num_chars):
    undo_stack.append(text)
    text = text[:-num_chars]
    return text, undo_stack

def undo(text, undo_stack):
    if undo_stack:
        text = undo_stack.pop()
    return text, undo_stack

def get_undo_list(undo_stack):
    return undo_stack

def get_current_text(text):
    return text

text, undo_stack = create_text_editor()

text, undo_stack = insert_text(text, undo_stack, "Hello, ")
print(get_current_text(text))  # Output: Hello,
text, undo_stack = insert_text(text, undo_stack, "world!")
print(get_current_text(text))  # Output: Hello, world!
text, undo_stack = undo(text, undo_stack)
print(get_current_text(text))  # Output: Hello,
text, undo_stack = undo(text, undo_stack)
print(get_current_text(text))  # Output: (empty string)

print("Undo list:")
for i, txt in enumerate(get_undo_list(undo_stack)):
    print(f"{i+1}. {txt}")