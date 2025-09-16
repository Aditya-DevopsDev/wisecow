#!/usr/bin/env bash

SRVPORT=4499

prerequisites() {
    command -v cowsay >/dev/null 2>&1 &&
    command -v fortune >/dev/null 2>&1 &&
    command -v nc >/dev/null 2>&1 ||
    { 
        echo "Install prerequisites."
        exit 1
    }
}

main() {
    prerequisites
    echo "Wisdom served on port=$SRVPORT..."

    while true; do
        # Read one request at a time
        { 
            read request_line
            fortune_text=$(fortune)
            echo -e "HTTP/1.1 200 OK\n\n<pre>$(cowsay "$fortune_text")</pre>"
        } | nc -l -p $SRVPORT -q 1
    done
}

main
