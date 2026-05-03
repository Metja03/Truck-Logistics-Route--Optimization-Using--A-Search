import time

def simulate_path(path, visited_order, total_cost):
    print("\n🚚 Truck traveling...\n")
    for node in path:
        print(f"Car is now at: {node}")
        time.sleep(1)
    print("\n✅ Destination reached!\n")
    
    print("📋 Visited Order:", visited_order)
    print("🛣️ Optimal Path:", path)
    print("💰 Total Cost:", total_cost)