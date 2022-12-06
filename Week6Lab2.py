MoviesName = "movies.txt"

def writeMovies(movieList):
    with open (MoviesName, "w+") as file:
        for movie in movieList:
            file.write(f"{movie}\n")

def readMovies():
    movies = []
    with open(MoviesName) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
    return movies

def disMenu():
    print("The Family Friendly Movie List Program\n")
    print("COMMAND MENU")
    print("LS - List all movies")
    print("ADD  - Add a movie")
    print("DEL  - Delete a movie")
    print("EXIT - Exit program\n")

def lsMovie(movieList):
    for i, movie in enumerate(movieList, start=1):
        print(f"{i}. {movie}")
    print()

def addMovie(movieList):
    movie = input("Name: ")
    movieList.append(movie)
    writeMovies(movieList)
    print(f"{movie} was added.\n")

def delMovie(movieList):
    number = int(input("Number: "))
    if number < 1 or number > len(movieList):
        print("Invalid movie number.\n")
    else:
        movie = movieList.pop(number-1)
        writeMovies(movieList)
        print(f"{movie} was deleted.\n")

def main():
    disMenu()
    List = readMovies()
    while True:        
        command = input("Command: ")
        if command.lower() == "ls" or command.lower() == "list":
            lsMovie(List)   
        elif command.lower() == "add":
            addMovie(List)
        elif command.lower() == "del" or command.lower() == "delete":
            delMovie(List)  
        elif command.lower() == "exit" or command.lower() == "quit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Goodbye!")
main()
