#Надстройка над sb\_smpp\_sdk для более простого взаимодействия

# Введение #

**sb\_smpp\_helper** это помошник в работе с sb\_smpp\_sdk. Он реализует часть методов сильно упрощающих работу при формировании и разборе большинства пакетов.

# Детали #

sb\_smpp\_helper реализует функционал отправки и получения сообщений, в упрощенном для пользователя формате. Теперь нет необходимости читать документацию по протоколу, helper все сделает за вас.

# Методы и классы #

**class hlp\_smpp()** - реализует все основные настройки соединения и параметры отправки сообщений.
Конструктор:
> service\_type,source\_addr\_ton,source\_addr\_npi,source\_addr="",
> dest\_addr\_ton=1,dest\_addr\_npi=1,destination\_addr="",esm\_class=0x00000000,protocol\_id=0,\
> > priority\_flag=0,schedule\_delivery\_time="",validity\_period="",registered\_delivery=0,\
> > replace\_if\_present\_flag=0,data\_coding=0x00000000



