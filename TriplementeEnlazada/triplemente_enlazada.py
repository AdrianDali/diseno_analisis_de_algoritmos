class NodoTriple():

    def __init__(self, value, siguiente_1=None, siguiente_2=None, siguiente_3=None):
        self.data = value
        self.siguiente_1 = siguiente_1
        self.siguiente_2 = siguiente_2
        self.siguiente_3 = siguiente_3


class TripleLinkedList():
    def __init__(self):
        self.__head = None
        print("lista triplemente ligada")
    
    def append(self,value):
        curr_node = self.__head
        nuevo = NodoTriple(value)
        if self.__head == None:
            self.__head = nuevo 
        else: 
            while curr_node.siguiente_1 != None:
                curr_node = curr_node.siguiente_1
            curr_node.siguiente_1 = nuevo 

    def is_empty(self):
        return self.__head == None

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -->", end="")
            curr_node = curr_node.siguiente_1
        print(" ") 


    


        

