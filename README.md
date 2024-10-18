
# DevSecOps Pipeline

Автоматизированный CI/CD процесс для сборки, тестирования и деплоя приложения в Kubernetes кластере с использованием GitLab Runner, работающего внутри пода Kubernetes.

## 🛠 Используемые технологии

- **GitLab** – CI/CD платформа
- **Docker** – контейнеризация приложений
- **SonarQube** – анализ качества кода
- **Safety** – сканирование зависимостей Python
- **Bandit** – статический анализ безопасности Python
- **Kubernetes** – оркестрация контейнеров

## 📁 Структура проекта

```bash
.
├── app/                      # Пример приложения
├── .gitlab-ci.yml             # Конфигурация CI/CD пайплайна
├── sonar-project.properties   # Конфигурация SonarQube
├── kubeconfig.yaml            # Пример Kubernetes конфигурации
└── your-app.yaml              # Пример манифеста для Kubernetes
```

## ⚙️ Настройка CI/CD

Для работы пайплайна необходимо добавить переменные окружения в GitLab.

### Переменные для Kubernetes и Docker

| Переменная                | Описание                                                               |
|---------------------------|------------------------------------------------------------------------|
| `KUBERNETES_API_URL`       | Адрес API Kubernetes кластера                                          |
| `KUBERNETES_NAMESPACE`     | Пространство имен, где будет развернуто приложение                     |
| `KUBERNETES_CA_CERT`       | Корневой сертификат Kubernetes                                         |
| `KUBERNETES_CLIENT_CERT`   | Сертификат клиента (роли), с которым работает раннер                   |
| `KUBERNETES_CLIENT_KEY`    | Ключ клиента (роли), с которым работает раннер                         |
| `DOCKER_USER`              | Логин для Docker registry                                              |
| `DOCKER_PASSWORD`          | Пароль для Docker registry                                             |
| `DOCKER_SOCK`              | `unix:///var/run/docker.sock` – путь к Docker сокету                    |
| `DOCKER_HOST`              | Адрес Docker registry                                                 |
| `DOCKER_IMAGE`             | Имя Docker образа с приложением                                        |

## 📜 Основные этапы пайплайна

1. **Сборка Docker образа**: Собирает Docker образ и пушит его в указанный Docker registry.
2. **Статический анализ кода**:
    - **SonarQube** проверяет качество кода.
    - **Bandit** сканирует Python код на уязвимости.
    - **Safety** проверяет зависимости Python на наличие уязвимых библиотек.
3. **Деплой в Kubernetes**: После успешных проверок приложение деплоится в кластер.

## 🚀 Деплой в Kubernetes

Пример Kubernetes манифеста для деплоя приложения:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: your-app
  namespace: your-namespace
spec:
  replicas: 2
  selector:
    matchLabels:
      app: your-app
  template:
    metadata:
      labels:
        app: your-app
    spec:
      containers:
      - name: your-app
        image: ${DOCKER_IMAGE}:latest
        ports:
        - containerPort: 80
```

## 📝 Примечания

1. Убедитесь, что GitLab Runner настроен на использование Docker.
2. Добавьте переменные окружения для Kubernetes и Docker registry в настройках проекта:  
   `Settings > CI/CD > Variables`.


