#!/bin/bash
echo "Welcome to Splash Screen Instalation"
echo "===============================================
     This step will take some important data
from the repository, SKIP if you have previously 
               perform this step.
================================================"
PS3='Please enter your choice: '
options=("Install" "Skip" "Uninstall")
select opt in "${options[@]}"
do
    case $opt in
        "Install")
            echo "Install option selected!"
            echo "Preparing area"
            echo "Installing dependencies"
			sudo apt install -y git inkscape python3 wmctrl
			echo "copying files"
			sudo git clone https://github.com/raniaamina/inkscape-splash-screen.git /opt/Inksplash
			echo "Done!"
            break
            ;;
        "Skip")
            echo "Skip option selected!"
            break
            ;;
  		"Uninstall")
            echo "Uninstall option selected!"
            echo "Unistall Inksplash"
			sudo sed -i "s/Exec=\/opt\/inksplash\/inksplash.py/Exec=inkscape %F/" /usr/share/applications/inkscape.desktop
			sudo rm -rf /opt/Inksplash
			echo "done"
            exit
            ;;
        *) echo invalid option;;
    esac
done

PS3='Please enter your choice: '
options=("Solid Splash" "Transparent Splash")
select opt in "${options[@]}"
do
    case $opt in
        "Solid Splash")
            echo "Solid Splash Screen Selected"
            echo "Preparing area"
            sudo rm -rf /opt/Inksplash/*.py
			sudo rm -rf /opt/Inksplash/*.png
            echo "Installing dependencies"
			sudo apt install -y git inkscape python3 wmctrl
			sudo cp /opt/Inksplash/solid-splash-screen/* /opt/Inksplash/
			sudo sed -i "s/Exec=inkscape %F/Exec=\/opt\/Inksplash\/inksplash.py/" /usr/share/applications/inkscape.desktop
            echo "Done!"
            break
            ;;
        "Transparent Splash")
            echo "Transparent Splash Screen Selected"
            echo "Preparing area"
            sudo rm -rf /opt/Inksplash/*.py
			sudo rm -rf /opt/Inksplash/*.png
            sudo cp /opt/Inksplash/transparent-splash-screen/* /opt/Inksplash/
			sudo sed -i "s/Exec=inkscape %F/Exec=\/opt\/Inksplash\/inksplash.py/" /usr/share/applications/inkscape.desktop
            echo "Done!"
            break
            ;;
        *) echo invalid option;;
    esac
done