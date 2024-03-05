from Database.database import session
from Database.models import UserResponseModels

class UserResponse:
    def __init__(self,db_session=None) -> None:
        self.__session = session if not db_session else db_session


    def add_question_response(self,request,user_id):
        return_rsponse = False
        try:
            for data in request:
                user_response_obj = UserResponseModels(question_id=data.question_id,option_id=data.option_id,user_id=user_id)
                self.__session.add(user_response_obj)
                self.__session.flush()
            return_rsponse = True
        except Exception as e:
            print("Exception comes in the user response",str(e)) 
        finally:
            return return_rsponse   

