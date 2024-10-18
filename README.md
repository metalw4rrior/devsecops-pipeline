# DevSecOps Pipeline

Этот пайплайн автоматизирует сборку, тестирование  и деплой приложения в кубернетес кластер. 
Гитлаб-раннер является подой кубернетеса.

## Technologies used

- GitLab
- Docker
- SonarQube
- Safety (Python dependency scanner)
- Bandit
- Kubernetes

## Project structure

- `app/`: Тут лежит пример приложения
- `.gitlab-ci.yml`: Конфигурация самого пайплайна
- `sonar-project.properties`: Настройки для SonarQube
- `kubeconfig.yaml`: Пример конфига для подключения к кластеру
- `your-app.yaml`: Пример манифеста для запуска приложения в кластере


## How it works



В настройки проекта - CI/CD - Variables:
-  KUBERNETES_API_URL: Сюда пихай адрес кластера
-  KUBERNETES_NAMESPACE: Сюда пихай пространство имен в котором будешь запускать свои поделки
-  KUBERNETES_CA_CERT: Сюда пихай корневой сертификат кубера
- KUBERNETES_CLIENT_CERT: Сюда пихай сертификат клиента (роли) с которой будет работать раннер
-  KUBERNETES_CLIENT_KEY: Сюда пихай ключ клиента (роли) с которой будет работать раннер
-  DOCKER_USER: Тут логин для докер регистри
-  DOCKER_PASSWORD: Тут пароль для докер регистри
-  DOCKER_SOCK: "unix:///var/run/docker.sock" - Тут сокет докера. Образ гитлаб-раннера лучше собирать с ним вместе. 
-  DOCKER_HOST: Адрес твоего регистри
-  DOCKER_IMAGE: То как ты назовешь контейнер с кодом





