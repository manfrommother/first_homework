class ObjList:
    
    def __init__(self, data: str):
        self.__prev = None
        self.__data = data
        self.__next = None

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: str):
        self.__data = data


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        '''Добалвяем переданный объект в конец списка'''
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj
    
    def remove_obj(self, obj: ObjList):
        """Удаляет указанный объект из списка"""
        if self.head is obj and self.tail is obj:
            self.head = self.tail = None
        elif obj is self.head:
            self.head = obj.next
            self.head.prev = None
        elif obj is self.tail:
            self.tail = obj.prev
            self.tail.next = None
        else:
            obj.prev.next = obj.next
            obj.next.prev = obj.prev
        
        obj.prev = obj.next = None

    def get_data(self) -> str:
        '''Возвращает строку с данными всех объектов'''
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return ' '.join(result)
    
