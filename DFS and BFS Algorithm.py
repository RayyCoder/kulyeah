graph = {
    '0' : ['1','2','3'],
    '1' : ['0','2'],
    '2' : ['0','1','4'],
    '3' : ['0'],
    '4' : ['2'],
}
visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end = " ")
    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
print("Urutan Node yang Dikunjungi yaitu: ")
bfs(visited, graph, '0')


# No. 1 : Membuat Graph Sesuai dengan NIM
# NIM: 252410101023
graph = {
'2A' : ['5B','2C',],
'5B' : ['4D', '1E'],
'2C' : ['0F'],
'4D' : ['1H'],
'1E' : ['0I'],
'0F' : ['1G','0J'],
'1G' : ['2K'],
'1H' : [],
'0I' : [],
'0J' : [],
'2K' : ['3L'],
'3L' : []
}

# No. 2 : Memodifikasi kode program BFS dan DFS untuk melakukan penelusuran pada graph NIM diatas

# BFS
visited = [] #untuk menyimpan/menampung node-node yang sudah dikunjungi
queue = [] #untuk menampung node-node yang masih berada dalam antrian untuk dikunjungi

# Membuat fungsi BFS
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)  # Mengambil node paling depan dari queue/antrian
        print(m, end=" ") # Mencetak node yang sedang dikunjungi

        for neighbour in graph[m]:  # Memeriksa semua tetangga (neighbour) dari node 'm'
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Menjalankan kode program BFS diatas dan dimulai dari node '2A'
print("Urutan Node yang Dikunjungi yaitu: ")
bfs(visited, graph, '2A')

# DFS
visited = set()

def dfs(visited, graph, node):
    if node not in visited:       
        print(node, end=" ")      
        visited.add(node)          

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Urutan Node yang Dikunjungi yaitu:")
dfs(visited, graph, '2A') 