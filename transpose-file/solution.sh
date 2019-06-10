# Read from the file file.txt and print its transposed content to stdout.
cat file.txt | awk '{
    for (i=1; i<=NF; i++) {
        # 为了格式化输出的空格
        if (NR==1) {
            res[i]=$i
        } else {
            res[i]=res[i] " " $i
        }
    }
}
END {
    for (i=1; i<=NF; i++) {
        print res[i]
    }
}'
