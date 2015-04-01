#Описание средства разработки sb\_smpp\_sdk

# Введение #
Описание средств разработки приложений использующих протокол SMPP 3.4


# Модули #

**sb\_pdu** - модуль формирования пакетов PDU (Protocol Data Unit)
Реализует базовые пакеты для работы протокола, для реализации основных классов.

**sb\_smpp** - модуль реализует основные пакеты протокола, все реализованные пакеты наследуют базовые, реализованные в sb\_pdu

**sb\_smpp\_opt** - модуль реализует поддержку опциональных полей (TLV пакеты)

**smpputil** - модуль реализующий дополнительный функционал, конвертирование и текстовое представление информации. Модули sb\_smpp и sb\_pdu используют его.