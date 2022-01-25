
FILE_LOC = '/home/app/config/hosts'

def add_host(host, endpoint):
    in_file = False
    content = []
    with open(FILE_LOC, "r") as f:
        lines = f.readlines()
        for line in lines:
            if endpoint in line:
                in_file = True
                content.append(f"{host} {endpoint}")
            else:
                content.append(line)

    if not in_file:
        content.append(f"{host} {endpoint}\n")

    with open(FILE_LOC, "w") as f:
        f.writelines(content)


