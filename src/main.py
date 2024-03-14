from converter import Converter



if __name__ == "__main__":
    conv = Converter()

    while True:
        command = input("AAS: ")
        command = command.split()
        if command[0] == "load":
            filename = command[1]
            conv.load(filename)
        elif command[0] == "render":
            conv.render()
        elif command[0] == "info":
            conv.info()
        elif command[0] == "quit":
            break