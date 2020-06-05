.PHONY: deploy

deploy:
	git subtree push --prefix get_caged/ heroku master
