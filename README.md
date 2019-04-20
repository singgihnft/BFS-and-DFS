# Artificial-Intelligence
Kecerdasan Buatan

  Breadth first search (BFS) adalah algoritma yang melakukan pencarian secara melebar yang mengunjungi node secara preorder yaitu mengunjungi suatu node kemudian mengunjungi semua node yang bertetangga dengan node tersebut terlebih dahulu. Selanjutnya, node yang belum dikunjungi dan bertetangga dengan node-node yang tadi dikunjungi , demikian seterusnya. Jika graf berbentuk pohon berakar, maka semua node pada aras d dikunjungi lebih dahulu sebelum node-node pada aras d+1. 
  Algoritma ini memerlukan sebuah antrian q untuk menyimpan node yang telah dikunjungi. Node-node ini diperlukan sebagai acuan untuk mengunjungi node-node yang bertetanggaan dengannya. Tiap node yang telah dikunjungi masuk ke dalam antrian hanya satu kali. 

  Sedangkan  Depth First Search (DFS) adalah salah satu algoritma penelusuran struktur graf / pohon berdasarkan kedalaman. Node ditelusuri dari root kemudian ke salah satu node anaknya ( misalnya prioritas penelusuran berdasarkan anak pertama [Node sebelah kiri] ), maka penelusuran dilakukan terus melalui node anak pertama dari node anak pertama level sebelumnya hingga mencapai level terdalam. 
  Setelah sampai di level terdalam, penelusuran akan kembali ke 1 level sebelumnya untuk menelusuri node anak kedua pada pohon biner [node sebelah kanan] lalu kembali ke langkah sebelumnya dengan menelusuri node anak pertama lagi sampai level terdalam dan seterusnya.
