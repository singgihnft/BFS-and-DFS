peta = {'A':set(['B']),
        'B':set(['C','A']),
        'C':set(['B','H','I','D']),
        'D':set(['C','E','H','F']),
        'E':set(['D']),
        'F':set(['D','G']),
        'G':set(['F','H']),
        'H':set(['D','C','G','L']),
        'I':set(['C','J','K']),
        'J':set(['I']),
        'K':set(['L','I']),
        'L':set(['K','H'])}


def dfs(graph, mulai, goal):
    #mengecek semua node
    explored = []
    # mengecek semua jalur
    queue = [[mulai]]

    # kembali ke jalur apabila awal adalah tujuan
    if mulai == goal:
        return "Awal adalah Tujuan"

    # perulangan sampai dengan semua jalur telah diperiksa
    while queue:
        # masukkan antrian paling belakang ke variabel jalur
        jalur = queue.pop(-1)
        # ambil node terakhir dari jalur
        node = jalur[-1]
        if node not in explored:
            neighbours = graph[node]
            # buat jalur baru dan
            # masukan ke dalam queue
            for neighbour in neighbours:
                jalur_baru = list(jalur)
                jalur_baru.append(neighbour)
                queue.append(jalur_baru)
                # kembali ke jalur apa bila cabang benar
                if neighbour == goal:
                    return jalur_baru

            explored.append(node)

    # dalam kasus ini tidak ada node yg diinputkan
    return "Mohon maaf node yang kalian pilih tidak ada"


awal = input("Masukan awal: ")
tujuan = input("Masukan Akhir: ")

print(dfs(peta, awal, tujuan))