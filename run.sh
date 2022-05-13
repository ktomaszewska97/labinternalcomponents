#!/bin/bash
python appexample/app/view.py ;
python CommunityPlatform/app/view.py &
python Koordinator/app/view.py &
wait