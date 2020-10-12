VERSION=0.1

fmt:
	@find . -type f -name \*.py -print0 | xargs -0 black && \
	black src/pytaskr

build:
	@echo "Building image" && \
	cd src && \
	docker build --no-cache=true --rm -t mwalters/pytaskr:$(VERSION) .

run:
	docker run --rm -d --name pytaskr mwalters/pytaskr:$(VERSION) && \
	docker logs -f pytaskr

stop:
	docker stop pytaskr
