echo Build using mkarchiso
echo OmegaLinux NEXT build ¡START!
rm -rf ISOs/*
sudo mkarchiso -v -r -w WorkDir -o ISOs Sources/
echo OmegaLinux NEXT build ¡FINISH!
((sec=SECONDS%60, min=SECONDS/60%60, hrs=SECONDS/3600))
timestamp=$(printf "OLN Build took %02d hours, %02d minutes, and %02d seconds." $hrs $min $sec)
echo $timestamp
