class UserEvent:

    @staticmethod
    def create( data, event='create'):
        metadata = {'event' : event, 'metadata' : data}
        return metadata
    
    @staticmethod
    def get( data ):
        return data['metadata']

    @staticmethod
    def get_event( data ):
        return data['event']   

    @staticmethod
    def get_id( data ):
        return data['metadata']['id']   
