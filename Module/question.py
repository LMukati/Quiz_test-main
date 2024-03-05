from Database.database import session
from Database.models import QuestionModels
class Questions:
    def __init__(self,db_session=None) -> None:
        self.__session = session if not db_session else db_session

    def fetch_all_questions(self):
        return_response = {
            'status':False,
            'total_rows':0,
            'data':[]
            }
        try:
    
            result = self.__session.query(QuestionModels).filter().order_by(QuestionModels.id)
            data_to_return = []

            for data in result:
                question_data = {
                    'id':data.id,
                    'questions':data.question,
                    'options':[]
                }
                for option in data.options:
                    question_data['options'].append({
                        'options_id':option.id,
                        'foptions_text':option.option_text
                    })
                data_to_return.append(question_data)    


            if result:
                return_response['total_rows']=result.count()
                return_response['data']=data_to_return
            return_response['status']=True
        except Exception as e:
            print('Error', str(e))

        finally:
            return return_response   
