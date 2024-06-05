
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data