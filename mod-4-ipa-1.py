#!/usr/bin/env python
# coding: utf-8

# In[ ]:


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Notes:
    # Use If elif conditional statements.
    
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            return("friends")
        elif from_member not in social_graph[to_member]["following"]:
            return("follower")
    elif from_member in social_graph[to_member]["following"]:
        return("followed by") 
    
    else:
        return("norelationship")
    
    
    
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    
    measure_board = len(board)
    win = ''
        
    #board 6x6    
    if measure_board == 6:
        for row in range(measure_board):
            if board[row][0]==board[row][1]==board[row][2]==board[row][3]==board[row][4]==board[row][5] and board[row][0] != 0:
                win = board[row][0]
        for col in range(measure_board):
            if board[0][col]==board[1][col]==board[2][col]==board[3][col]==board[4][col]==board[5][col] and board[col][0] != 0:
                win = board[0][col]
        
        if board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4]==board[5][5] and board[0][0] !=0:
            win = board[0][0]
        
        if board[0][5]==board[1][4]==board[2][3]==board[3][2]==board[4][1]==board[5][0] and board[0][3]!=0:
            win = board[0][3]
        if win == '':
            return("NO WINNER")
        else:
            return(win)
        
        
    #board 5x5    
    if measure_board == 5:
        for row in range(measure_board):
            if board[row][0]==board[row][1]==board[row][2]==board[row][3]==board[row][4] and board[row][0] != 0:
                win = board[row][0]
        for col in range(measure_board):
            if board[0][col]==board[1][col]==board[2][col]==board[3][col]==board[4][col] and board[col][0] != 0:
                win = board[0][col]
        if board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4] and board[0][0] !=0:
            win = board[0][0]
        if board[0][4]==board[1][3]==board[2][2]==board[3][1]==board[4][0] and board[0][3]!=0:
            win = board[0][3]
        if win == '':
            return("NO WINNER")
        else:
            return(win)    
        
        
    #board 4x4    
    if measure_board == 4:
        for row in range(measure_board):
            if board[row][0]==board[row][1]==board[row][2]==board[row][3] and board[row][0] != 0:
                win = board[row][0]

        for col in range(measure_board):
            if board[0][col]==board[1][col]==board[2][col]==board[3][col] and board[0][col] != 0:
                win = board[0][col]
        
        if board[0][0]==board[1][1]==board[2][2]==board[3][3] and board[0][0] !=0:
            win = board[0][0]
        
        if board[0][3]==board[1][2]==board[2][1]==board[3][0] and board[0][3]!=0:
            win = board[0][3]
        if win == '':
            return("NO WINNER")
        else:
            return(win)
            
        
        
    #board 3x3
    if measure_board == 3:
        for row in range(measure_board):
            if board[row][0]==board[row][1]==board[row][2] and board[row][0] != 0:
                win = board[row][0]
        
        for col in range(measure_board):
            if board[0][col]==board[1][col]==board[2][col] and board[0][col] != 0:
                win = board[0][col]
        
        if board[0][0]==board[1][1]==board[2][2] and board[0][0] !=0:
            win = board[0][0]
        
        if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=0:
            win = board[0][2]
        if win == '':
            return("NO WINNER")
        else:
            return(win)
        
        
        
'''
Sample data for ETA below:
(from_stop, to_stop)
'''

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

#legs = {
#    ('a1', 'a2'): {
#        'travel_time_mins': 10
#    },
#    ('a2', 'b1'): {
#        'travel_time_mins': 10230
#    },
#    ('b1', 'a1'): {
#        'travel_time_mins': 1
#    }
#}

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    

    if second_stop == first_stop:
        return("You are there")
    else:
        keys = list(route_map.keys())
        i = 0
        newlist = []

        while i < len(keys):
            newlist.append(keys[i][0])
            i+=1

        direction = (first_stop,second_stop)

        if direction in route_map:
            return(route_map[direction]["travel_time_mins"])
        else:
            midpoint = newlist.index(first_stop)+1

            if midpoint > 2:
                midpoint -= len(keys)
                
                
            #Routes
            route1 = (first_stop,newlist[midpoint])

            route2 = (newlist[midpoint],second_stop)

            return((route_map[route1]["travel_time_mins"]) + route_map[route2]["travel_time_mins"])
        
        
        
        

