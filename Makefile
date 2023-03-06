.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec aws-sso-dev --no-session -- sam deploy

deploy-site:
	aws-vault exec aws-sso-dev --no-session -- aws s3 sync ./resume-site s3:://bmkrresume