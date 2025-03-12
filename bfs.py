from collections import deque # sıra (queue) yapısı için kullanılan kütüphane

# Grafik yapısı(şehirler veya kişiler arasındaki ilişkiler gibi) için bir sözlük yapısı kullanıyoruz.
# Bu sözlük yapısında her düğümün komşuları listelenmiştir.
# Örneğin A düğümünün komşuları D ve C'dir.
# Bu grafik yapısını kullanarak BFS algoritmasını uygulayacağız.
# BFS algoritması, düğümleri genişlik öncelikli olarak gezer.
# Yani bir düğümün tüm komşularını ziyaret ettikten sonra o düğümün komşularını ziyaret eder.
# Bu algoritma genellikle kısa mesafelerde kullanılır.
grafik = {
    'A': ['D', 'C'],
    'B': ['C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['F'],
    'E': [],
    'F': []
}

def bfs(başlangıç):

    sira = deque() # ziyaret edilecek düğümleri tutan sıra(queue) yapısı
    ziyaret_edildi = [] # ziyaret edilen düğümleri tutan liste
    
    sira.append(başlangıç) # başlangıç noktasını sıraya ekliyoruz

    while sira: # sıra boş olana kadar döngüyü sürdür
        # sıradan bir yer alıyoruz
        düğüm = sira.popleft()

        # eğer daha önce ziyaret etmediysek 
        if düğüm not in ziyaret_edildi:

            print(düğüm) # düğümü ekrana yazdırıyoruz
            ziyaret_edildi.append(düğüm)

            # düğümün komşularını sıraya ekliyoruz
            for komşu in grafik[düğüm]:
                sira.append(komşu)

# BFS i başlatıyoruz
bfs('A')






