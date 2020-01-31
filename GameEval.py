from bs4 import BeautifulSoup
import requests

URL = "https://yuzu-emu.org/game/"
filename = "Watchlist.txt"

Def = {}

inputs = [
        "1","c", # new Game AND new Watchlist
        "2","a", # Add Game to Watchlsit
        "3","s", # Print the Watchlist
        "4","l", # Load Watchlist ------- DEFAULT
        "5","d", # Show Definitions
        "6","h", # print Commands
        "7","q"  # Close
]
options = [
    "Create new Watchlist(c)",
    "Add new Game to Watchlist(a)",
    "Show Watchlist(s)",
    "Load Watchlist(L)?",
    "Show Compatibility Definition(d)",
    "Help(h)",
    "Quit(q)"
]

def printinit():
    for i in range(len(options)):
        print(str(i+1)+". "+options[i])


def printAllGames():
    try:
        with open(filename, "r+") as f:
            for l in f:
                print(l[:-1])
    except:
        print("No Elements in Watchlist yet.")

def printCompDef():
    for key in Def:
        print(key +" = " + Def[key])

def getGame():
    inp = input().lower()
    if inp == "":
        inp = "l"
    inputi = inputs.index(inp)

    
    if inputi < 2:                  # new Game AND new Watchlist
        return newGame()
    elif inputi < 4:                # Add Game to Watchlsit
        return newGame(append=True)
    elif inputi < 6:                # Print the Watchlist
        printAllGames()
        return getGame()
    elif inputi < 8:                # Load Watchlist ------- DEFAULT
        return loadGame()
    elif inputi < 10:               # Print Compatibility Definition
        printCompDef()
        return getGame()   
    elif inputi < 12:               # print Commands
        printinit()
        return getGame()
    elif inputi < 14:               # Close
        exit()


def newGame(append=False):
    modifier = "w+"
    if append:
        modifier = "a+"
    inp = input("What Games are u Looking for? q to Cancel input\n").lower()
    if inp == "q" or inp == "":
        printinit()
        return getGame()
    newGames = [inp]
    while(True):
        inp = input("")
        if inp == "q" or inp == "":
            break
        newGames.append(inp)
    with open(filename, modifier) as f:
        for game in newGames:
            f.write(game+"\n")

    return loadGame()

def loadGame():
    result = []
    try:
        with open(filename, "r+") as f:
            for l in f:
                if len(l) > 1:
                    result.append(l[:-1])
    except:
        pass
    if len(result) == 0:
            print("nothin to Load")
            return newGame()
    else:
        print("Loaded: "+str(len(result))+" Games")
        return result


def printCount(elem):
    print(str(len(elem)))

def prittyPrint(GameList, GameData):
    for i in range(len(GameList)):
        gameTitle = GameList[i]+":"
        print(gameTitle)
        for t in range(len(GameData[i])):
            e = GameData[i][t]
            print("\t"+ str(t+1) +". "+ e[0] +"\tstatus: "+ e[1] +"\tlast Checked: "+ e[2])



if __name__ == "__main__":
    printinit()
    soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
    
    allTables = soup.find_all("table")
    CompTable = allTables[0].tbody
    CompRows = CompTable.find_all('tr')

    CompData=[]
    for CompRow in CompRows:
        cols = CompRow.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        CompData.append(cols)

    for CompRow in CompData:
        Def[CompRow[0]] = CompRow[1]

    GameNames = getGame()

    GameComp = allTables[1].tbody
    GameRows = GameComp.find_all('tr')

    data=[]
    for GameRow in GameRows:
        cols = GameRow.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
    
    Matches = []
    for i in range(len(GameNames)):
        Matches.append([])
    for GameRow in data:
        for i in range(len(GameNames)):
            game = GameNames[i]
            if game in GameRow[0].lower():
                Matches[i].append(GameRow)
    
    #print(Matches)
    

    prittyPrint(GameNames, Matches)

    input("Press any key to quit. . .")
