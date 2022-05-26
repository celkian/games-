class CustomPlayer: 
    def __init__(self): 
        self.total_move_count = 0
    
    def choose_move(self): 

        if self.total_move_count < 6: 
            self.total_move_count += 1
            return "d"
        
        if self.total_move_count == 6:
            self.total_move_count += 1 
            return "s"
        
        if self.total_move_count < 11: 
            self.total_move_count += 1 
            return "s"
        
        if self.total_move_count == 11: 
            self.total_move_count += 1 
            return "a"
        
        if self.total_move_count < 20: 
            self.total_move_count += 1 
            return "a"
        
        if self.total_move_count == 20: 
            self.total_move_count += 1 
            return "w"
        
        if self.total_move_count < 29: 
            self.total_move_count += 1 
            return "w"
        
        if self.total_move_count == 29: 
            self.total_move_count += 1 
            return "d"
        
        if self.total_move_count < 38: 
            self.total_move_count += 1 
            return "s"
        
        if self.total_move_count == 38: 
            self.total_move_count += 1 
            return "d"
        
        if self.total_move_count < 47: 
            self.total_move_count += 1 
            return "w"
        
        if self.total_move_count == 47: 
            self.total_move_count += 1
            return "d"
        if self.total_move_count < 56: 
            self.total_move_count += 1 
            return "s"
        
        if self.total_move_count == 56: 
            self.total_move_count += 1 
            return "d"
        
        if self.total_move_count < 65: 
            self.total_move_count += 1 
            return "w"
        
        if self.total_move_count == 65: 
            self.total_move_count += 1 
            return "d"
        
        if self.total_move_count < 74: 
            self.total_move_count += 1 
            return "s"
        
        if self.total_move_count == 74: 
            self.total_move_count += 1 
            return "d"
        
        if self.total_move_count < 83: 
            self.total_move_count += 1 
            return "w"
        
        if self.total_move_count == 83: 
            self.total_move_count += 1 
            return "d"
        
        if self.total_move_count < 92: 
            self.total_move_count += 1
            return "s"
        
        if self.total_move_count == 92: 
            self.total_move_count +=1 
            return "d"
        
        if self.total_move_count < 101: 
            self.total_move_count += 1
            return "w"
        
        if self.total_move_count == 101: 
            self.total_move_count += 1
            return "d"
        if self.total_move_count < 111: 
            self.total_move_count +=1
            return "s"
        
        if self.total_move_count == 111: 
            self.total_move_count = 12
            return "a"



        
        
       