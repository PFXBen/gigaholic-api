import jsonpickle

class Tour:
    def __init__(self,tour_id:int, tour_name:str):
        self.tour_id = tour_id
        self.TourName = tour_name

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)
