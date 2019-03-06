
This documents how SC2 game and maps were downloaded and installed. By extracting the archives
you agree to Blizzard's license: http://blzdistsc2-a.akamaihd.net/AI_AND_MACHINE_LEARNING_LICENSE.html

    apt install unzip

    mkdir /opt/sc2-downloads
    cd /opt/sc2-downloads

    wget http://blzdistsc2-a.akamaihd.net/Linux/SC2.4.7.1.zip
    wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season1.zip

    unzip -P iagreetotheeula SC2.4.7.1.zip
    unzip -P iagreetotheeula Ladder2017Season1.zip

    aws s3 cp SC2.4.7.1.zip s3://hagaton2019-sc2-spectator/downloads/
    aws s3 cp Ladder2017Season1.zip s3://hagaton2019-sc2-spectator/downloads/

    ln -s /opt/starcraft2 /home/ubuntu/StarCraftII
    ln -s /opt/starcraft2/Maps /opt/starcraft2/maps

    sudo chmod -R o+r /opt/starcraft2/Maps/
    sudo chmod o+x /opt/starcraft2/Maps/Ladder2017Season1

# Run a bot

    git clone https://github.com/Vilsepi/sc2-landlubber.git
    cd sc2-landlubber
    ./run.sh
