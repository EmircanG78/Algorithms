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

            if current.name == goal:
                print("Hedefe ulaşıldı.")
                return
            
            closed_list.add(current.name)

            for neighbor, cost in graph[current.name]:
                if neighbor in closed_list:
                    continue

                g = current.g + cost
                h = heuristics[neighbor]
                neighbor_node = Node(neighbor,g,h)

                heapq.heappush(open_list,neighbor_node)

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

    

        