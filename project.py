import sys
import csv

def main():
     len_arg()

     inf= []
     
     try:
          with open(sys.argv[1], "r") as csvfile:
               reader = csv.DictReader(csvfile) 
               for row in reader:
                    inf.append(row)
     except FileNotFoundError:
          sys.exit("FILE NOT FOUND")
  
     
     output = []
     for row in inf:
          the_genre = genre(row["theme"])
          the_shelf = shelf(row["page"])
          output.append({"genre": the_genre, "book": row["book"], "author": row["author"], "shelf": the_shelf})
    
     output = sorted(output, key=lambda x: x["shelf"]) 

     with open(sys.argv[2], "w") as file:
          writer = csv.DictWriter(file, fieldnames=["genre", "book", "author", "shelf"])
          writer.writerow({"genre": "genre", "book": "book", "author": "author", "shelf": "shelf"})
          for row in output: 
               writer.writerow({"genre": row["genre"], "book": row["book"], "author": row["author"], "shelf": row["shelf"]})



def len_arg():
      if len(sys.argv) < 3:
           sys.exit("Too few command-line arguments")
                
      elif len(sys.argv) > 3:
           sys.exit("Too many command-line arguments")
    
      elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
           sys.exit("NOT A CSV FILE")
                

def genre(info):
     if info in ["well-being", "trauma", "emotions"]:
          return "psychology"
     elif info in ["society", "life", "groups"]:
          return "sociology"
     elif info in ["ontology", "epistemology", "thinking"]:
          return "philosophy"
     elif info in ["method", "experiment", "observation"]:
          return "science"
     elif info in ["romance", "fantasy", "love"]:
          return "fiction"
     else:
          return "GENRE NOT FOUND"
     

def shelf(num):
     try:
          if int(num)>399:
               return "5.shelf"
          elif int(num)>299:
               return "4.shelf"
          elif int(num)>199:
               return "3.shelf"
          elif int(num)>99:
               return "2.shelf"
          elif int(num)>0:
               return "1.shelf"
          else:
               return "6.shelf"
     except ValueError:
          return "NOT AN INTEGER"


if __name__ == "__main__":
     main()