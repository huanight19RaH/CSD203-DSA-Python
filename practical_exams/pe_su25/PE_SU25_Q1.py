class Model:
    def __init__(self, name, month, year):
        self.name = name
        self.month = month
        self.year = year

class Node:
    def __init__(self, model):
        self.model = model
        self.next = None
        
class LLMLinkedListManager:
    def __init__(self):
        self.head = None
        self.tail = None

    def check_empty(self):
        return self.head == None
    
    def length(self):
        if self.head == None:
            return 0
        current = self.head
        len = 1
        while current.next != None:
            len += 1
            current = current.next
        return len
    
    def add_to_tail(self, model):
        newNode = Node(model)
        if self.check_empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def delete_by_name(self, name):
        if self.check_empty():
            return
        elif self.head == self.tail:
            self.head = self.tail = None
            return
        else:
            current = self.head
            while current is not None and current.next is not None:
                if current.next.model.name == name:
                    current.next = current.next.next
                    return
                current = current.next
                
    def sort_by_year(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append((current.model.name, current.model.month, current.model.year))
            current = current.next
        nodes.sort(key=lambda x: x[2])
        current = self.head
        current = self.head
        for name, month, year in nodes:
            current.model.name = name
            current.model.month = month
            current.model.year = year
            current = current.next
        
    def display(self):
        if self.length() == 0:
             print("Empty list")
        else:
             current = self.head
             while current != None:
                 print(f"{current.model.name} - {current.model.month}/{current.model.year}")
                 current = current.next
             print()
             
LLM_LL = LLMLinkedListManager()

LLM_LL.add_to_tail(Model('FLAN', 9, 2021))
LLM_LL.add_to_tail(Model('BERT', 10, 2018))
LLM_LL.add_to_tail(Model('Transformers', 6, 2017))
LLM_LL.add_to_tail(Model('ChatGPT', 11, 2022))
LLM_LL.add_to_tail(Model('GPT-3', 5, 2020))
LLM_LL.add_to_tail(Model('GPT', 6, 2018))
LLM_LL.add_to_tail(Model('GPT-2', 2, 2019))
LLM_LL.add_to_tail(Model('DeepSeek_R1', 1, 2025))
LLM_LL.add_to_tail(Model('GPT-4o', 3, 2024))
LLM_LL.add_to_tail(Model('LLaMA', 2, 2023))

LLM_LL.sort_by_year()
LLM_LL.display()

LLM_LL.delete_by_name("BERT")
LLM_LL.display()