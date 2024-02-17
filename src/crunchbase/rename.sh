rename_path="../../data/crunchbase"
files=$(find "$rename_path/$1" -type f -name "*.csv")

OIFS="$IFS"
IFS=$'\n'
num=0
for f in $files; do
  newf="$rename_path/$1/$2_$num.csv"
  echo "file: $f"
  echo "new file: $newf"
  ((num++))
  mv -- "$f" "${newf}"
done
IFS="$OIFS"