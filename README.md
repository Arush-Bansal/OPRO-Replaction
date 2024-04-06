## SETUP

### REDIS DOCKER SETUP
1. Make sure that you have docker desktop installed in your computer
2. Run `docker pull redis` to install redis on your computer
3. Run `docker run --name my-redis-container -d -p 6379:6379 redis` to run the redis container


## FEW HANDY COMMANDS FOR DOCKER

1. `docker run --name my-redis-container -d -p 6379:6379 redis` : turn the container up
2. `docker exec -it my-redis-container redis-cli` : terminal now runs with location of docker container.
3. `127.0.0.1:6379> ping` : run when termial switches to the container. output is PONG
3. `127.0.0.1:6379> exit` : switches the terimal back to orignal location