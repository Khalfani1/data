import random
import csv
import os

'''
    without pandas 
    (*)    https://docs.python.org/3/library/csv.html#csv.DictReader
    (**)   https://stackoverflow.com/questions/8689964/why-do-some-functions-have-underscores-before-and-after-the-function-name
    (***)  https://blog.finxter.com/how-to-filter-in-python-using-lambda-functions/
    (****) https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    also:    https://www.google.com/search?q=programming+fizzbuzz&source=lnms&tbm=vid
'''


class Questions:
    def __init__(self,location = os.getcwd(), filename = 'questions.csv'):
        self.questions = self._read_question(os.path.join(location,filename))

    def _read_question(self,file):
        'returns list of dict with questions see (*)'
        with open(file, 'r') as f:
            # read rows as list of dictionaries 
            all_rows = list(csv.DictReader(f))
            # make sure that qid, category and level are of correct data type
            all_rows = list(map(self._change_type, all_rows))
            # alternative see (****)
            # all_rows = [self._change_type(row) for row in all_rows]
            return all_rows

    def _change_type(self,row):
            ' make sure  qid, category, level are integers'
            row['qid'] = int(row['qid'])     
            row['category'] = int(row['category'])
            row['level'] = int(row['level'])
            return row

    def _filter_by_level(self,level):
        'filter questions based on specific level, see (***)'
        return list(filter(lambda x: x.get('level') == level, self.questions))

    def _filter_by_qid(self,qid):
        'filter questions based on specific qid, see (***)'
        return list(filter(lambda x: x.get('qid') == qid, self.questions))


    def get(self, category = 1, level = None, qid = None):
        'returns a random question with random task'
        if qid != None:
            qid_question = self._filter_by_qid(qid)
            if len(qid_question):
                return qid_question[0]
            else:
                return {}
        elif level != None:
            questions = self._filter_by_level(level)
            if len(questions) > 0:
                question = random.choice(questions)
                return question
            else:
                return {}
        else:
            return 'this is an incomplete program, you can use it with pa part1'
                      



