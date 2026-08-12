FROM wordpress:latest

RUN apt-get update \
    && apt-get install -y curl less \
    && curl -o /usr/local/bin/wp https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
    && chmod +x /usr/local/bin/wp \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*