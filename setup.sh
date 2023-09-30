# Quick setup script for this stupid little programme.
# This is probably needlessly complicating everything but this is my program so fuck you.
PYGAME_REQ_VER="pygame==2.5.2"
echo "Before procceeding, please make sure you are running from the projects root directory. Press any key to continue."
read -n 1 -s -r
echo "Setting up necessary directories..."
(mkdir -p ./logs && echo "Successfully created directory 'logs'") || echo "Failed to create log directory, try running as root."
pygame_version=$(pip freeze | grep -e $PYGAME_REQ_VER) || echo "Please make sure pip is installed and try again."
## If required version of pygame is not installed
if [[ -z $pygame_version ]]; then
    echo "$PYGAME_REQ_VER not found, installing..."
    pip install $PYGAME_REQ_VER && echo "Successfuly installed pygame" || echo "Something went wrong, please see error message and try again."
elif [[ -n $pygame_version ]]; then
    echo "Pygame already installed."
else
    echo "How the actual fuck did you even get here?"
fi
echo "Jobs done :)"