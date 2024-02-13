check_path="../../data/crunchbase"
lines=$(find "$check_path/$1" -type f -name "*.csv" -print0 | xargs -0 wc -l | awk 'END {print $1}')
headers=$(find "$check_path/$1" -type f -name "*.csv" | wc -l)
rows=$((lines - headers))

echo "Rows in csvs: $rows"