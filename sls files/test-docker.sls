# Файл: test_docker_security.sls

# Установка пакета docker.io
install_docker:
  pkg.installed:
    - name: docker.io

# Перезапуск службы Docker
restart_docker_service:
  service.running:
    - name: docker
    - enable: True
    - watch:
      - pkg: install_docker

# Загрузка образа для тестирования безопасности (Clair)
load_security_scanner_image:
  cmd.run:
    - name: docker pull quay.io/coreos/clair:latest

# Запуск контейнера с инструментом тестирования безопасности
run_security_scanner_container:
  cmd.run:
    - name: docker run -d --name clair-container -p 6060:6060 quay.io/coreos/clair:latest

# Ожидание запуска контейнера с инструментом тестирования безопасности
wait_for_security_scanner_container:
  cmd.wait:
    - name: docker ps | grep clair-container
    - timeout: 60
    - watch:
      - cmd: run_security_scanner_container

# Тестирование безопасности Docker контейнеров с помощью инструмента
run_security_tests:
  cmd.run:
    - name: |
        docker exec clair-container clairctl --config /config/config.yaml health

# Удаление контейнера с инструментом тестирования безопасности
remove_security_scanner_container:
  cmd.run:
    - name: docker rm -f clair-container

# Удаление загруженного образа инструмента тестирования безопасности
remove_security_scanner_image:
  cmd.run:
    - name: docker rmi quay.io/coreos/clair:latest


#salt-call state.apply test_docker_security