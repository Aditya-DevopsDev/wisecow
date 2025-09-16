FROM debian:stable-slim

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    fortune-mod cowsay netcat-openbsd ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Add /usr/games to PATH (where cowsay & fortune are installed)
ENV PATH="/usr/games:${PATH}"

WORKDIR /app
COPY wisecow.sh /app/wisecow.sh
RUN chmod +x /app/wisecow.sh

EXPOSE 4499
CMD ["/app/wisecow.sh"]
