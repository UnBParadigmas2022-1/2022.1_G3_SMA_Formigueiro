build:
	docker build -t anthill .

run:
	docker run -it -d -p 8521:8521 --name anthill anthill

stop:
	docker stop anthill
clean:
	docker rm -f anthill
