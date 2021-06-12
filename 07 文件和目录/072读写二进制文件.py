fileImage1 = '076Test1.png'
fileImage2 = '076Test2.png'


def D1():
    with open(fileImage1, 'rb') as file:
        image = file.read()
        with open(fileImage2, 'wb') as file2:
            file2.write(image)


if __name__ == "__main__":
    D1()
