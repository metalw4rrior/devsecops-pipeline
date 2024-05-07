

stages:
  - test

variables:
  TRUFFLEHOG_RESULTS_PATH: "trufflehog_results.json"

find_secrets:
  stage: test
  image: python:3.9
  script:
    - pip install trufflehog
    - trufflehog --json https://gitlab-ci-token:$CI_JOB_TOKEN@your.gitlab.server/namespace/repo.git#$CI_COMMIT_SHA > $TRUFFLEHOG_RESULTS_PATH
  artifacts:
    paths:
      - $TRUFFLEHOG_RESULTS_PATH

