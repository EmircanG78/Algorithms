import heapq # Python'da öncelik sırası olan kuyruk (priority queue) için kullanılır.
# En düşük öncelikli elemanı almak için kullanılır.

class Node:
    def __init__(self, name, g=0, h=0):
        self.name = name    # düğüm adı
        self.g = g  # başlangıçtan buraya olan maliyet
        self.h = h  # hedefe olan tahmini maliyet / heuristik

    def f(self):
        return self.g + self.h  # toplam maliyet
    
    #   Bu __lt__ (less than) metodu Python'da '<' operatörünü temsil ediyor.
    #   2 düğüm arasında karşılaştırma yapar ve 
    #   F değeri düşük olan Node'lar önce gelir, çünkü öncelikli olarak işlenir.
    def __lt__(self, other):
        return self.f() < other.f() # heapq sıralaması için 
    
    def a_star(start, goal, graph, heuristics):
        # A* algoritmasını başlatır.
        # start: başlangıç düğümü
        # goal: hedef düğümü
        # graph: düğümler ve komşuları (komşu, maliyet)
        # heuristics: her düğümün hedege olan tahmini uzaklığı (H değeri)

        open_list = []  # ziyaret edilmesi gereken düğümleri tutar. F değeri en düşük olan başa gelir.
        closed_list = set() # ziyaret edilmiş düğümleri tutar.

        start_node = Node(start, g=0, h =heuristics[start]) # başlangıç düğümü, g değeri 0 ve h değeri heuristik
        heapq.heappush(open_list,start_node)    # başlangıç düğümünü açık listeye ekler, heapq kendisi sıralar.

        while open_list:
            # Açık liste boşalana kadar devam eder.
            # Her turda sıradaki en düşük F değerine sahip düğümü ziyaret eder.
            current = heapq.heappop(open_list) # Açık listedeki en düşük F değerine sahip düğüm çıkarılır ve ziyaret edilir.
            print(f"Ziyaret edilen düğüm:{current.name} (F={current.f()})")

            if current.name == goal:    # Hedef düğüme ulaşılırsa algoritmayı bitirir.
                print("Hedefe ulaşıldı.")
                return
            
            closed_list.add(current.name)  # Ziyaret edilen düğümü listeye ekler.

            for neighbor, cost in graph[current.name]:
                # Şu anki düğümün komşularını ve maliyetlerini döner. 
                if neighbor in closed_list:
                    continue
                # Komşu düğüm daha önce ziyaret edilmişse onu atlar.

                g = current.g + cost    # Mevcut düğümün G değeri + komşuya gitme maliyeti
                h = heuristics[neighbor]    # Komşunun hedefe olan tahmini uzaklığı
                neighbor_node = Node(neighbor,g,h)  # Komşu düğüm oluşturulur. G ve H değerleriyle yeni bir Node oluşturur.

                heapq.heappush(open_list,neighbor_node) # yeni düğümü açık listeye ekliyoruz, liste F değerine göre sıralanır.

# Grafik: düğümler ve komşuları (komşu, maliyet)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

# Heuristik (tahmini mesafeler)
heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}

# A* çalıştır
Node.a_star('A', 'G', graph, heuristics)
# Başlangıç düğümü: A
# Hedef düğüm: G
# Graf ve heuristik verileri kullanılarak yol aranır.     