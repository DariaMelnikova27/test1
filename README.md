Проектная работа к курсу "Python QA Engineer"

- Репозиторий содержит автотесты для сайта https://spb.ticketland.ru/
- Тесты возможно запускать как локально, так и удаленно (remote/local)
- Присутствует Dockerfile, позволяющий запустить тесты в контейнере (команда docker build -t tests . и docker run --name tests_run tests)
- По результатам прогона формируется Allure отчет (команда ~/Downloads/allure/allure-2.20.1/bin/allure generate allure-results/ --clean
, где ~/Downloads/allure/allure-2.20.1/bin/allure - путь до утилиты allure)
- Также предусмотрен запуск в Jenkins
- Применен паттерн PageObject
