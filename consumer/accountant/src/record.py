class Record:

    @staticmethod
    def count(db, event, compareEvent, field ):
        count = 0

        if (db.exists(field)):
            count = int(db.get(field))
        
        if event == compareEvent:
            count = count + 1
           
        return count   
       