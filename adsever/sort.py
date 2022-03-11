versions_list = ["1.11","2.0.1","1.21","2","0.1","12.2.1","2.1.1","2.0"]
versions_list.sort(key=lambda s: list(map(int, s.split('.'))))
print(versions_list)