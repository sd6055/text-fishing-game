"""
Text Fishing Simulator - With Rich Colors
Fixed command display and background contrast issues
"""
import random
import time
import sys
from rich.console import Console
from rich.theme import Theme
from rich.markup import escape

# Create custom theme for better visibility on dark backgrounds
custom_theme = Theme({
    "info": "cyan",
    "success": "bright_green",
    "warning": "bright_yellow",
    "error": "bright_red",
    "command": "bold white",
    "legendary": "bold bright_yellow"
})

# Initialize Rich console with theme
console = Console(theme=custom_theme, force_terminal=True)

class FishingGame:
    def __init__(self):
        self.fish_types = [
            {"name": "Bluegill", "points": 1, "rarity": "Common", "weight": (0.5, 2.0)},
            {"name": "Largemouth Bass", "points": 3, "rarity": "Uncommon", "weight": (1.0, 8.0)},
            {"name": "Channel Catfish", "points": 5, "rarity": "Rare", "weight": (3.0, 15.0)},
            {"name": "Golden Trout", "points": 10, "rarity": "LEGENDARY", "weight": (2.0, 5.0)}
        ]
        
        # Define color mappings using Rich markup
        self.rarity_colors = {
            "Common": "white",
            "Uncommon": "green",
            "Rare": "blue",
            "LEGENDARY": "bold bright_yellow"
        }
        
        self.inventory = []
        self.score = 0
        self.casts = 0
        
    def colorize(self, text, color):
        """Apply Rich markup color to text"""
        return f"[{color}]{text}[/{color}]"
    
    def cast_line(self):
        """Simulate one fishing attempt"""
        self.casts += 1
        console.print(f"\n[info]🎣 Cast #{self.casts}: Throwing line...[/info]")
        time.sleep(1)
        
        # 65% chance to catch something
        if random.random() > 0.35:
            fish = random.choice(self.fish_types)
            weight = round(random.uniform(*fish["weight"]), 2)
            
            # Get color for this rarity
            color = self.rarity_colors.get(fish["rarity"], "white")
            
            console.print(f"[success]⭐ HOOKED![/success] [{color}]{fish['name']}[/{color}] ([{color}]{fish['rarity']}[/{color}])")
            console.print(f"   [info]Weight:[/info] {weight} lbs | [info]Points:[/info] [success]+{fish['points']}[/success]")
            
            self.inventory.append({
                "name": fish["name"],
                "weight": weight,
                "points": fish["points"],
                "rarity": fish["rarity"]
            })
            self.score += fish["points"]
            return True
        else:
            console.print("[error]💨 Fish got away...[/error]")
            return False
    
    def show_inventory(self):
        """Display caught fish and stats"""
        if not self.inventory:
            console.print("[info]\nYour bucket is empty.[/info]")
            return
        
        console.print(f"\n[info]{'='*50}[/info]")
        console.print(f"[bold]YOUR CATCHES ({len(self.inventory)} fish)[/bold]")
        console.print(f"[info]{'='*50}[/info]")
        
        for i, fish in enumerate(self.inventory, 1):
            color = self.rarity_colors.get(fish["rarity"], "white")
            console.print(f"{i}. [{color}]{fish['name']:20}[/{color}] {fish['weight']:>5} lbs")
        
        console.print(f"\n[bold]📊 STATS[/bold]")
        console.print(f"Total Score: [success]{self.score}[/success]")
        console.print(f"Total Casts: {self.casts}")
        success_rate = (len(self.inventory)/self.casts*100) if self.casts > 0 else 0
        
        # Color success rate based on performance
        if success_rate >= 70:
            rate_color = "success"
        elif success_rate >= 40:
            rate_color = "info"
        else:
            rate_color = "error"
            
        console.print(f"Success Rate: [{rate_color}]{success_rate:.1f}%[/{rate_color}]")
    
    def run(self):
        """Main game loop with fixed command display"""
        console.print(f"[info]{'='*50}[/info]")
        console.print("[bold]🎣 WELCOME TO TEXT FISHING SIMULATOR! 🎣[/bold]")
        console.print(f"[info]{'='*50}[/info]")
        console.print("\nCommands:")
        # Use color highlighting instead of brackets to avoid Rich tag parsing
        console.print(f"  {self.colorize('c', 'bright_green')}ast      - Cast your fishing line")
        console.print(f"  {self.colorize('i', 'bright_cyan')}nventory - View your catches")
        console.print(f"  {self.colorize('q', 'bright_red')}uit      - Exit game")
        
        while True:
            console.print(f"\n[info]{'-'*30}[/info]")
            cmd = input("Enter command: ").lower().strip()
            
            if cmd in ["c", "cast"]:
                self.cast_line()
            elif cmd in ["i", "inventory"]:
                self.show_inventory()
            elif cmd in ["q", "quit"]:
                console.print(f"\n[info]{'='*50}[/info]")
                console.print("[success]Thanks for playing![/success]")
                console.print(f"Final Score: [bold]{self.score}[/bold]")
                console.print(f"Fish Caught: [info]{len(self.inventory)}[/info]")
                
                # Bonus message for legendary catch
                if any(fish["rarity"] == "LEGENDARY" for fish in self.inventory):
                    console.print("[legendary]🌟 You caught a LEGENDARY fish! Amazing! 🌟[/legendary]")
                
                console.print(f"[info]{'='*50}[/info]")
                break
            else:
                console.print("[error]Invalid command. Use: c, i, or q[/error]")

def main():
    game = FishingGame()
    game.run()

if __name__ == "__main__":
    main()