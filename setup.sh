FILE_CSV=twcs/twcs.csv
FILE_ZIP=customer-support-on-twitter.zip

cd /app

if test -f "$FILE_CSV"; 
then
    echo "$FILE_CSV exists."
else
    if !(test -f "$FILE_ZIP");
    then
        kaggle datasets download -d thoughtvector/customer-support-on-twitter
    fi
    unzip "$FILE_ZIP"
    #rm "sample.csv"
    #rm "$FILE_ZIP"
fi

