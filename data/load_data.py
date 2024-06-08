
def load_data(file_path):
    text = ""
    with open(file_path, 'r') as file:
        text += file.read()
    return text