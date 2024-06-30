from master_graph import *

from master_graph_city import *
from collections import deque

# Creating instance of users
main_server = Graph()
# Creating instnce of cities
south_india_graph = Graph1()

# Function to store the accounts in respective locations
# O(V)
def link_accounts_and_cities(south_india_graph,main_server):
    user_accounts = main_server.vertices()
    for i in user_accounts:
        city = i.location
        find_city = south_india_graph.get_vertex(city)
        find_city.user_accounts.append(i)
    
# Breadth First Search at the same time , checks for range distance
# O(V+E)
def bfs(graph, start_vertex, max_distance):
    visited = set()
    queue = deque([(start_vertex, 0)])
    surrounding_cities = []

    while queue:
        current_vertex, distance = queue.popleft()
        visited.add(current_vertex)

        if distance <= max_distance:
            surrounding_cities.append(current_vertex.city)

            for neighbor, edge in graph.outgoing[current_vertex].items():
                if neighbor not in visited:
                    queue.append((neighbor, distance + edge.weight))

    return surrounding_cities



# Functino to populate the nodes
def populate():
    
    

    # Add cities as vertices
    cities = [
        "Bangalore",
        "Chennai",
        "Hyderabad",
        "Kochi",
        "Mysore",
        "Thiruvananthapuram",
        "Coimbatore",
        "Mangalore",
        "Vijayawada",
        "Visakhapatnam"
    ]

    for city in cities:
        south_india_graph.insertVertex(city)

    # Add edges with distances
    distances = {
        ("Bangalore", "Chennai"): 350,
        ("Bangalore", "Hyderabad"): 570,
        ("Bangalore", "Kochi"): 530,
        ("Bangalore", "Mysore"): 145,
        ("Bangalore", "Thiruvananthapuram"): 730,
        ("Bangalore", "Coimbatore"): 370,
        ("Bangalore", "Mangalore"): 350,
        ("Bangalore", "Vijayawada"): 680,
        ("Bangalore", "Visakhapatnam"): 1080,
        ("Chennai", "Hyderabad"): 630,
        ("Chennai", "Kochi"): 690,
        ("Chennai", "Mysore"): 480,
        ("Chennai", "Thiruvananthapuram"): 720,
        ("Chennai", "Coimbatore"): 500,
        ("Chennai", "Mangalore"): 710,
        ("Chennai", "Vijayawada"): 430,
        ("Chennai", "Visakhapatnam"): 800,
        ("Hyderabad", "Kochi"): 1050,
        ("Hyderabad", "Mysore"): 770,
        ("Hyderabad", "Thiruvananthapuram"): 1270,
        ("Hyderabad", "Coimbatore"): 950,
        ("Hyderabad", "Mangalore"): 750,
        ("Hyderabad", "Vijayawada"): 270,
        ("Hyderabad", "Visakhapatnam"): 700,
        ("Kochi", "Mysore"): 530,
        ("Kochi", "Thiruvananthapuram"): 220,
        ("Kochi", "Coimbatore"): 190,
        ("Kochi", "Mangalore"): 420,
        ("Kochi", "Vijayawada"): 1130,
        ("Kochi", "Visakhapatnam"): 1660,
        ("Mysore", "Thiruvananthapuram"): 640,
        ("Mysore", "Coimbatore"): 260,
        ("Mysore", "Mangalore"): 260,
        ("Mysore", "Vijayawada"): 710,
        ("Mysore", "Visakhapatnam"): 1210,
        ("Thiruvananthapuram", "Coimbatore"): 430,
        ("Thiruvananthapuram", "Mangalore"): 620,
        ("Thiruvananthapuram", "Vijayawada"): 1190,
        ("Thiruvananthapuram", "Visakhapatnam"): 1520,
        ("Coimbatore", "Mangalore"): 400,
        ("Coimbatore", "Vijayawada"): 910,
        ("Coimbatore", "Visakhapatnam"): 1420,
        ("Mangalore", "Vijayawada"): 890,
        ("Mangalore", "Visakhapatnam"): 1430,
        ("Vijayawada", "Visakhapatnam"): 430
    }

    for (city1, city2), distance in distances.items():
        south_india_graph.insert_edge(city1, city2, distance)

    main_server.insertVertex('user_001', 'pass352', 'Naveen', 34, 'M', 9964837295, 'naveen@gmail.com', 'Bangalore', 'sports')
    main_server.insertVertex('user_002', 'pass582', 'Geeta', 25, 'F', 9832478925, 'geeta@gmail.com', 'Chennai', 'biking')
    main_server.insertVertex('user_003', 'pass641', 'Suresh', 31, 'M', 9792438947, 'suresh@gmail.com', 'Hyderabad', 'public speaking')
    main_server.insertVertex('user_004', 'pass739', 'Pooja', 27, 'F', 9734298734, 'pooja@gmail.com', 'Kochi', 'sports')
    main_server.insertVertex('user_005', 'pass123', 'Amit', 24, 'M', 9973837248, 'amit@gmail.com', 'Mysore', 'biking')
    main_server.insertVertex('user_006', 'pass456', 'Lakshmi', 29, 'F', 9647384932, 'lakshmi@gmail.com', 'Thiruvananthapuram', 'public speaking')
    main_server.insertVertex('user_007', 'pass789', 'Rohan', 26, 'M', 9748932745, 'rohan@gmail.com', 'Coimbatore', 'sports')
    main_server.insertVertex('user_008', 'pass234', 'Kavita', 22, 'F', 9864372847, 'kavita@gmail.com', 'Mangalore', 'biking')
    main_server.insertVertex('user_009', 'pass567', 'Vishal', 28, 'M', 9984728347, 'vishal@gmail.com', 'Vijayawada', 'public speaking')
    main_server.insertVertex('user_010', 'pass890', 'Anju', 32, 'F', 9638472384, 'anju@gmail.com', 'Visakhapatnam', 'sports')
    main_server.insertVertex('user_011', 'pass111', 'Sneha', 30, 'F', 9748237482, 'sneha@gmail.com', 'Bangalore', 'biking')
    main_server.insertVertex('user_012', 'pass222', 'Deepak', 23, 'M', 9874238942, 'deepak@gmail.com', 'Chennai', 'public speaking')
    main_server.insertVertex('user_013', 'pass333', 'Anita', 27, 'F', 9732487394, 'anita@gmail.com', 'Hyderabad', 'sports')
    main_server.insertVertex('user_014', 'pass444', 'Ravi', 29, 'M', 9964732943, 'ravi@gmail.com', 'Kochi', 'biking')
    main_server.insertVertex('user_015', 'pass555', 'Meena', 24, 'F', 9784384923, 'meena@gmail.com', 'Mysore', 'public speaking')
    main_server.insertVertex('user_016', 'pass666', 'Nandini', 35, 'F', 9873427389, 'nandini@gmail.com', 'Thiruvananthapuram', 'sports')
    main_server.insertVertex('user_017', 'pass777', 'Hari', 21, 'M', 9647384723, 'hari@gmail.com', 'Coimbatore', 'biking')
    main_server.insertVertex('user_018', 'pass888', 'Swati', 26, 'F', 9837492837, 'swati@gmail.com', 'Mangalore', 'public speaking')
    main_server.insertVertex('user_019', 'pass999', 'Raj', 34, 'M', 9748923748, 'raj@gmail.com', 'Vijayawada', 'sports')
    main_server.insertVertex('user_020', 'pass000', 'Vidya', 28, 'F', 9732487324, 'vidya@gmail.com', 'Visakhapatnam', 'biking')
    main_server.insertVertex('user_021', 'pass321', 'Kiran', 24, 'M', 9963827384, 'kiran@gmail.com', 'Bangalore', 'public speaking')
    main_server.insertVertex('user_022', 'pass654', 'Priya', 25, 'F', 9847238423, 'priya@gmail.com', 'Chennai', 'sports')
    main_server.insertVertex('user_023', 'pass987', 'Sanjay', 30, 'M', 9763849238, 'sanjay@gmail.com', 'Hyderabad', 'biking')
    main_server.insertVertex('user_024', 'pass210', 'Rekha', 27, 'F', 9873482374, 'rekha@gmail.com', 'Kochi', 'public speaking')
    main_server.insertVertex('user_025', 'pass543', 'Rakesh', 32, 'M', 9734892374, 'rakesh@gmail.com', 'Mysore', 'sports')
    main_server.insertVertex('user_026', 'pass876', 'Anjali', 29, 'F', 9647384723, 'anjali@gmail.com', 'Thiruvananthapuram', 'biking')
    main_server.insertVertex('user_027', 'pass109', 'Vikram', 33, 'M', 9847382947, 'vikram@gmail.com', 'Coimbatore', 'public speaking')
    main_server.insertVertex('user_028', 'pass432', 'Divya', 26, 'F', 9738492374, 'divya@gmail.com', 'Mangalore', 'sports')
    main_server.insertVertex('user_029', 'pass765', 'Harish', 28, 'M', 9873427384, 'harish@gmail.com', 'Vijayawada', 'biking')
    main_server.insertVertex('user_030', 'pass098', 'Manisha', 25, 'F', 9964738942, 'manisha@gmail.com', 'Visakhapatnam', 'public speaking')
    main_server.insertVertex('user_031', 'pass123', 'Rohit', 31, 'M', 9734827348, 'rohit@gmail.com', 'Bangalore', 'sports')
    main_server.insertVertex('user_032', 'pass456', 'Neha', 23, 'F', 9873428742, 'neha@gmail.com', 'Chennai', 'biking')
    main_server.insertVertex('user_033', 'pass789', 'Siddharth', 27, 'M', 9647384728, 'siddharth@gmail.com', 'Hyderabad', 'public speaking')
    main_server.insertVertex('user_034', 'pass234', 'Preeti', 28, 'F', 9847384732, 'preeti@gmail.com', 'Kochi', 'sports')
    main_server.insertVertex('user_035', 'pass567', 'Ritesh', 30, 'M', 9738492374, 'ritesh@gmail.com', 'Mysore', 'biking')
    main_server.insertVertex('user_036', 'pass890', 'Sunita', 24, 'F', 9873428743, 'sunita@gmail.com', 'Thiruvananthapuram', 'public speaking')
    main_server.insertVertex('user_037', 'pass111', 'Ankur', 32, 'M', 9964738942, 'ankur@gmail.com', 'Coimbatore', 'sports')
    main_server.insertVertex('user_038', 'pass222', 'Sonal', 25, 'F', 9847384732, 'sonal@gmail.com', 'Mangalore', 'biking')
    main_server.insertVertex('user_039', 'pass333', 'Nitin', 33, 'M', 9738492374, 'nitin@gmail.com', 'Vijayawada', 'public speaking')
    main_server.insertVertex('user_040', 'pass444', 'Smita', 27, 'F', 9647384723, 'smita@gmail.com', 'Visakhapatnam', 'sports')
    main_server.insertVertex('user_041', 'pass555', 'Ajay', 29, 'M', 9873428742, 'ajay@gmail.com', 'Bangalore', 'biking')
    main_server.insertVertex('user_042', 'pass666', 'Vandana', 28, 'F', 9964738943, 'vandana@gmail.com', 'Chennai', 'public speaking')
    main_server.insertVertex('user_043', 'pass777', 'Gaurav', 34, 'M', 9738492374, 'gaurav@gmail.com', 'Hyderabad', 'sports')
    main_server.insertVertex('user_044', 'pass888', 'Ruchi', 24, 'F', 9873428743, 'ruchi@gmail.com', 'Kochi', 'biking')
    main_server.insertVertex('user_045', 'pass999', 'Pranav', 30, 'M', 9647384723, 'pranav@gmail.com', 'Mysore', 'public speaking')
    main_server.insertVertex('user_046', 'pass000', 'Komal', 32, 'F', 9847384732, 'komal@gmail.com', 'Thiruvananthapuram', 'sports')
    main_server.insertVertex('user_047', 'pass321', 'Rajesh', 27, 'M', 9738492374, 'rajesh@gmail.com', 'Coimbatore', 'biking')
    main_server.insertVertex('user_048', 'pass654', 'Pallavi', 25, 'F', 9873428742, 'pallavi@gmail.com', 'Mangalore', 'public speaking')
    main_server.insertVertex('user_049', 'pass987', 'Karthik', 29, 'M', 9964738942, 'karthik@gmail.com', 'Vijayawada', 'sports')
    main_server.insertVertex('user_050', 'pass210', 'Nisha', 26, 'F', 9647384723, 'nisha@gmail.com', 'Visakhapatnam', 'biking')

    main_server.insert_edge('user_001','user_023')
    main_server.insert_edge('user_023','user_002')
    main_server.insert_edge('user_002','user_017')
    main_server.insert_edge('user_003','user_029')
    main_server.insert_edge('user_004','user_015')
    main_server.insert_edge('user_005','user_020')
    main_server.insert_edge('user_006','user_011')
    main_server.insert_edge('user_007','user_022')
    main_server.insert_edge('user_008','user_034')
    main_server.insert_edge('user_009','user_027')
    main_server.insert_edge('user_010','user_039')
    main_server.insert_edge('user_011','user_033')
    main_server.insert_edge('user_012','user_040')
    main_server.insert_edge('user_013','user_032')
    main_server.insert_edge('user_014','user_046')
    main_server.insert_edge('user_015','user_038')
    main_server.insert_edge('user_016','user_042')
    main_server.insert_edge('user_017','user_048')
    main_server.insert_edge('user_018','user_041')
    main_server.insert_edge('user_019','user_026')
    main_server.insert_edge('user_020','user_031')
    main_server.insert_edge('user_021','user_043')
    main_server.insert_edge('user_022','user_035')
    main_server.insert_edge('user_023','user_044')
    main_server.insert_edge('user_024','user_049')
    main_server.insert_edge('user_025','user_037')
    main_server.insert_edge('user_026','user_050')
    main_server.insert_edge('user_027','user_045')
    main_server.insert_edge('user_028','user_036')
    main_server.insert_edge('user_029','user_047')
    main_server.insert_edge('user_030','user_018')
    main_server.insert_edge('user_031','user_024')
    main_server.insert_edge('user_032','user_012')
    main_server.insert_edge('user_033','user_009')
    main_server.insert_edge('user_034','user_014')
    main_server.insert_edge('user_035','user_019')
    main_server.insert_edge('user_036','user_030')
    main_server.insert_edge('user_037','user_007')
    main_server.insert_edge('user_038','user_016')
    main_server.insert_edge('user_039','user_028')
    main_server.insert_edge('user_040','user_003')
    main_server.insert_edge('user_041','user_002')
    main_server.insert_edge('user_042','user_025')
    main_server.insert_edge('user_043','user_001')
    main_server.insert_edge('user_044','user_021')
    main_server.insert_edge('user_045','user_005')
    main_server.insert_edge('user_046','user_013')
    main_server.insert_edge('user_047','user_004')
    main_server.insert_edge('user_048','user_008')
    main_server.insert_edge('user_049','user_006')
    main_server.insert_edge('user_050','user_010')

    link_accounts_and_cities(south_india_graph,main_server)
    

    return main_server,south_india_graph
