from master_graph import *
from predefined_prompt import *
from tabulate import tabulate

# Running the predifined function calls 
main_server,location_server = populate()

# Function to validate username and password 
# O(1)
def validate(username,passwrod):
    node = main_server.get_vertex(username)
    if username == 'admin' and password == '1234':
        return 'admin'
    if node is None:
        return node
    if passwrod == node.password:
        return node
    return None

# Function to find friends of friends
# O(V1*V2)
def friends_friend(u):
    a=main_server.transitive_follow(u)
    l=recommend(main_server,u)
    level1=[]
    for i in a:
        for j in i:
            if j not in l and j is not u:
                level1.append(j)
    return level1


# Function to recommend friends based on mutuals
# O(V^2)
def recommend(g,u):# Here u is vertex
        x=[]
        for v in g.outgoing[u]:
            r=[]
            cycle=g.detect_cycle_between(u.userid,v.userid)
            if cycle:
                remove= {u,v}
                # Using list comprehension
                r = [e for e in cycle if e not in remove]
                x.append(r)
        to_be_recommended=set()
        for j in  x:
            for i in  j:
                if i is not u and i not in g.outgoing[u]:
                    to_be_recommended.add(i)
        return list(to_be_recommended)

# Function to make user u follow user v
# O(1)
def follow(u,v):
    main_server.insert_edge(u.userid,v)
    print(f"{u} is following {v}".center(40, "="))

# Function to display followers of a user
# O(V)
def followers(u):
    keys = list(main_server.outgoing[u].keys())
    table = []
    print(f"\nFriends of {u} are".center(40, "="))
    for i in keys:
        table.append([i.userid, i.name, i.age])
    print()

    headers = ["User ID", "Name", "Age"]
    print(tabulate(table, headers, tablefmt="grid"))

while True:
    print("\n" + "="*40)
    print(" Welcome to the Application ".center(40, "="))
    print("="*40)
    print("\nPlease choose an option:")
    print("1. Login")
    print("2. Exit App")
    print("="*40)

    try:
        choice1 = int(input("Enter your choice (1 or 2): "))
        if choice1 == 1:
            print("\n" + "="*40)
            print(" Login ".center(40, "="))
            print()
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            check = validate(username, password)
            if check is None:
                print("\n" + "="*40)
                print(" Invalid User. Try again or wrong password. ".center(40, "="))
                print("="*40)
                continue
            elif check == 'admin':
                print("1. BroadCast Messages")
                print("2. To view all the nodes")
                print("3. Cluster the graph based on interest")
                choice_admin = int(input("Enter the choice : "))
                if choice_admin == 1:
                    message1 = input("Enter the message to be broadcasted : ")
                    all_vertices = main_server.outgoing.keys()
                    for i in all_vertices:
                        main_server.addMessage(i,message1)
                    continue
                elif choice_admin == 2:
                    main_server.visualize()
                elif choice_admin == 3:
                    main_server.cluster()
                continue
            elif check:
                print("\n" + "="*40)
                print(" Successful Login! ".center(40, "="))
                print("="*40)

                while True:
                    print("\n" + "="*40)
                    print(" User Menu ".center(40, "="))
                    print("="*40)
                    print("1. Show recommendations based on mutuals")
                    print("2. Show recommended friends based on location")
                    print("3. Find Users")
                    print("4. Show Friends List")
                    print("5. View Notifications")
                    print("6. Friends's Friends")
                    print("7. Log out")
                    print("="*40)

                    choice3 = int(input("Enter your choice (1 to 4): "))
                    if choice3 == 1:
                        print("\n" + "="*40)
                        print(" Recommendations Based on Mutuals ".center(40, "="))
                        print("="*40)
                        r=recommend(main_server,check)
                        table = []
                        for i in r:
                            table.append([i.userid, i.name, i.age])
                        print()
                        headers = ["User ID", "Name", "Age"]
                        print(tabulate(table, headers, tablefmt="grid"))
                        
                        u=input("Enter userid from table you want to follow : ")
                        print()
                        u1=main_server.get_vertex(u)
                        if u1 in r:
                            follow(check,u)
                        continue
                    elif choice3 == 2:
                        range = int(input("Enter the range to see friends (in km): "))
                        starting_city = check.location
                        max_distance = range  # Maximum distance to consider

                        starting_vertex = location_server.get_vertex(starting_city)
                        if starting_vertex:
                            surrounding_cities = bfs(south_india_graph, starting_vertex, max_distance)
                            print("\n" + "="*40)
                            print(f" Cities within {max_distance} km from {starting_city} ".center(40, "="))
                            print("="*40)
                            print(surrounding_cities)
                            find_city = location_server.get_vertex(starting_city)
                            user_accounts = find_city.user_accounts
                            user_accounts.print_list()

                            u=input("Enter userid from table you want to follow : ")
                            print()
                            follow(check,u)
                            continue
                           
                    elif choice3 == 3:
                        find_users = input("Enter the user ID: ").strip()
                        user = main_server.get_vertex(find_users)
                        if user is None:
                            print("\n" + "="*40)
                            print(" No user found ".center(40, "="))
                            print("="*40)
                        else:
                            print("\n" + "="*40)
                            print(f" User Found: {user} ".center(40, "="))
                            choice4=int(input("Enter 1 if you want to follow : "))
                            if choice4==1:
                                follow(check,user.userid)
                            print("="*40)
                            continue

                    elif choice3 == 4:
                        followers(check)
                    elif choice3 == 5:
                        print("\nNotification : ",end=" ")
                        print(check.message)
                    elif choice3 == 6:
                        r = friends_friend(check)
                        table = []
                        for i in r:
                            table.append([i.userid, i.name, i.age])
                        print()
                        headers = ["User ID", "Name", "Age"]
                        print(tabulate(table, headers, tablefmt="grid"))
                    elif choice3 == 7:
                        print("\n" + "="*40)
                        print(" Logging out... ".center(40, "="))
                        print("="*40)
                        break
                    else:
                        print("\n" + "="*40)
                        print(" Invalid choice. Please enter a number between 1 and 4. ".center(40, "="))
                        print("="*40)
                        continue

        elif choice1 == 2:
            print("\n" + "="*40)
            print(" Exiting Application. Goodbye! ".center(40, "="))
            print("="*40)
            break
        else:
            print("\n" + "="*40)
            print(" Invalid choice. Please enter 1 or 2. ".center(40, "="))
            print("="*40)
    except ValueError:
        print("\n" + "="*40)
        print(" Invalid input. Please enter a number (1 or 2). ".center(40, "="))
        print("="*40)
