from Database.database import session
from Database.models import UserModels
from Module.user_response import UserResponse


class Users:
    def __init__(self,db_session=None) -> None:
        self.__session = session if not db_session else db_session

    
    def create_user(self,request):
        return_response = {
            "status":False
        }
        try:
            request_data = request.dict()
            user_object= UserModels(**request_data['user_details'])
            self.__session.add(user_object)
            self.__session.flush()
            if user_object.id:
                result = UserResponse(self.__session).add_question_response(request=request.response,user_id=user_object.id)
                if result is True:
                    self.__session.commit()
                    return_response['status']=True
        except Exception as e:
            print("exception on User module",str(e))
        finally:
            return return_response
                        

    

    