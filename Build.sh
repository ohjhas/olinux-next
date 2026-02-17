echo Build using mkarchiso
rm -rf ISOs/*
sudo mkarchiso -v -r -w WorkDir -o ISOs Sources/
