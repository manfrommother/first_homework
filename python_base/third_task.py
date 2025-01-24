class Server:
    """Класс для описания серверов в сети"""
    def __init__(self):
        self.ip = None
        self.__buffer = []

    @property
    def buffer(self):
        """Свойство для доступа к буферу (только чтение)"""
        return tuple(self.__buffer)  # Возвращаем неизменяемую копию

    def send_data(self, data):
        """Отправка информационного пакета data (объекта класса Data) через роутер"""
        Router.send_data(data)

    def get_data(self):
        """Возвращает список принятых пакетов"""
        return self.__buffer[:]  # Возвращаем копию буфера

    def get_ip(self):
        """Возвращает IP-адрес текущего сервера"""
        return self.ip


class Router:
    """Класс для описания роутеров в сети"""
    servers = {}

    @classmethod
    def link(cls, server):
        """Присоединяет сервер к роутеру (регистрирует его в списке servers)"""
        if server.ip is None:
            server.ip = len(cls.servers) + 1
        cls.servers[server.ip] = server

    @classmethod
    def unlink(cls, server):
        """Отсоединяет сервер от роутера"""
        if server.ip in cls.servers:
            del cls.servers[server.ip]

    @classmethod
    def send_data(cls, data):
        """Пересылает пакет data к серверу назначения"""
        if data.ip in cls.servers:
            cls.servers[data.ip]._Server__buffer.append(data)


class Data:
    """Класс для описания пакета информации"""
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip



