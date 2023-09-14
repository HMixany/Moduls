class A:
    @staticmethod         # Дозволяє визвати цей метод без создания екземпляру класу. Він не має доступу до екземпляру.
    def method():
        print('asd')



A().method()