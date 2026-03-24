#!/usr/bin/env bash

# commit folders first
for dir in */; do
    git add "$dir"
    git commit -m "Add $(basename "$dir") directory"
done

# commit files in human task order
for dir in */; do
    for file in $(ls "$dir" | sort -V); do
        path="$dir$file"

        if [ -f "$path" ]; then
            task=$(echo "$file" | cut -d'-' -f1)
            name=$(echo "$file" | cut -d'-' -f2- | sed 's/\..*//')

            git add "$path"
            git commit -m "Task $task: $name"
        fi
    done
done

