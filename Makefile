SHELL:=/bin/bash

.PHONY: build
.SILENT: integration-test

build:
	sam build

deploy-infra:
	sam build && aws-vault exec aws-sso-dev --no-session -- sam deploy

deploy-site:
	aws-vault exec aws-sso-dev --no-session -- aws s3 sync ./resume-site s3://bmkrresume

invoke-get:
	sam build && aws-vault exec aws-sso-dev --no-session -- sam local invoke GetFunction

invoke-put:
	sam build && aws-vault exec aws-sso-dev --no-session -- sam local invoke PutFunction

run-unit-tests:
	aws-vault exec aws-sso-dev --no-session -- python -m pytest tests/unit/test_handler.py

integration-test:
	FIRST=$$(curl -s "https://yz8xehlav7.execute-api.ap-southeast-2.amazonaws.com/Prod/get" | jq ".visits| tonumber");\
	curl -s "https://yz8xehlav7.execute-api.ap-southeast-2.amazonaws.com/Prod/put";\
	SECOND=$$(curl -s "https://yz8xehlav7.execute-api.ap-southeast-2.amazonaws.com/Prod/get" | jq ".visits| tonumber");\
	echo "Comparing if first count ($$FIRST) is less than (<) second count ($$SECOND)"; \
	if [[ $$FIRST -le $$SECOND ]]; then echo "PASS"; else echo "FAIL";  fi