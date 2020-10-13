VERSION=0.2.0

fmt:
	@find . -type f -name \*.py -print0 | xargs -0 black && \
	black src/pytaskr

build:
	@echo "Building image" && \
	cd src && \
	docker build --no-cache=true --rm -t pylios/pytaskr:$(VERSION) -t pylios/pytaskr:latest .

run:
	docker run --rm -d --name pytaskr pylios/pytaskr:$(VERSION) && \
	docker logs -f pytaskr

stop:
	docker stop pytaskr

push:
	docker push pylios/pytaskr:$(VERSION) && \
	docker push pylios/pytaskr:latest
