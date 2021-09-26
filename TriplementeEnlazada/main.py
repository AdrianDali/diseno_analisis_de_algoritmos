from triplemente_enlazada import TripleLinkedList

def run():
    TripleLista = TripleLinkedList()
    print(f"La lista esta vacia? {TripleLista.is_empty()}")
    TripleLista.append(20)
    TripleLista.append(23)
    TripleLista.append(57)
    TripleLista.append(19)
    TripleLista.append(67)
    TripleLista.append(90)


    TripleLista.transversal()
    



if __name__ == "__main__":
    run()