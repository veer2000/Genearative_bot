from langchain_core.messages import HumanMessage, AIMessage


class MemoryManager():

    def __init__(self):
        self.history = []


    def add_message(self, role:str, content:str):
        try:
            if role == 'user':
                self.history.append(HumanMessage(content = content))
            else:
                self.history.append(AIMessage(content = content))
        except Exception as e:
            print(e)

    def get_history(self):
        return self.history

memeorymanager = MemoryManager()