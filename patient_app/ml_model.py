class MLModel:
    
    def predict(self, input_data):
        score = 0
    
        heartbeat, bmi, gender, sleeptime, age = input_data
        
        if 60 <= heartbeat < 100:
            score += 1
        elif (45 <= heartbeat < 60) or (100 <= heartbeat < 140):
            score += 0.5
        else:
            score += 0
            
        if 18 <= bmi < 25:
            score += 1
        elif (14 <= bmi < 18) or (25 <= bmi < 30):
            score += 0.5
        else:
            score += 0
        
        if gender == 1:
            score += 1
        else:
            score += 0.5
            
        if 5 <= sleeptime < 10:
            score += 1
        elif (3 <= sleeptime < 5) or (10 <= sleeptime < 13):
            score += 0.5
        else:
            score += 0
            
        if 18 <= age < 40:
            score += 1
        elif (4 <= age < 18) or (40 <= age < 60):
            score += 0.5
        else:
            score += 0
            
        return score