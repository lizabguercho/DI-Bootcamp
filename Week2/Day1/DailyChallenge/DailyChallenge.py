class Farm:
    def __init__(self,farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self,animal_type,count = 1):
        if animal_type in self.animals:
           self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count 

    def get_info(self):
        # Return a string with name of the farm, animals + their count and phrase ( E-I-E-I-O)
        lines = []
        lines.append(f"{self.name}'s farm")
        lines.append("")
        for animal,count in self.animals.items():
            lines.append(f"{animal} : {count}")
        lines.append("")
        lines.append("E-I-E-I-0!")
        song = "\n".join(lines)
        return song
    
    def get_animal_types(self):
        animal_type = []
        for animal in self.animals.keys():
            animal_type.append(animal)
        sorted_animals = sorted(animal_type)
        return sorted_animals
    
    def get_short_info(self,count):
        animal_types_list = self.get_animal_types()
        formatted = []
        for animal in animal_types_list:
            if count > 1:
                formatted.append(animal + "s")
            else:
                formatted.append(animal)
        if len(formatted) > 1:
            animal_str = ", ".join(formatted[:-1]) + " and " + formatted[-1]
        else:
            animal_str = formatted[0]
        return f"{self.name}'s farm has {animal_str}"
            
      
        

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info(5))