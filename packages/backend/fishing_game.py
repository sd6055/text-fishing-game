"""
Text Fishing Simulator
A console-based fishing game for learning Python and Git.
"""
import random
import time
import sys

class FishingGame:
    def __init__(self):
        self.fish_types = [
            {"name": "Bluegill", "points": 1, "rarity": "Common", "weight": (0.5, 2.0)},
            {"name": "Largemouth Bass", "points": 3, "rarity": "Uncommon", "weight": (1.0, 8.0)},
            {"name": "Channel Catfish", "points": 5, "rarity": "Rare", "weight": (3.0, 15.0)},
            {"name": "Golden Trout", "points": 10, "rarity": "LEGENDARY", "weight": (2.0, 5.0)}
        ]
        self.inventory = []
        self.score = 0
        self.casts = 0
        
    def cast_line(self):
        """Simulate one fishing attempt"""
        self.casts += 1
        print(f"\n🎣 Cast #{self.casts}: Throwing line...")
        time.sleep(1)
        
        # 65% chance to catch something
        if random.random() > 0.35:
            fish = random.choice(self.fish_types)
            weight = round(random.uniform(*fish["weight"]), 2)
            
            print(f"⭐ HOOKED! {fish['name']} ({fish['rarity']})")
            print(f"   Weight: {weight} lbs | Points: +{fish['points']}")
            
            self.inventory.append({
                "name": fish["name"],
                "weight": weight,
                "points": fish["points"]
            })
            self.score += fish["points"]
            return True
        else:
            print("💨 Fish got away...")
            return False
    
    def show_inventory(self):
        """Display caught fish and stats"""
        if not self.inventory:
            print("\nYour bucket is empty.")
            return
        
        print(f"\n{'='*40}")
        print(f"YOUR CATCHES ({len(self.inventory)} fish)")
        print(f"{'='*40}")
        
        for i, fish in enumerate(self.inventory, 1):
            print(f"{i}. {fish['name']:20} {fish['weight']:>5} lbs")
        
        print(f"\n📊 STATS")
        print(f"Total Score: {self.score}")
        print(f"Total Casts: {self.casts}")
        success_rate = (len(self.inventory)/self.casts*100) if self.casts > 0 else 0
        print(f"Success Rate: {success_rate:.1f}%")
    
    def run(self):
        """Main game loop"""
        print("="*50)
        print("🎣 WELCOME TO TEXT FISHING SIMULATOR!")
        print("="*50)
        print("\nCommands:")
        print("  [c]ast   - Cast your fishing line")
        print("  [i]nventory - View your catches")
        print("  [q]uit   - Exit game")
        
        while True:
            print("\n" + "-"*30)
            cmd = input("Enter command: ").lower().strip()
            
            if cmd in ["c", "cast"]:
                self.cast_line()
            elif cmd in ["i", "inventory"]:
                self.show_inventory()
            elif cmd in ["q", "quit"]:
                print(f"\n{'='*50}")
                print("Thanks for playing!")
                print(f"Final Score: {self.score}")
                print(f"Fish Caught: {len(self.inventory)}")
                print("="*50)
                break
            else:
                print("Invalid command. Use: c, i, or q")

def main():
    game = FishingGame()
    game.run()

if __name__ == "__main__":
    main()