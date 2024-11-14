#!/bin/bash

# Start the server in a new Terminal window
osascript <<EOF
tell application "Terminal"
    do script "cd $(pwd)/server && node server.js"
end tell
EOF

# Start the client in another new Terminal window
osascript <<EOF
tell application "Terminal"
    do script "cd $(pwd)/client && npm start"
end tell
EOF
