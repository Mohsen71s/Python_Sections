# #singel responsability principle (srp)
# from pathlib import Path
# from zipfile import ZipFile
# class FileManager:
#     def __init__(self, filename):
#         self.path = Path(filename)
#     def read(self, encoding="utf-8"):
#         return self.path.read_text(encoding)
#     def write(self, data, encoding="utf-8"):
#         self.path.write_text(data, encoding)
# class ZipFileManager:
#     def __init__(self, filename):
#         self.path = Path(filename)
#     def compress(self):
#         with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
#             archive.write(self.path)
#     def decompress(self):
#         with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
#             archive.extractall()

print("="*40)

# # open-closed principle (ocp)
# from abc import ABC,abstractmethod
# from math import pi
# class Shape(ABC):
#     def __init__(self,shape_type):
#         self.shape_type=shape_type
#     @abstractmethod
#     def calculate_area(self):
#         pass
# # circle class
# class Circle(Shape):
#     def __init__(self, redius):
#         super().__init__("Circle")
#         self.redius=redius
#     def calculate_area(self):
#         return pi*self.redius**2
# # circle Rectangel
# class Rectangel(Shape):
#     def __init__(self, hight,widht):
#         super().__init__("Rectangel")
#         self.hight=hight
#         self.widht=widht
#     def calculate_area(self):
#         return self.widht*self.hight
# # circle square
# class Square(Shape):
#     def __init__(self, side):
#         super().__init__("Square")
#         self.side=side
#     def calculate_area(self):
#         return self.side**2
    
print("="*40)

# #Liskov Substitution Principle (LSP)    
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
# def calculate_area(self):
#     return self.width * self.height

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side   
#     def calculate_area(self):
#         return self.side ** 2

print("="*40)
#Interface Segregation Principle (ISP)
# from abc import ABC,abstractmethod
# class Printer(ABC):
#     @abstractmethod
#     def Printer(self,document):
#         pass
# class Fax(ABC):
#     @abstractmethod
#     def Fax(self,document):
#         pass
# class Scanner(ABC):
#     @abstractmethod
#     def Printer(self,document):
#         pass
# class OldPrinter(Printer):
#     def print(self, document):
#         print(f"Printing {document} in black and white...")
# class NewPrinter(Printer, Fax, Scanner):
#     def print(self, document):
#         print(f"Printing {document} in color...")
#     def fax(self, document):
#         print(f"Faxing {document}...")
#     def scan(self, document):
#         print(f"Scanning {document}...")

print("="*40)

# # Dependency Inversion Principle (DIP)
# from abc import ABC, abstractmethod
# class FrontEnd:
#     def __init__(self, data_source):
#         self.data_source = data_source
#     def display_data(self):
#         data = self.data_source.get_data()
#         print("Display data:", data)

# class DataSource(ABC):
#     @abstractmethod
#     def get_data(self):
#         pass
# class Database(DataSource):
#     def get_data(self):
#         return "Data from the database"
# class API(DataSource):
#     def get_data(self):
#         return "Data from the API"
# db_front_end = FrontEnd(Database())
# db_front_end.display_data()
# api_front_end = FrontEnd(API())
# api_front_end.display_data()
