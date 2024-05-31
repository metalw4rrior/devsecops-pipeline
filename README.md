# DevSecOps Pipeline

Конвейер DevSecOps использует GitLab CI/CD, интегрируя методы обеспечения безопасности и проверки соответствия на каждом этапе конвейера. Он создает, тестирует и развертывает образец веб-приложения, включая автоматическое сканирование безопасности и проверку соответствия...

## Technologies used

- GitLab
- Docker
- SonarQube
- Safety (Python dependency scanner)
- Bandit

## Project structure

- `app/`: Содержит исходный код и файл настройки для примера веб-приложения
- `terraform/`: Содержит файлы конфигурации Terraform для предоставления ресурсов инфраструктуры.
- `.gitignore`: файл, указывающий файлы и каталоги, которые должны игнорироваться Git
- `.gitlab-ci.yml`: Определяет конфигурацию конвейера GitLab CI/CD.

## How it works

1. Конвейер GitLab CI/CD запускается при нажатии на код или запросе на слияние.
2. Конвейер создает образ Docker для веб-приложения, используя файл Docker в каталоге `app/`.
3. Конвейер запускает проверку безопасности OpenSCAP в образе Docker с помощью сценария "openscap/dockerfile_scan.sh". Конвейер завершится сбоем, если будут обнаружены какие-либо уязвимости с высокой степенью риска или несоответствующие конфигурации.
4. Конвейер запускает статическое тестирование безопасности приложений (SAST) с использованием SonarQube для сканирования исходного кода на наличие уязвимостей.
5. Конвейер выполняет автоматическое сканирование зависимостей с использованием Safety для выявления уязвимостей в зависимостях и библиотеках приложения.
6. Конвейер предоставляет ресурсы инфраструктуры с помощью Terraform на основе файлов конфигурации в каталоге "terraform/".
7. Конвейер развертывает контейнер Docker в созданной инфраструктуре.
8. Хранилище HashiCorp Vault используется для безопасного хранения и управления конфиденциальной информацией, такой как ключи API, учетные данные базы данных и SSL-сертификаты. Конвейер интегрируется с Vault для доступа к этим секретам по мере необходимости.
9. Конвейер запускает динамическое тестирование безопасности приложений (DAST) с использованием OWASP ZAP для сканирования веб-приложения на наличие уязвимостей в системе безопасности во время выполнения.
10. Мониторинг и оповещения настраиваются с помощью Prometheus и Grafana для уведомления о событиях безопасности и уязвимостях, обнаруженных во время выполнения конвейера или в развернутом приложении.
11. В конвейере реализован механизм отката для восстановления состояния инфраструктуры в случае сбоев развертывания или критических уязвимостей в системе безопасности.

## Getting started

1. Clone the repository
2. Set up a GitLab project and configure the necessary environment variables for GitLab CI/CD, such as Docker registry credentials, Terraform backend configuration, and HashiCorp Vault access tokens.
3. Make changes to the Terraform configuration files in the `terraform/` directory as needed, based on your infrastructure requirements.
4. Configure the OpenSCAP scanning policy in the `openscap/` directory.
5. Set up a SonarQube server and configure a project for your application.
6. Deploy and configure Prometheus and Grafana for monitoring and alerting.
7. Push your changes to the GitLab project, which will trigger the CI/CD pipeline. 
8. Monitor the pipeline execution in GitLab and review the logs to ensure all stages are successful and that security scans and compliance checks are being performed as expected.**



